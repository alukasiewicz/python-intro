# =============================================================================
# my_awesome_lib/text_processing.py
# =============================================================================
"""Lekki zestaw funkcji tekstowych – zero zależności heavy‑NLP."""
from __future__ import annotations

import unicodedata
from typing import List, Tuple

# Kody kategorii Unicode dla znaków diakrytycznych (łączących)
_COMBINING_MARK = {"Mn", "Mc"}

# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def strip_accents(text: str) -> str:
    """Usuwa polskie znaki diakrytyczne (łącznie z „ł/Ł”).

    *Krok 1*  Unicode NFD dzieli znaki z akcentami na: znak bazowy + znak łączący.
    *Krok 2*  odrzucamy wszystkie **łączące**.
    *Krok 3*  wciąż pozostają litery z przekreśleniem („ł/Ł”), bo to *osobne* kody
    Unicode kategorii ``Ll``/``Lu`` (a nie łączące).  Zamieniamy je ręcznie na
    odpowiedniki ASCII.
    """
    normalized = unicodedata.normalize("NFD", text)
    no_combining = "".join(
        ch for ch in normalized if unicodedata.category(ch) not in _COMBINING_MARK
    )
    # "ł" i "Ł" nie mają wariantu złożonego, więc mapujemy je ręcznie.
    translation = str.maketrans({"ł": "l", "Ł": "L"})
    return no_combining.translate(translation)


def tokenize(text: str, *, keep_punct: bool = False) -> List[str]:
    """Bardzo prosta tokenizacja.

    Działa bez zewnętrznych bibliotek NLP:

    * ``keep_punct=False`` litery/cyfry są tokenami, interpunkcja wyrzucana,
    * ``keep_punct=True`` znaki interpunkcyjne traktujemy jako osobne tokeny.
    """
    tokens: List[str] = []
    buff = ""
    for ch in text:
        if ch.isalnum():               # litera/cyfra – dodaj do bufora
            buff += ch
        else:
            if buff:                   # koniec słowa → zapisz do listy
                tokens.append(buff)
                buff = ""
            if keep_punct and not ch.isspace():
                tokens.append(ch)      # pojedynczy znak interpunkcji jako token
    if buff:
        tokens.append(buff)
    return tokens


def ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
    """Generuje kolejne *n*-gramy (krotki) z listy *tokens*.

    Parametry
    ----------
    tokens : list[str]
        Lista tokenów (np. wynik `tokenize`).
    n : int (> 0)
        Długość n gramu.

    Zwraca
    -------
    list[tuple[str, ...]]
        N gramy w kolejności występowania.
    """
    if n <= 0:
        raise ValueError("n must be > 0")
    # List‑comp: przesuwamy okno długości n po tokenach.
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
