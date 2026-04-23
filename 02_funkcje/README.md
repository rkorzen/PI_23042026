W tym module posluze sie jupyter notebook do prezentacji materialow i realizacji cwiczen

W wierszy polecen:

    pip install jupyter
    jupyter notebook


#

Jasne — oto praktyczna **ściąga poruszania się po Jupyter Notebook**.

## Podstawy

Jupyter ma dwa główne tryby:

**1. Command mode**
Służy do operowania na komórkach.
Wchodzisz przez `Esc`

**2. Edit mode**
Służy do pisania kodu lub tekstu w komórce.
Wchodzisz przez `Enter`

---

## Najważniejsze skróty

### Uruchamianie komórek

* `Shift + Enter` — uruchom komórkę i przejdź do następnej
* `Ctrl + Enter` — uruchom komórkę i zostań w niej
* `Alt + Enter` — uruchom komórkę i dodaj nową poniżej

### Przełączanie trybów

* `Esc` — command mode
* `Enter` — edit mode

---

## Dodawanie i usuwanie komórek

W **command mode**:

* `A` — dodaj komórkę **nad**
* `B` — dodaj komórkę **pod**
* `D`, `D` — usuń komórkę
* `X` — wytnij komórkę
* `C` — kopiuj komórkę
* `V` — wklej **pod**
* `Shift + V` — wklej **nad**

---

## Zmiana typu komórki

W **command mode**:

* `Y` — zmień na komórkę **Code**
* `M` — zmień na **Markdown**
* `R` — zmień na **Raw**

---

## Poruszanie się

W **command mode**:

* `↑` / `↓` — przechodzenie między komórkami
* `J` / `K` — też przechodzenie między komórkami
* `Home` — początek notebooka
* `End` — koniec notebooka

W **edit mode**:

* standardowo strzałkami po tekście/kodzie
* `Ctrl + ←` / `Ctrl + →` — skok po słowach

---

## Edycja i wygoda pracy

### W edit mode

* `Tab` — podpowiedzi / autouzupełnianie
* `Shift + Tab` — podgląd dokumentacji
* `Ctrl + Shift + -` — podziel komórkę w miejscu kursora

### W command mode

* `Z` — cofnij usunięcie komórki
* `L` — pokaż/ukryj numery linii
* `O` — pokaż/ukryj output
* `Shift + O` — przełącz przewijanie outputu

---

## Restart i czyszczenie

Z menu **Kernel**:

* **Interrupt** — przerwij wykonywanie
* **Restart** — zrestartuj kernel
* **Restart & Run All** — restart i uruchom wszystko od początku

To bardzo ważne, bo notebook **pamięta stan w pamięci**, więc czasem działa coś tylko dlatego, że było uruchomione wcześniej.

---

## Markdown w notebooku

W komórce typu **Markdown** możesz pisać np.:

```markdown
# Nagłówek 1
## Nagłówek 2

**pogrubienie**
*kursywa*

- punkt 1
- punkt 2
```

Kod w linii:

```markdown
`print("hej")`
```

Blok kodu:

````markdown
```python
print("hej")
```
````

---

## Bardzo przydatne komendy w kodzie

### Help

```python
len?
```

### Szczegółowa dokumentacja

```python
len??
```

### Lista metod obiektu

```python
my_list.
```

i potem `Tab`

---

## Typowy workflow

Najczęściej pracuje się tak:

1. `B` — nowa komórka pod spodem
2. `Enter` — wejście do edycji
3. wpisujesz kod
4. `Shift + Enter` — uruchamiasz
5. `M` — gdy chcesz zrobić opis Markdown
6. `A` / `B` — dokładanie kolejnych sekcji

---

## Minimum, które warto zapamiętać

Jeśli chcesz zapamiętać tylko kilka skrótów, to te:

* `Esc` — tryb komend
* `Enter` — tryb edycji
* `Shift + Enter` — uruchom
* `A` / `B` — dodaj komórkę
* `D D` — usuń komórkę
* `Y` — code
* `M` — markdown
* `Z` — cofnij usunięcie

---

## Uwaga praktyczna

Najczęstszy problem początkujących:
**komórki uruchamiane są w innej kolejności niż wyglądają w notebooku**.
Dlatego gdy coś „dziwnie działa”, często pomaga:

* **Kernel → Restart**
* potem **Run All**

---

Mogę Ci też zrobić **krótszą ściągę w formie jednej tabelki**, taką idealną do wydrukowania.
