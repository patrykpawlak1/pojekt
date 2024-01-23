import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk


    
types = ["Ognisty", "Elektryczny", "Wodny", "Normalny", "Trawiasty", "Lodowy", "Walczący", "Latający",
         "Trujący", "Ziemny", "Psychiczny", "Robaczy", "Kamienny", "Stalowy", "Duch", "Smoczy"]

def wyswietl_pokemony(pokedex, text_widget):
    text_widget.delete(1.0, tk.END)  
    
    if not pokedex:
        text_widget.insert(tk.END, "Na co czekasz? Złap je wszystkie!\n")
        
    else:
        for pokemon in pokedex:
            text_widget.insert(tk.END, f"{pokemon[0]} - Typ: {', '.join(pokemon[1])}\n")
        

def wyswietl_pokemony_wg_typu(pokedex, text_widget ):
    text_widget.delete(1.0, tk.END)  
    
    wybor_typu = simpledialog.askinteger("Wyświetl Pokemony wg Typu", "Wybierz opcję:\n1. Szukaj według jednego typu\n2. Szukaj według dwóch typów\n3. Szukaj według dokładnie jednego typu")
    
    if wybor_typu not in [1, 2, 3]:
        text_widget.insert(tk.END, "Błąd: Niewłaściwy wybór. Wybierz 1, 2 lub 3.\n")
        return
        if wybor_typu == 1:
        wybrany_typ = simpledialog.askstring("Wyświetl pokemony wg typu", f"Wybierz typ (dostępne typy: {', '.join(types)}):")
        if wybrany_typ.capitalize() not in types:
            text_widget.insert(tk.END, f"{wybrany_typ} to nieprawidłowy typ. Wybierz spośród dostępnych.\n")
            return

        pokemony_wg_typu = [pokemon for pokemon in pokedex if wybrany_typ.capitalize() in pokemon[1]]
    elif wybor_typu == 2:
        typ_1 = simpledialog.askstring("Wyświetl pokemony wg typu", f"Wybierz pierwszy typ (dostępne typy: {', '.join(types)}):")
        if typ_1.capitalize() not in types:
            text_widget.insert(tk.END, f"{typ_1} to nieprawidłowy typ. Wybierz spośród dostępnych.\n")
            return

        typ_2 = simpledialog.askstring("Wyświetl pokemony wg typu", f"Wybierz drugi typ (dostępne typy: {', '.join(types)}):")
        if typ_2.capitalize() not in types:
            text_widget.insert(tk.END, f"{typ_2} to nieprawidłowy typ. Wybierz spośród dostępnych.\n")
            return

        pokemony_wg_typu = [pokemon for pokemon in pokedex if typ_1.capitalize() in pokemon[1] and typ_2.capitalize() in pokemon[1]]
    else:  # wybor_typu == 3
        wybrany_typ = simpledialog.askstring("Wyświetl pokemony wg typu", f"Wybierz typ (dostępne typy: {', '.join(types)}):")
        if wybrany_typ.capitalize() not in types:
            text_widget.insert(tk.END, f"{wybrany_typ} to nieprawidłowy typ. Wybierz spośród dostępnych.\n")
            return

        pokemony_wg_typu = [pokemon for pokemon in pokedex if wybrany_typ.capitalize() in pokemon[1] and len(pokemon[1]) == 1]

    if not pokemony_wg_typu:
        text_widget.insert(tk.END, f"Brak pokemonów według kryteriów.\n")
    else:
        for pokemon in pokemony_wg_typu:
            text_widget.insert(tk.END, f"{pokemon[0]} - Typ: {', '.join(pokemon[1])}\n")

