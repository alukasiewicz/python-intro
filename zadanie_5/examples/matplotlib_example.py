"""
Przykład 1: Wykres liniowy i słupkowy w Matplotlib

Matplotlib to najbardziej wszechstronna biblioteka do wizualizacji w Pythonie.
Pozwala tworzyć wykresy dowolnego typu, z pełną kontrolą nad wyglądem.
"""

import matplotlib.pyplot as plt
import numpy as np

# Dane do wykresu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Wykres liniowy
plt.figure(figsize=(7, 4))
plt.plot(x, y, label="sin(x)")
plt.title("Wykres funkcji sinus")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Wykres słupkowy
categories = ["A", "B", "C", "D"]
values = [12, 7, 9, 15]

plt.figure(figsize=(5, 3))
plt.bar(categories, values, color="skyblue")
plt.title("Prosty wykres słupkowy")
plt.ylabel("Wartość")
plt.tight_layout()
plt.show()
