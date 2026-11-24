# Podstawy Programowania - podstawowe konstrukcje języka programowania Python

Ćwiczenia dotyczące podstawowych konstrukcji języka programowania Python z przedmiotu Podstawy Programowania.

## Jak utworzyć własne repozytorium z tego szablonu

Zanim rozpoczniesz rozwiązywanie zadań, musisz utworzyć własną kopię tego projektu na swoim koncie GitHub. Projekt ten jest przygotowany jako **szablon (template)**. Aby to zrobić, postępuj zgodnie z poniższymi krokami:

1. Upewnij się, że jesteś zalogowany na swoje konto GitHub.
2. Na stronie głównej tego repozytorium (nad listą plików, po prawej stronie) znajdź i kliknij zielony przycisk **"Use this template"**.
3. Z rozwijanego menu wybierz opcję **"Create a new repository"**.
4. W formularzu tworzenia nowego repozytorium:
   * **Owner:** Wybierz swoje konto studenta.
   * **Repository name:** Nazwij swoje repozytorium zgodnie z następującym szablonem `grupa-nralbumu-Nazwisko-Imie-PPPKP` (np. `INF-1-12-26-27Z-12345-Sikora-Mateusz-PPPKP`).
   * **Privacy:** Wybierz **Public** (publiczne).
5. Kliknij przycisk **"Create repository from template"** na dole strony.
6. GitHub wygeneruje dla Ciebie nowe repozytorium, zawierające wszystkie pliki z tego szablonu, ale z czystą historią commitów.
7. Otwórz terminal, sklonuj swoje **nowo utworzone** repozytorium na dysk (`git clone <link-do-twojego-repo>`) i przejdź do instrukcji poniżej.

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

Kod **nie potrzebuje bibliotek zewnętrznych**. Wystarczy Python 3.10 lub nowszy i moduł
`unittest` ze standardowej biblioteki.

## Struktura repozytorium

Każdy temat ma **dwie równoległe wersje**. Tę samą logikę piszesz raz jako
funkcje, raz jako klasę:

| Katalog | Styl |
|---|---|
| `src/functions/` | funkcje (proceduralnie) |
| `src/objects/` | klasy (OOP) |
| `tests/unit/functions/` | testy wersji funkcyjnej |
| `tests/unit/objects/` | testy wersji obiektowej |

Tematy (po jednym module w każdym stylu):

`calculator`, `comparisons`, `conditionals`, `data_structures`, `data_types`,
`error_handling`, `function_basics`, `input_output`, `list_operations`,
`lists_dicts_tuples`, `loops`, `modules_imports`, `nested_statements`, `operators`,
`parameters`, `string_operations`, `variable_scope`, `variables`

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

### Wszystkie testy naraz

```bash
python3 -m unittest discover -s tests -v
```

### Testy jednego stylu (katalogu)

```bash
python3 -m unittest discover -s tests/unit/functions -v
python3 -m unittest discover -s tests/unit/objects   -v
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

Analogicznie dla każdego z modułów.

Testy też można odpalać pojedynczymi plikami:

```bash
python3 -m unittest tests/unit/functions/test_calculator.py -v
python3 -m unittest tests/unit/objects/test_calculator.py -v
```

## Tryb pracy krok po kroku

1. Wybierz moduł (np. `loops`).
2. Przeczytaj testy moduł (np. w `tests/unit/functions/test_loops.py`). Nazwy mówią,
   czego się spodziewać (np. `test_factorial_of_negative_number_raises_error`).
3. Zajrzyj do wersji funkcyjnej (np. `src/functions/loops.py`). Komentarze podpowiadają logikę.
4. Zaimplementuj funkcje, uruchom testy tego modułu.
5. Gdy są zielone, zrzuć pracę do Gita i wyślij na GitHub
   (np. `git add -A && git commit -m "Zaimplementowano loops - wersja funkcyjna" && git push`).
   Rób tak po **każdej** zielonej implementacji. 
   Lepiej wiele małych commitów niż jeden duży.
6. Przejdź do wersji obiektowej (np. `src/objects/loops.py`).
   Po jej zazielenieniu znowu commit i push.
7. Powtarzaj analogicznie dla każdego z modułów.
8. Na koniec puść całość testów: `python3 -m unittest discover -s tests -v`.

## CI

Każdy commit odpala testy automatycznie (GitHub Actions,
`.github/workflows/tests.yml`). Czerwone testy **nie blokują** commita.
W TDD to normalny etap pracy, a nie błąd.