def dodaj_pokemona(pokedex, text_widget):
    text_widget.delete(1.0, tk.END)  
    
    nazwa = simpledialog.askstring("Dodaj Pokemona", "Podaj nazwę nowego pokemona:")
    nazwa=nazwa.capitalize()
    
    if not nazwa:
        text_widget.insert(tk.END, "Błąd: Nie podano nazwy nowego pokemona.\n")
        return
    
    if any(pokemon[0] == nazwa for pokemon in pokedex):
        text_widget.insert(tk.END, f"{nazwa} już istnieje w Pokedexie. Nie można dodawać powtarzających się Pokémonów.\n")
        return

    liczba_typow = simpledialog.askinteger("Dodaj Pokemona", "Ile typów ma pokemon? (1 lub 2)")
    if liczba_typow not in [1, 2]:
        text_widget.insert(tk.END, "Błąd: Niewłaściwa liczba typów. Podaj 1 lub 2.\n")
        return

    typy = []
    for t in range(liczba_typow):
        wybrany_typ = simpledialog.askstring("Dodaj Pokemona", f"Wybierz typ dla {nazwa} (dostępne typy: {', '.join(types)}):")
        if wybrany_typ.capitalize() in types:
            typy.append(wybrany_typ.capitalize())
        else:
            text_widget.insert(tk.END, f"{wybrany_typ} to nieprawidłowy typ. Wybierz spośród dostępnych.\n")
            return
    
    nowy_pokemon = (nazwa, typy, None)  
    pokedex.append(nowy_pokemon)
    text_widget.insert(tk.END, f"{nazwa} został dodany do Pokedexu!\n")

def dodaj_grafike_pokemona(pokedex, text_widget):
    text_widget.delete(1.0, tk.END)  

    nazwa = simpledialog.askstring("Dodaj Grafikę Pokemona", "Podaj nazwę pokemona, dla którego chcesz dodać grafikę:")
    nazwa=nazwa.capitalize()
    if not nazwa:
        text_widget.insert(tk.END, "Błąd: Nie podano nazwy pokemona.\n")
        return

    pokemon = next((p for p in pokedex if p[0] == nazwa), None)

    if not pokemon:
        text_widget.insert(tk.END, f"{nazwa} nie istnieje w Pokedexie.\n")
        return

    ścieżka = filedialog.askopenfilename(title="Wybierz Grafikę Pokemona", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

    try:
        obraz = Image.open(ścieżka)
        obraz.thumbnail((300, 300))  
    except Exception as x:
        text_widget.insert(tk.END, f"Błąd: {str(x)}\n")
        return

    pokemon = list(pokemon)  
    pokemon[2] = obraz  
    pokedex[pokedex.index((pokemon[0], pokemon[1], None))] = tuple(pokemon)  
    text_widget.insert(tk.END, f"Grafika dla {nazwa} została dodana!\n")
    
def wyswietl_grafike_pokemona(pokedex, text_widget):
    text_widget.delete(1.0, tk.END)  

    nazwa_pokemona = simpledialog.askstring("Wyświetl Grafikę Pokemona", "Podaj nazwę pokemona, którego grafikę chcesz wyświetlić:")
    nazwa_pokemona=nazwa_pokemona.capitalize()
    
       
    if not nazwa_pokemona:
        text_widget.insert(tk.END, "Błąd: Nie podano nazwy pokemona.\n")
        return

    pokemon = next((p for p in pokedex if p[0] == nazwa_pokemona), None)

    if not pokemon or len(pokemon) < 3 or pokemon[2] is None:
        text_widget.insert(tk.END, f"{nazwa_pokemona} nie istnieje w Pokedexie lub nie ma przypisanej grafiki.\n")
        return

    obraz = pokemon[2]  
    obraz.show()
def Pokedex():
    pokedex = []
    root = tk.Tk()
    root.title("Pokedex")
    text_widget = tk.Text(root, height=10, width=40)
    text_widget.pack(pady=10)
    przyciski = {
        "Wyświetl pokemony": lambda: wyswietl_pokemony(pokedex, text_widget),
        "Dodaj pokemona": lambda: dodaj_pokemona(pokedex, text_widget),
        "Wyświetl pokemony wg typu": lambda: wyswietl_pokemony_wg_typu(pokedex, text_widget),
        "Dodaj grafikę": lambda: dodaj_grafike_pokemona(pokedex, text_widget),
        "Wyświetl grafikę": lambda: wyswietl_grafike_pokemona(pokedex, text_widget),
        "Zamknij pokedex": root.destroy
    }

    for nazwa, funkcja in przyciski.items():
        przycisk = tk.Button(root, command=funkcja ,text=nazwa)
        przycisk.pack(pady=5)
    root.mainloop()

Pokedex()
