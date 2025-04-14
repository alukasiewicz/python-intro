"""
Program demonstrujący praktyczne użycie:
1. Funkcji zip() do łączenia dwóch list (dystanse i czasy).
2. Modułu math do obliczeń matematycznych.
3. Obsługi wyjątków (ValueError, ZeroDivisionError).
"""

import math  # https://docs.python.org/3/library/math.html

def get_floats_from_user(prompt):
    """
    Funkcja pomocnicza, która pobiera od użytkownika dane typu float,
    rozdzielone spacjami, i zwraca je w postaci listy.
    Jeśli format jest nieprawidłowy, zgłaszany jest wyjątek ValueError.
    """
    # Dokumentacja ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    user_input = input(prompt)
    # map() próbuje przekształcić każdą wartość w float; jeśli się nie uda, poleci ValueError
    return list(map(float, user_input.split()))

def main():
    """
    Funkcja główna programu:
    1. Pobiera od użytkownika dwie listy (dystanse i czasy).
    2. Łączy je za pomocą zip().
    3. Oblicza prędkości średnie dla każdego odcinka.
    4. Liczy średnią prędkość ze wszystkich odcinków, korzystając z modułu math.
    5. Obsługuje ewentualne błędy (ValueError, ZeroDivisionError).
    """
    try:
        # Pobranie listy dystansów (w km)
        distances = get_floats_from_user("Podaj dystanse (km) rozdzielone spacjami: ")
        # Pobranie listy czasów (w h)
        times = get_floats_from_user("Podaj czasy (h) rozdzielone spacjami: ")

        # [Funkcja wbudowana - zip()]
        # https://docs.python.org/3/library/functions.html#zip
        # Łączymy dystanse i czasy w pary; np. [dist1, dist2] i [time1, time2] => [(dist1, time1), (dist2, time2), ...]
        paired_data = zip(distances, times)

        speeds = []  # przechowa wyliczone prędkości
        for dist, t in paired_data:
            # Obsługa potencjalnego błędu dzielenia przez zero (ZeroDivisionError)
            # Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
            speed = dist / t  # km / h
            speeds.append(speed)

        # Wyświetlenie wszystkich obliczonych prędkości
        print("Prędkości średnie na każdej trasie (km/h):", speeds)

        if speeds:  # upewniamy się, że lista nie jest pusta
            
            # [Moduł math]
            # math.sqrt() – https://docs.python.org/3/library/math.html#math.fsum
            avg_speed = math.fsum(speeds) / len(speeds)  # fsum() zapewnia większą precyzję sumowania floatów
            print(f"Średnia prędkość: {avg_speed:.2f} km/h")
              
        else:
            print("Nie wprowadzono żadnych danych lub któraś lista jest pusta.")
    
    except ValueError:
        print("Błąd: wprowadzono niepoprawny format danych (nie można skonwertować do float).")
    except ZeroDivisionError:
        print("Błąd: próba dzielenia przez zero (któryś z czasów jest równy zero).")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
