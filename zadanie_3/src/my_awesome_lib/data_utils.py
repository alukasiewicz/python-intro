# =============================================================================
# my_awesome_lib/data_utils.py
# =============================================================================
"""Funkcje wspomagające pracę z danymi i zagnieżdżonymi słownikami."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Dict, List, Mapping


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def load_csv(path: str | Path, *, separator: str = ",") -> List[Dict[str, str]]:
    """Czyta plik CSV i zwraca go jako listę słowników.

    Parametry
    ----------
    path : str | Path
        Ścieżka do pliku CSV z wierszem nagłówkowym (nazwy kolumn) w pierwszej
        linii.
    separator : str, domyślnie `","`
        Separator kolumn.  Ustaw na `";"` dla plików w stylu Excel-owskim.

    Zwraca
    -------
    list[dict[str, str]]
        Każdy wiersz to słownik ``{nazwa_kolumny: wartość}`` *bez rzutowania
        typów* - wszystkie wartości pozostają łańcuchami znaków.

    Wyjątki
    --------
    FileNotFoundError
        Gdy wskazany plik nie istnieje.
    ValueError
        Gdy plik nie zawiera nagłówka.
    """
    path = Path(path)

    # ── 1. Walidacja wejścia ────────────────────────────────────────────────
    if not path.exists():
        raise FileNotFoundError(path)

    # ── 2. Odczyt pliku za pomocą DictReader ───────────────────────────────
    with path.open(newline="", encoding="utf-8") as fp:
        reader = csv.DictReader(fp, delimiter=separator)
        rows = list(reader)  # wczytujemy cały plik do pamięci (zwykle niewielki)

    # ── 3. Kontrola jakości ─────────────────────────────────────────────────
    if not reader.fieldnames:
        raise ValueError("CSV file has no header – cannot build dict keys")

    return rows


def flatten_dict(d: Mapping[str, Any], *, sep: str = ".") -> Dict[str, Any]:
    """Spłaszcza dowolnie zagnieżdżony słownik.

    Wejście: ``{"a": {"b": 1, "c": {"d": 2}}, "e": 3}``
    Wyjście: ``{"a.b": 1, "a.c.d": 2, "e": 3}``

    Parametry
    ----------
    d : Mapping[str, Any]
        Źródłowy słownik (może zawierać kolejne słowniki wewnątrz).
    sep : str, domyślnie "."
        Separator używany do łączenia kluczy kolejnych poziomów.
    """
    out: Dict[str, Any] = {}

    def _walk(curr: Mapping[str, Any], prefix: str | None = None) -> None:
        """Rekurencyjny spacer po gałęziach słownika."""
        for key, value in curr.items():
            full_key = f"{prefix}{sep}{key}" if prefix else key
            if isinstance(value, Mapping):
                # Zagnieżdżony słownik – wchodzimy głębiej.
                _walk(value, full_key)
            else:
                out[full_key] = value  # Liść – zapisujemy wartość.

    _walk(d)
    return out