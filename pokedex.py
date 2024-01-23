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

