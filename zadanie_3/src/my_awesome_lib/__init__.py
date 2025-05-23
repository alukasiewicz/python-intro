# =====================
# my_awesome_lib/__init__.py
# =====================
"""Wygodne eksporty modułu *my_awesome_lib*.

Pakiet składa się z trzech pod‑modułów:

* ``data_utils`` - operacje na plikach i strukturach danych,
* ``math_tools`` - statystyka opisowa bez zależności zewnętrznych,
* ``text_processing``   niewielkie funkcje NLP niewymagające ciężkich bibliotek.

Dzięki re eksportom użytkownik może pisać::

    from my_awesome_lib import mean_weighted, load_csv

zamiast dłuższych ścieżek importu.
"""

from .data_utils import flatten_dict, load_csv
from .math_tools import mean_weighted, std_dev
from .text_processing import ngrams, strip_accents, tokenize

__all__: list[str] = [
    "load_csv",
    "flatten_dict",
    "mean_weighted",
    "std_dev",
    "strip_accents",
    "tokenize",
    "ngrams",
]