# Podstawy Programowania 2026/2027

Ćwiczenia z przedmiotu Podstawy Programowania w roku akademickim 2026/2027.

## Jaki jest cel

Każde ćwiczenie to para: **mały plik z kodem + plik z testami**. Testy opisują,
jak kod ma się zachowywać. To one są specyfikacją. Twoim zadaniem jest
**dopisać implementację tak, aby testy przeszły**.

Metoda pracy (TDD - Test Driven Development):

1. Otwierasz plik z ćwiczenia i czytasz, co mają robić funkcje/metody.
2. Podpowiedzi znajdziesz w **komentarzach w kodzie** (np. `# Raise ValueError exception if b is 0.`)
   oraz w nazwach testów (np. `test_divide_by_zero_raises_value_error`).
3. Dopisujesz implementację w miejsce `pass`.
4. Uruchamiasz testy i sprawdzasz, czy są zielone.
5. Powtarzasz, aż dany moduł przechodzi w całości.

Kod **nie potrzebuje bibliotek zewnętrznych**. Wystarczy Python 3 i moduł
`unittest` ze standardowej biblioteki.

## Struktura repozytorium

Każdy temat ma **dwie równoległe wersje**. Tę samą logikę piszesz raz jako
funkcje, raz jako klasę:

| Katalog | Styl | Plików |
|---|---|---|
| `src/functions/` | funkcje (proceduralnie) | 15 |
| `src/objects/` | klasy (OOP) | 15 |
| `tests/unit/functions/` | testy wersji funkcyjnej | 15 |
| `tests/unit/objects/` | testy wersji obiektowej | 15 |

Tematy (po 1 module w każdym stylu):

`calculator`, `comparisons`, `conditionals`, `data_types`, `error_handling`,
`input_output`, `list_operations`, `lists_dicts_tuples`, `loops`,
`nested_statements`, `operators`, `parameters`, `string_operations`,
`variable_scope`, `variables`

Przykład funkcji i jej test:

```python
# src/functions/calculator.py
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# tests/unit/functions/test_calculator.py
def test_divide_by_zero_raises_value_error(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
```

## Jak uruchomić testy

Wszystkie komendy uruchamiaj **z głównego katalogu repozytorium**
(`Podstawy-Programowania-2026-2027/`), bo importy są ścieżkami względnymi
(`from src.functions.calculator import add`).

### Wszystkie testy naraz (134 testy)

```bash
python3 -m unittest discover -s tests -v
```

### Testy jednego stylu (katalogu)

```bash
python3 -m unittest discover -s tests/unit/functions -v   # 70 testów
python3 -m unittest discover -s tests/unit/objects   -v   # 64 testy
```

### Testy jednego modułu

```bash
python3 -m unittest tests.unit.functions.test_calculator -v
```

### Pojedyncza klasa / pojedynczy test

```bash
python3 -m unittest tests.unit.functions.test_calculator.TestCalculator -v
python3 -m unittest tests.unit.functions.test_calculator.TestCalculator.test_divide_numbers -v
```

Flaga `-v` (verbose) wypisuje nazwy testów. Bez niej zobaczysz tylko kropki.
Na końcu zawsze pojawi się podsumowanie:

```
Ran 7 tests in 0.000s

OK
```

## Jak uruchomić pojedynczy plik

Każdy plik z kodem możesz odpalić w trybie interaktywnym. Pokaże się wynik działania:

```bash
python3 -i src/functions/calculator.py
```

```console
$ python3 -i src/functions/calculator.py
>>> print(divide(10, 2))
5.0
>>> exit()
```

Można też użyć flagi `-c` zapisując kod w jednej linii:

```bash
python3 -c "from src.functions.calculator import divide; print(divide(10, 2))"
```

```console
$ python3 -c "from src.functions.calculator import divide; print(divide(10, 2))"
5.0
```

Analogicznie dla każdego z 15 modułów.

Testy też można odpalać pojedynczymi plikami:

```bash
python3 -m unittest tests/unit/functions/test_calculator.py -v
python3 -m unittest tests/unit/objects/test_calculator.py -v
```

## Tryb pracy krok po kroku

1. Wybierz moduł, np. `loops`.
2. Przeczytaj testy w `tests/unit/functions/test_loops.py`. Nazwy mówią,
   czego się spodziewać (`test_factorial_of_negative_number_raises_error`).
3. Zajrzyj do `src/functions/loops.py`. Komentarze podpowiadają logikę.
4. Zaimplementuj funkcje, uruchom testy tego modułu.
5. Gdy są zielone, przejdź do wersji obiektowej: `src/objects/loops.py`.
6. Na koniec puść całość: `python3 -m unittest discover -s tests -v`.

## CI

Każdy commit odpala testy automatycznie (GitHub Actions,
`.github/workflows/tests.yml`). Czerwone testy **nie blokują** commita.
W TDD to normalny etap pracy, a nie błąd.
