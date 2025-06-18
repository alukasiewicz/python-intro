# Sprawozdanie – Lab 4: Analiza MCDM z biblioteką pymcdm

**Autor:** Adrian Łukasiewicz  
**Data:** …

---

## 1. Cel i zakres

Celem ćwiczenia było poznanie analizy wielokryterialnej (MCDM) w Pythonie na przykładzie pymcdm, przeprowadzenie procesu od przygotowania macierzy decyzyjnej przez normalizację, wyznaczenie wag i rankingów TOPSIS/SPOTIS.

---

## 2. Dane wejściowe – macierz decyzyjna

| Alternatywa | CAPEX [mln PLN] | NPV [mln PLN] | ROI [%] | Okres zwrotu [lata] |
|-------------|-----------------|--------------|---------|---------------------|
| **A**       | 120             | 60           | 18      | 5.2                 |
| **B**       | 150             | 75           | 22      | 4.8                 |
| **C**       | 100             | 50           | 17      | 5.5                 |
| **D**       | 130             | 68           | 20      | 4.9                 |

- Typy kryteriów: CAPEX, Okres zwrotu – minimalizujemy (`-1`); NPV, ROI – maksymalizujemy (`1`).

---

## 3. Normalizacja i wyznaczanie wag

- Normalizacja Min-Max do [0, 1] dla każdego kryterium.
- Wagi: równe (`[0.25, 0.25, 0.25, 0.25]`) – funkcja entropy była niedostępna.

---

## 4. Rankingi decyzyjne

| Alternatywa | TOPSIS | SPOTIS |
|-------------|:------:|:------:|
| **A**       |   2    |   3    |
| **B**       |   4    |   1    |
| **C**       |   1    |   4    |
| **D**       |   3    |   2    |

---

## 5. Wizualizacja wyników

![Ranking TOPSIS vs SPOTIS](figures/ranking_compare.png)

---

## 6. Wnioski

- Wyniki TOPSIS i SPOTIS różnią się – metody oceniają alternatywy na podstawie innych algorytmów.
- Równe wagi pozwalają porównać czysto mechanicznie, ale w praktyce warto dobrać je ekspercko lub automatycznie (gdy entropy działa).
- W praktyce przy większych różnicach rankingów warto przeanalizować czułość i wpływ wag.

---

## 7. Pliki projektu

- `mcdm_analysis.py` – kod analizy
- `figures/ranking_compare.png` – wykres
- (opcjonalnie) `report.md` – to sprawozdanie

---