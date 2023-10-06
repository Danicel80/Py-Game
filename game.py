# Game 1.2
# importam 2 librarii (sau module) tkinter este pentru a face modul grafic
import random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# test sa vedem ce zicee git
# pozitionez fereastra pe mijlocul ecranului, in functie de ecran


def center_pos(win_width, win_height):
    s_width = root.winfo_screenwidth()
    s_height = root.winfo_screenheight()
    win_pos_x = int(s_width / 2 - win_width / 2)
    win_pos_y = int(s_height / 2 - win_height / 2)
    if win_height > s_height:
        win_height = s_height - 160
    return f"{win_width}x{win_height}+{win_pos_x}+{win_pos_y}"


# aceasta functie primeste nr. introdus de user, verifica si afisaza un rezultat
def check_nr(nr):
    global i, gen_nr
    combo_dif.config(state='disabled')
    msg = ""
    if nr.isnumeric():
        nr = int(nr)
        if nr < gen_nr:
            msg = "Ati introdus un numar mai mic"
            i += 1
        elif nr > gen_nr:
            msg = "Ati introdus un numar mai mare"
            i += 1
        else:
            msg = f"Ati ghicit din {i} incercari, numarul era {gen_nr}"
            btn_enter.config(state='disabled')
            # buton de reset, apare doar la final
            btn_reset.grid()
    else:
        msg = "trebuie sa introduceti un numar"
    e_nr.delete(0, END)
    # afisam rezultatul intr-o alta fereastra
    messagebox.showinfo(title="Game info", message=msg)

# o functie care genereaza numarul random
# in versiunea urmatoare functia ar putea primi o valoare pentru max randint
# astfel putem modifica dificultatea jocului
def gen_rand():
    global gen_nr, max_gen_nr
    gen_nr = random.randint(0, max_gen_nr)

def combo_selected(event):
    global max_gen_nr
    max_gen_nr = int(combo_dif.get().split(" ")[1])
    gen_rand()
    l_entry.config(text=f"Introduceti un numar intre 0 si {max_gen_nr}")

# la final putem reseta in cazul in care vrem sa mai incercam odata
def reset():
    global i, max_gen_nr
    # reactivam butonul "enter"
    btn_enter.config(state='active')
    # scoatem butonul "reset"
    btn_reset.grid_remove()
    i = 0
    max_gen_nr = 50
    # resetez dificultatea
    combo_dif.set("max 50")
    combo_dif.config(state='active')
    l_entry.config(text=f"Introduceti un numar intre 0 si {max_gen_nr}")
    # apelam gen_rand din nou pentru alt numar
    gen_rand()


i = 0
gen_nr = -1
max_gen_nr = 50
# apelam gen_rand
gen_rand()
# mai jos avem partea care genereaza fereastra si continutul
root = Tk()
root.title('Game')
root.geometry(center_pos(250, 300))
root.resizable(False, False)

description = "Bine ati venit.\n Jocul este simplu, sistemul va alege un numar random iar dumneavoastra trebuie sa-l ghiciti"

l_description = Label(root, text=description, wraplength=240, justify="center")
l_description.grid(column=0, row=0, sticky=tkinter.EW, padx=5, pady=5)
l_dif = Label(root, text="Selectati dificultatea")
l_dif.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
combo_dif = ttk.Combobox(root, values=["max 50", "max 100", "max 200"])
combo_dif.grid(column=0, row=3, sticky=tkinter.W, padx=5, pady=1)
combo_dif.bind("<<ComboboxSelected>>", combo_selected)
l_entry = Label(root, text=f"Introduceti un numar intre 0 si {max_gen_nr}")
l_entry.grid(column=0, row=4, sticky=tkinter.W, padx=5, pady=5)
e_nr = Entry(root)
e_nr.grid(column=0, row=5, sticky=tkinter.EW, padx=40, pady=1)
btn_enter = Button(root, text="Enter", command=lambda: check_nr(e_nr.get()))
btn_enter.grid(column=0, row=6, padx=20, pady=10)
btn_reset = Button(root, text="Reset", command=lambda: reset())
btn_reset.grid(column=0, row=7, padx=20, pady=5)
btn_reset.grid_remove()

# o bucla, probabil un while care ruleaza pana inchideti fereastra
root.mainloop()