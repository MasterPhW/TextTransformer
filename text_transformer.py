# Copyright (c) 2023 MasterPhW
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Benötigte Bibliotheken Importieren 
import tkinter as tk
import string
import re
import pyperclip  # Zwischenablage Bibliothek 

# Funktionen zum Umwandeln des Textes
def to_upper():
    text = apply_checkbox_actions(entry.get('1.0', tk.END)) # Anwenden von Checkbox-Aktionen vor der Umwandlung
    result.delete(1.0, tk.END) # Löschen des bisherigen Inhalts des Ausgabefelds
    result.insert(tk.END, text.upper()) # Umwandeln des Textes vollständig in Großbuchstaben: AAAA BBB CCCCC DDD

def to_lower():
    text = apply_checkbox_actions(entry.get('1.0', tk.END))
    result.delete(1.0, tk.END)
    result.insert(tk.END, text.lower()) # Umwandeln des Textes vollständig in Kleinbuchstaben: aaaa bbb ccccc ddd

def capitalize():
    text = apply_checkbox_actions(entry.get('1.0', tk.END))
    result.delete(1.0, tk.END)
    result.insert(tk.END, text.capitalize()) # Nur den allerersten Buchstaben groß schreiben: Aaaa bbb ccccc ddd

def title():
    text = apply_checkbox_actions(entry.get('1.0', tk.END))
    result.delete(1.0, tk.END)
    result.insert(tk.END, text.title()) # Nur den ersten Buchstaben jedes Wortes groß schreiben: Aaaa Bbb Ccccc Ddd

def reverse_case():
    text = apply_checkbox_actions(entry.get('1.0', tk.END))
    result.delete(1.0, tk.END)
    result.insert(tk.END, text.swapcase()) # Umkehren der Groß-/Kleinschreibung: aus Aaaa Bbb Ccccc Ddd wird aAAA bBB cCCCC dDD

def alternating_case():
    text = apply_checkbox_actions(entry.get('1.0', tk.END))
    result.delete(1.0, tk.END)
    result.insert(tk.END, ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])) # Wechselnde Groß-/Kleinschreibung: AaAa bBb cCcCc dDd

# Funktion zum Kopieren des Inhalts des Ausgabefelds in die Zwischenablage
def copy_to_clipboard():
    pyperclip.copy(result.get('1.0', tk.END))

# Funktion zum Einfügen des Inhalts der Zwischenablage in das Eingabefeld
def paste_from_clipboard():
    entry.delete('1.0', tk.END)
    entry.insert(tk.END, pyperclip.paste())

# Funktion zum Anwenden von Checkbox-Aktionen
def apply_checkbox_actions(text):
    if all_var.get():  # Wenn die Checkbox "Alle Anpassungen durchführen" aktiviert ist, werden alle Checkboxen aktiviert
        text = text.replace('_', ' ').replace('-', ' ').replace('\n', ' ')
        text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
        text = text.replace('ß', 'ss').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE')
        text = re.sub(r'[<>:"/\\|?*]', '', text)
        text = ' '.join(text.split())
    else:
        if var1.get(): # Wenn die Checkbox "_ durch Leerzeichen ersetzen" aktiviert ist
            text = text.replace('_', ' ') # Ersetzen von "_" durch Leerzeichen
        if var2.get(): # Wenn die Checkbox "- durch Leerzeichen ersetzen" aktiviert ist
            text = text.replace('-', ' ') # Ersetzen von "-" durch Leerzeichen
        if var3.get(): # Wenn die Checkbox "Zeilenumbrüche entfernen" aktiviert ist
            text = text.replace('\n', ' ') # Entfernen von Zeilenumbrüchen
        if var4.get(): # Wenn die Checkbox "Satzzeichen entfernen" aktiviert ist
            punctuation_without_dash = string.punctuation.replace('-', '') # Erstellen einer Zeichenkette für Satzzeichen ohne "-"
            text = text.translate(str.maketrans('', '', punctuation_without_dash)) # Entfernen von Satzzeichen (ohne "-")
        if var5.get(): # Wenn die Checkbox "ß durch ss ersetzen" aktiviert ist
            text = text.replace('ß', 'ss') # Ersetzen von "ß" durch "ss"
        if var6.get(): # Wenn die Checkbox "Nicht darstellbare Zeichen entfernen" aktiviert ist
            text = re.sub(r'[<>:"/\\|?*]', '', text) # Entfernen von Zeichen, die im Windows-Explorer nicht darstellbar sind
        if var7.get(): # Wenn die Checkbox "Deutsche Umlaute (ÄÖÜ) durch Standardzeichen (AE/OE/UE) ersetzen" aktiviert ist
            text = text.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE') # Ersetzen von Umlauten durch Standardzeichen
        if var8.get(): # Wenn die Checkbox "mehrfache Leerzeichen entfernen" aktiviert ist
            text = ' '.join(text.split()) # Entfernen von mehrfachen Leerzeichen
    return text

