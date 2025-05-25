# Biblioteka my\_awesome\_lib

Lekka biblioteka narzędziowa napisana w Pythonie, oferująca moduły do pracy z plikami CSV, obliczeń statystycznych oraz przetwarzania tekstu.

## Workflow

![CI](https://github.com/alukasiewicz/python-intro/actions/workflows/python-package.yml/badge.svg)


##  Spis plików i opis

* **`.gitignore`**: lista plików i katalogów ignorowanych przez Git (środowisko wirtualne, cache Pythona, pliki tymczasowe).
* **`pyproject.toml`**: metadane projektu, zależności oraz konfiguracja build-backend.
* **`README.md`**: dokumentacja projektu i instrukcje użycia.
* **`LICENSE`**: warunki licencji MIT.
* **`src/my_awesome_lib/__init__.py`**: inicjalizuje pakiet `my_awesome_lib`.
* **`src/my_awesome_lib/data_utils.py`**: moduł I/O dla plików CSV.
* **`src/my_awesome_lib/math_tools.py`**: moduł z funkcjami statystycznymi.
* **`src/my_awesome_lib/text_processing.py`**: moduł do podstawowego przetwarzania tekstu.
* **`tests/test_data_utils.py`**: testy jednostkowe dla `data_utils.py`.
* **`tests/test_math_tools.py`**: testy jednostkowe dla `math_tools.py`.
* **`tests/test_text_processing.py`**: testy jednostkowe dla `text_processing.py`.
* **`.github/workflows/python-package.yml`**: definicja CI w GitHub Actions (instalacja, pytest, coverage).

##  Funkcjonalności

* **data\_utils**

  * `load_csv(path, *, separator=',')`: wczytuje pliki CSV do listy słowników.
  * `flatten_dict(d, *, sep='.')`: spłaszcza zagnieżdżone słowniki.
* **math\_tools**

  * `mean_weighted(values, weights)`: oblicza średnią ważoną.
  * `std_dev(sample, *, ddof=1)`: oblicza odchylenie standardowe.
* **text\_processing**

  * `strip_accents(text)`: usuwa znaki diakrytyczne.
  * `tokenize(text, *, keep_punct=False)`: dzieli tekst na tokeny.
  * `ngrams(tokens, n)`: generuje n-gramy z listy tokenów.

##  Instalacja

Zainstaluj bibliotekę w trybie developerskim:

```bash
pip install -e src/my_awesome_lib/
```

albo z głównego katalogu:

```bash
pip install -e .
```

##  Przykłady użycia

### Praca z CSV

```python
from my_awesome_lib.data_utils import load_csv, flatten_dict

# Wczytywanie pliku CSV z separatorem ';'
rows = load_csv('data.csv', separator=';')
# Przykład spłaszczenia zagnieżdżonego słownika
nested = {'user': {'id': 1, 'info': {'name': 'Alice'}}}
flat = flatten_dict(nested, sep='_')
print(flat)  # {'user_id': 1, 'user_info_name': 'Alice'}
```

### Operacje statystyczne

```python
from my_awesome_lib.math_tools import mean_weighted, std_dev

values = [10, 20, 30]
weights = [1, 2, 1]
print(mean_weighted(values, weights))
# 20.0

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(std_dev(data, ddof=0))  # populacyjna
print(std_dev(data, ddof=1))  # próbka
```

### Przetwarzanie tekstu

```python
from my_awesome_lib.text_processing import strip_accents, tokenize, ngrams

text = 'Zażółć, gęślą jaźń!'
clean = strip_accents(text)
print(clean)  # 'Zazolc, gesla jazn!'

tokens = tokenize(clean, keep_punct=False)
print(tokens)  # ['Zazolc', 'gesla', 'jazn']

tokens_punct = tokenize(clean, keep_punct=True)
print(tokens_punct)  # ['Zazolc', ',', 'gesla', 'jazn', '!']

print(ngrams(tokens, 2))
# [('Zazolc', 'gesla'), ('gesla', 'jazn')]

print(ngrams(tokens_punct, 3))
# [('Zazolc', ',', 'gesla'), (',', 'gesla', 'jazn'), ('gesla', 'jazn', '!')]
```

##  Testy

Uruchom testy za pomocą:

```bash
pytest --maxfail=1 --disable-warnings -q
```

##  CI/CD

Konfiguracja GitHub Actions znajduje się w `.github/workflows/python-package.yml`, automatyzująca budowanie, testy oraz raportowanie pokrycia.

##  Licencja

Projekt udostępniony na licencji MIT. Dokładne warunki w pliku `LICENSE`.

##  Autor

Adrian Łukasiewicz
