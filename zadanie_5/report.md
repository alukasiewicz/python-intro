# Sprawozdanie – Lab 5: Przegląd bibliotek do wizualizacji danych w Pythonie

**Autor:** Adrian Łukasiewicz  
**Data:** 2024-06-19

---

## 1. Dziedzina i cel

Wybrałem dziedzinę **wizualizacji danych** w Pythonie, ponieważ jest ona kluczowa w analizie statystycznej, uczeniu maszynowym i komunikacji wyników. Przetestowałem dwie najważniejsze biblioteki: Matplotlib i Seaborn.

---

## 2. Matplotlib

- **Opis:** Podstawowa i najpotężniejsza biblioteka do wykresów. Pozwala tworzyć dowolne wizualizacje (linie, słupki, koła, rozrzut, mapy ciepła).
- **Link:** [https://matplotlib.org/](https://matplotlib.org/)
- **Instalacja:**  
  `pip install matplotlib`

**Przykład użycia:**  
Zobacz [examples/matplotlib_example.py](examples/matplotlib_example.py)

**Zalety:**
- Pełna kontrola nad każdym aspektem wykresu.
- Szeroki wybór typów wykresów (2D i 3D).
- Standard branżowy, ogromna społeczność.

**Ograniczenia:**
- Składnia bywa rozbudowana, szczególnie przy zaawansowanych layoutach.
- Styl domyślny jest prosty; do ładniejszych wykresów trzeba stylizować ręcznie.

---

## 3. Seaborn

- **Opis:** Rozszerzenie Matplotlib z domyślnie „ładnymi” wykresami, uproszczonym API dla danych statystycznych, integracja z Pandas.
- **Link:** [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- **Instalacja:**  
  `pip install seaborn`

**Przykład użycia:**  
Zobacz [examples/seaborn_example.py](examples/seaborn_example.py)

**Zalety:**
- Łatwe wykresy statystyczne z Pandas.
- Automatyczne kolorowanie, style, legendy.
- Szybka eksploracja danych.

**Ograniczenia:**
- Oparty na Matplotlib – nie wszystko można łatwo przestylizować.
- Najlepiej działa z DataFrame (Pandas), gorzej z „gołymi” listami/numpy.

---

## 4. Podsumowanie

Obie biblioteki są niezbędne dla każdego analityka danych w Pythonie.  
Matplotlib zapewnia pełną elastyczność, Seaborn pozwala szybciej generować wykresy „prosto z Pandas”.

---

## 5. Linki do dokumentacji

- [Matplotlib – dokumentacja](https://matplotlib.org/stable/contents.html)
- [Seaborn – dokumentacja](https://seaborn.pydata.org/tutorial.html)
- [Przykłady kodu](examples/)

---

> Raport i kody wygenerowane na potrzeby zaliczenia Lab 5.
