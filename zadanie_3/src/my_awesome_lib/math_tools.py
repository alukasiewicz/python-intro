# =============================================================================
# my_awesome_lib/math_tools.py
# =============================================================================
"""Podstawowe narzędzia matematyczne / statystyczne bez zależności zewnętrznych."""
from __future__ import annotations

from math import sqrt
from typing import Iterable, Sequence


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def mean_weighted(values: Sequence[float], weights: Sequence[float]) -> float:
    """Średnia ważona.

    Funkcja przyjmuje dwie sekwencje tej samej długości: *values* (wartości)
    oraz *weights* (wagi).  Wynik to suma iloczynów ``v * w`` podzielona przez
    łączną wagę.

    Wyjątki
    --------
    ValueError
        Gdy sekwencje mają różne długości lub suma wag ≤ 0.
    """
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")

    total_weight = sum(weights)
    if total_weight <= 0:
        raise ValueError("sum(weights) must be > 0")

    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight


def std_dev(sample: Iterable[float], *, ddof: int = 1) -> float:
    """Odchylenie standardowe próbki (*ddof=1*) lub populacji (*ddof=0*).

    Parametry
    ----------
    sample : Iterable[float]
        Próbka liczb.
    ddof : int, domyślnie `1`
        *Delta Degrees of Freedom* - gdy ``0`` obliczamy odchylenie populacyjne,
        gdy ``1``- próbkę (korekta Bessela).

    Zwraca
    -------
    float
        Odchylenie standardowe.

    Wyjątki
    --------
    ZeroDivisionError
        Gdy ``len(sample) − ddof <= 0`` - za mało obserwacji.
    """
    xs = list(sample)               # Przerabiamy iterator na listę, by użyć kilka razy.
    n = len(xs)
    if n - ddof <= 0:
        raise ZeroDivisionError("not enough observations for given ddof")

    mean = sum(xs) / n              # Średnia arytmetyczna.
    var = sum((x - mean) ** 2 for x in xs) / (n - ddof)  # Wariancja.
    return sqrt(var)
