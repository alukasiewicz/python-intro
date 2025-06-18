"""Lab 4 – MCDM: Pełna analiza w jednym skrypcie
================================================

*Cel*: Od macierzy decyzyjnej → przez normalizację, wyznaczenie wag (entropia lub równe) → ranking TOPSIS i SPOTIS + wizualizacja.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- Pomocnicza implementacja normalizacji Min-Max ---
def minmax(dm: np.ndarray, types: np.ndarray) -> np.ndarray:
    """Normalizacja Min-Max: każda kolumna do [0, 1], osobno benefit/cost."""
    dm_norm = np.zeros_like(dm, dtype=float)
    for j in range(dm.shape[1]):
        col = dm[:, j]
        min_val, max_val = col.min(), col.max()
        if max_val == min_val:
            dm_norm[:, j] = 0.0
        else:
            if types[j] == 1:
                dm_norm[:, j] = (col - min_val) / (max_val - min_val)
            else:
                dm_norm[:, j] = (max_val - col) / (max_val - min_val)
    return dm_norm

# --- 1. Definicje ---
ALTERNATIVES: list[str] = ["A", "B", "C", "D"]
CRITERIA: list[str] = [
    "CAPEX [mln PLN]",
    "NPV [mln PLN]",
    "ROI [%]",
    "Okres zwrotu [lata]",
]
TYPES: np.ndarray = np.array([-1, 1, 1, -1])

DM: np.ndarray = np.array([
    [120,  60, 18, 5.2],   # A
    [150,  75, 22, 4.8],   # B
    [100,  50, 17, 5.5],   # C
    [130,  68, 20, 4.9],   # D
], dtype=float)

assert DM.shape == (len(ALTERNATIVES), len(CRITERIA)), "Nieprawidłowe wymiary DM"
assert TYPES.size == DM.shape[1], "Nieprawidłowy wektor TYPES"

print("1) Macierz decyzyjna (DM):")
print(DM)
print("Typy kryteriów:", TYPES)

# --- 2. Normalizacja ---
DM_NORM = minmax(DM, TYPES)
print("\n2) Znormalizowana macierz (DM_NORM):")
print(np.round(DM_NORM, 3))

# --- 3. Wagi: entropia (jeśli dostępna), inaczej równe ---
try:
    from pymcdm.weights import entropy
    W: np.ndarray = entropy(DM_NORM)
    print("\n3) Wektor wag (entropia):", np.round(W, 3))
except Exception:
    print("\nUwaga: brak entropy w pymcdm – używamy wag równych.")
    W = np.ones(DM_NORM.shape[1]) / DM_NORM.shape[1]
    print("   Równe wagi:", np.round(W, 3))

# --- 4. Rankingi TOPSIS i SPOTIS ---
from pymcdm.methods import TOPSIS, SPOTIS

# bounds do SPOTIS muszą odpowiadać zakresowi DM_NORM!
bounds = np.array([[DM_NORM[:, j].min(), DM_NORM[:, j].max()] for j in range(DM_NORM.shape[1])])

method_topsis = TOPSIS()
method_spotis = SPOTIS(bounds)

scores_topsis = method_topsis(DM_NORM, W, TYPES)
scores_spotis = method_spotis(DM_NORM, W, TYPES)

topsis_rank = scores_topsis.argsort()[::-1] + 1
spotis_rank = scores_spotis.argsort()[::-1] + 1

print("\n4) Ranking TOPSIS:", topsis_rank)
print("   Ranking SPOTIS:", spotis_rank)

# --- 5. Wizualizacja ---
fig, ax = plt.subplots(figsize=(6, 4))
x = np.arange(len(ALTERNATIVES))
bar_w = 0.35

ax.bar(x - bar_w/2, topsis_rank, bar_w, label="TOPSIS")
ax.bar(x + bar_w/2, spotis_rank, bar_w, label="SPOTIS")

ax.set_xticks(x)
ax.set_xticklabels(ALTERNATIVES)
ax.set_ylabel("Miejsce w rankingu (1 = najlepiej)")
ax.set_title("Porównanie rankingów MCDM: TOPSIS vs SPOTIS")
ax.invert_yaxis()
ax.legend()
plt.tight_layout()

out_dir = Path("figures")
out_dir.mkdir(exist_ok=True)
fig_path = out_dir / "ranking_compare.png"
plt.savefig(fig_path, dpi=150)
print(f"\n5) Wykres zapisany: {fig_path}")
plt.show()
