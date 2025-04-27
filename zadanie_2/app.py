import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    """
    Sprawdza, czy podany adres e-mail jest poprawny.

    Args:
        email (str): Adres e-mail do sprawdzenia.

    Returns:
        bool: True jeśli adres e-mail jest poprawny, False w przeciwnym wypadku.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def calculate_area(shape: str, *params: float) -> float:
    """
    Oblicza pole powierzchni dla podanego typu figury.

    Obsługiwane figury: 'circle', 'rectangle', 'triangle'.

    Args:
        shape (str): Typ figury.
        params (float): Parametry potrzebne do obliczenia pola.

    Returns:
        float: Pole powierzchni.

    Raises:
        ValueError: Jeśli typ figury jest nieobsługiwany lub parametry są nieprawidłowe.
    """
    if shape == 'circle':
        if len(params) != 1:
            raise ValueError("Koło wymaga jednego parametru: promienia.")
        radius = params[0]
        if radius < 0:
            raise ValueError("Promień nie może być ujemny.")
        return 3.14159 * radius ** 2

    elif shape == 'rectangle':
        if len(params) != 2:
            raise ValueError("Prostokąt wymaga dwóch parametrów: długości i szerokości.")
        length, width = params
        if length < 0 or width < 0:
            raise ValueError("Długość i szerokość nie mogą być ujemne.")
        return length * width

    elif shape == 'triangle':
        if len(params) != 2:
            raise ValueError("Trójkąt wymaga dwóch parametrów: podstawy i wysokości.")
        base, height = params
        if base < 0 or height < 0:
            raise ValueError("Podstawa i wysokość nie mogą być ujemne.")
        return 0.5 * base * height

    else:
        raise ValueError("Nieobsługiwany typ figury.")

def filter_even(numbers: list) -> list:
    """
    Zwraca listę parzystych liczb z podanej listy.

    Args:
        numbers (list): Lista liczb.

    Returns:
        list: Lista zawierająca tylko liczby parzyste.

    Raises:
        TypeError: Jeśli argument nie jest listą.
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument musi być listą.")
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]

def convert_date_format(date_str: str) -> str:
    """
    Konwertuje datę z formatu 'YYYY-MM-DD' na 'DD/MM/YYYY'.

    Args:
        date_str (str): Data w formacie 'YYYY-MM-DD'.

    Returns:
        str: Data w formacie 'DD/MM/YYYY'.

    Raises:
        ValueError: Jeśli format daty jest nieprawidłowy.
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano 'YYYY-MM-DD'.")

def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy podany tekst jest palindromem.

    Args:
        text (str): Tekst do sprawdzenia.

    Returns:
        bool: True jeśli tekst jest palindromem, False w przeciwnym wypadku.

    Raises:
        TypeError: Jeśli podany argument nie jest typu string.
    """
    if not isinstance(text, str):
        raise TypeError("Argument musi być łańcuchem znaków.")
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
