# Keylogger designed in python
# English docs
Tested in Windows 10/11.
After starting, the keylogger copies the keylogger executable file (if it does not find in the startup programs folder) to the folder C:\Users\<username>\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup user. 
The keylogger saves pressed keys to a text file located in the C:\Users\<username>\AppData\Local\Temp folder. Every 10 seconds the log file is sent to the mega disk.
Keylogger should be converted to executable using py-to-exe.

# Dokumentacja
**Wykaz i opis części składowych –** opracowanych lub adaptowanych

Keylogger **napisany w języku** Python

Wykorzystane procedury/funkcje keylogger python:

1. copy_to_strartup(soruce_file)

argumenty wejściowe:

- soruce_file – string, ścieżka do pliku keyloggera

wartość zwracana:

- brak

Działanie

Kopiowanie pliku exe keyloggera do katalogu Startup aktualnego użytkownika (jeśli
nie jest dodany)

2. Find_File()

argumenty wejściowe:

- brak

wartość zwracana:

- bezwzględna ścieżka do pliku keylogger

Działanie

Szukanie pliku keyloggera w systemie plików oraz zwracanie ścieżki do pliku
keyloggera

3. upload_to_mega(file_path)

argumenty wejściowe:

- file_path – string, ścieżka do pliku który zostanie wysłany na dysk mega (logi)

wartość zwracana:

- brak

Działanie

Logowanie do dysku mega i wysyłanie wskazanego pliku na dysk

4. add_to_startup()

argumenty wejściowe:

- brak


wartość zwracana:

- brak

Działanie

Znajdowanie ścieżki do pliku keyloggera i wywoływanie funkcji copy_to_startup

5. get_active_window_title()

argumenty wejściowe:

- brak

wartość zwracana:

- ciąg znaków wskazujący aktywne okno

Działanie

Odczytywanie i zwracanie nazwy aktywnego okna

6. start_keylogger()

argumenty wejściowe:

- brak

wartość zwracana:

- brak

Działanie

Rozpoczęcie przechwytywania wpisywanych znaków

7. periodic_upload(file_path, interval)

argumenty wejściowe:

- file_path – string, ścieżka do pliku który zostanie wysłany na dysk mega (logi)
- interval – czas w sekundach po których plik zostanie wysłany na dysk mega

wartość zwracana:

- brak

Działanie

Wysyłanie co określony czas pliku na dysk mega

8. on_press(key)

argumenty wejściowe:

- key – typ wyzwalacza wywołujący procedurę on_press


wartość zwracana:

- brak

Działanie

Zapisywanie do pliku tekstowego ciągu wskazującego: wciśnięty klawisz i aktywne
okno. Znaki wpisywane w jednym oknie są zapisywane w pojedynczym wierszu pliku

**Skąd pozyskano kod python** – ChatGPT 3.

**Krótki opis działania**

Po uruchomieniu keylogger kopiuje plik wykonywalny keylogger’a (jeśli nie znajduje
się w folderze programów uruchomieniowych) do folderu
C:\Users\<username>\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
użytkownika. Keylogger zapisuje wciśnięte klawisze do pliku tekstowego (plik z
logami) znajdującego się w folderze C:\Users\<username>\AppData\Local\Temp. Co
10 sekund plik z logami jest wysyłany na dysk mega.

**Instrukcja instalacji/użytkownika**

Scenariusze

```
i. Instalacji na komputerze ofiary.
```
1.Agent stosując biały wywiad zbiera informacje na temat ofiary

2.Bazując na informacjach zebranych w poprzednim punkcie, Agent tworzy mail spear
phisingowy (np. wykorzystując social engeneering toolkit). W załączniku dodaje plik
wykonywalny (tworzony podczas :punkt ii. podpunkt 6 ) i wysyła go do ofiary.

```
2.1 Jeśli przesyłanie pliku wykonywalnego jest blokowane, agent przygotowuje
inną formę dostarczenia pliku wykonywalnego (np. poprzez użycie narzędzi do
kompresji i archiwizacji/udostępnienie pliku wykonywalnego w sieci i wysłanie
adresu do pliku w mail’u).
```
3.Ofiara otwiera mail, pobiera załącznik. Załącznik to plik wykonywalny (szczegóły
punkt ii.), który po uruchomieniu wykonuje czynności zgodne z treścią mail’a spear
phisingowego (np. wyświetla obraz/otwiera aplikację/pobiera aktualizację), a także
pobiera i uruchamia keylogger (w tle).

```
ii. Przygotowania mechanizmów dostarczania informacji do napastnika.
```
1. Napastnik otwiera Tor Browser, tworzy konto pocztowe (np. domena interia.pl)
2. Napastnik tworzy konto na dysku mega z użyciem konta pocztowego
    utworzonego w poprzednim punkcie
3. Napastnik przekazuje agentowi poświadczenie do konta dysku mega
    (komunikacja wyłącznie przez Tor Browser), tak aby agent zmodyfikował
    poświadczenia do zalogowania do dysku mega w skrypcie python (keylogger)
4. Agent generuje plik wykonywalny ze skryptu python (keylogger)


5. Agent udostępnia plik wykonywalny wygenerowany w poprzednim punkcie w
    sieci, aby można go było pobrać za pomocą komendy curl/Invoke-WebRequest
    z powershell (np. udostępnia plik w file.io) oraz zapisuje adres pliku
6. Agent tworzy skrypt powershell, który wykonuje czynności zgodne z treścią
    mail’a spear phisingowego (wytworzonego w punkcie i. podpunkt 2). Skrypt
    powershell również pobiera (korzysta z adresu pliku z podpunktu 5) i
    uruchamia keylogger.
7. Agent generuje plik wykonywalny (wysłany w załączniku maila w punkcie i.
    podpunkt 2) ze skryptu powershell
iii. **Obsługi odbierania informacji przez** napastnika.
1. Napastnik otwiera Tor Browser
2. Napastnik loguję się na dysk mega
3. Napastnik przegląda pliki, które znajdują się na dysku (logi z wciśniętych
    klawiszy)