# Funktion zum Aktivieren aller Checkboxen
def activate_all():
    if all_var.get():
        var1.set(1)
        var2.set(1)
        var3.set(1)
        var4.set(1)
        var5.set(1)
        var6.set(1)
        var7.set(1)
        var8.set(1)
    else:
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("TextTransformer") # Setzen des Titels des Fensters

# Erstellen der Eingabe- und Ausgabefelder
tk.Label(root, text="Text eingeben, der bearbeitet werden soll:", font='Helvetica 10 bold').pack(pady=(10,2))
entry = tk.Text(root, width=50, height=10, wrap=tk.WORD)
entry.pack()
tk.Button(root, text="Text aus Zwischenablage einfügen", command=paste_from_clipboard).pack(pady=2)

# Erstellen eines Frames für die Checkboxen
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Anpassungen:", font='Helvetica 10 bold').grid(row=0, column=0, columnspan=2, sticky="w")

# Erstellen der Checkboxen im Frame
all_var = tk.IntVar()
all_var.trace("w", lambda *args: activate_all())  # Wenn der Zustand von all_var geändert wird, wird die Funktion activate_all aufgerufen
check_all = tk.Checkbutton(frame, text="Alle Anpassungen durchlaufen lassen", variable=all_var)
check_all.grid(row=1, column=0, columnspan=2, sticky="w")

var1 = tk.IntVar()
check1 = tk.Checkbutton(frame, text="_ zu Leerzeichen", variable=var1)
check1.grid(row=2, column=0, sticky="w")

var2 = tk.IntVar()
check2 = tk.Checkbutton(frame, text="- zu Leerzeichen", variable=var2)
check2.grid(row=2, column=1, sticky="w")

var3 = tk.IntVar()
check3 = tk.Checkbutton(frame, text="Zeilenumbrüche entfernen", variable=var3)
check3.grid(row=3, column=0, sticky="w")

var4 = tk.IntVar()
check4 = tk.Checkbutton(frame, text="Satzzeichen entfernen", variable=var4)
check4.grid(row=3, column=1, sticky="w")

var5 = tk.IntVar()
check5 = tk.Checkbutton(frame, text="ß zu ss", variable=var5)
check5.grid(row=4, column=0, sticky="w")

var6 = tk.IntVar()
check6 = tk.Checkbutton(frame, text="Nicht darstellbare Zeichen entfernen", variable=var6)
check6.grid(row=4, column=1, sticky="w")

var7 = tk.IntVar()
check7 = tk.Checkbutton(frame, text="Umlaute zu AE/OE/UE", variable=var7)
check7.grid(row=5, column=0, sticky="w")

var8 = tk.IntVar()
check8 = tk.Checkbutton(frame, text="Mehrfache Leerzeichen entfernen", variable=var8)
check8.grid(row=5, column=1, sticky="w")

# Erstellen der Schaltflächen
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_title = tk.Button(button_frame, text="Ersten Buchstaben Jedes Wortes Immer Groß", command=title, width=40)
button_title.grid(row=0, column=0, padx=5, pady=5)

button_upper = tk.Button(button_frame, text="ALLES GROß SCHREIBEN", command=to_upper, width=40)
button_upper.grid(row=0, column=1, padx=5, pady=5)

button_lower = tk.Button(button_frame, text="alles klein schreiben", command=to_lower, width=40)
button_lower.grid(row=1, column=0, padx=5, pady=5)

button_capitalize = tk.Button(button_frame, text="Nur ersten buchstaben groß", command=capitalize, width=40)
button_capitalize.grid(row=1, column=1, padx=5, pady=5)

button_reverse = tk.Button(button_frame, text="gROß-/kLEINSCHREIBUNG UMKEHREN", command=reverse_case, width=40)
button_reverse.grid(row=2, column=0, padx=5, pady=5)

button_alternating = tk.Button(button_frame, text="wEcHsElNdE GrOß- uNd KlEiNsChReIbUnG", command=alternating_case, width=40)
button_alternating.grid(row=2, column=1, padx=5, pady=5)

# Erstellen des Ausgabefelds
tk.Label(root, text="geänderter Text:", font='Helvetica 10 bold').pack(pady=(10,2))
result = tk.Text(root, width=50, height=10, wrap=tk.WORD)
result.pack()
tk.Button(root, text="Text in Zwischenablage kopieren", command=copy_to_clipboard).pack(pady=2)

# Starten der Hauptschleife von Tkinter
root.mainloop()
