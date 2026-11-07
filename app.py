from random import randint, choice
from tkinter import *
import string
def generate_password():
    password_min=6
    password_max=12
    all_chars=string.ascii_letters + string.digits
    password = "".join(choice(all_chars)for x in range(randint(password_min,password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("generateur mot de passe ")
window.geometry("720x480")
window.configure(background="#4065A4")

#frame
frame=Frame(window,bg="#4065A4")
#creation d'image
width = 300
HEIGTH = 300
image = PhotoImage(file="agent-de-securite.png").zoom(35).subsample(32)

canvas = Canvas(frame,width=width,height=HEIGTH,bg="#4065A4",bd=0,highlightthickness=0)
canvas.create_image(width/2, HEIGTH/2, image=image)
canvas.grid(row=0,column=0)
frame.pack(expand=YES)
# CREE UNE BOITE
rigth_frame = Frame(frame,bg="#4065A4")
#UN TITRE
label_title= Label(frame , text="Mot de Passe ", font=("Helvetica", 25),bg="#4065A4",fg="white")
label_title.grid(row=0,column=0)

#chammps
password_entry= Entry(frame , font=("Helvetica", 25),bg="#4065A4",fg="white")
password_entry.grid(row=0,column=1)

#bouton
generate_password_button = Button(frame , text="Generer ", font=("Helvetica", 25),bg="#4065A4",fg="white",command=generate_password)
generate_password_button.grid(row=2,column=0)
menu_bar = Menu(window)



rigth_frame.grid(row=0,column=2,sticky=W)




#bar de menu
menu_bar = Menu(window)
#fichier
file_menu =Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=generate_password)
file_menu.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="fichier",menu=file_menu)

#confid
window.config(menu=menu_bar)
#AFFICHER
window.mainloop()
