#########################################
#informations liées au groupe
# groupe Miashs Td1 groupe 5
# Gouyer Roxane
# Alioune Ndiaye
# Momar SAMBE
# Maxime Jouan
#
# https://github.com/uvsq22001707/projet_incendie
###########################################
#https://discord.gg/yuxCwtMP




###########################################
#import des librairies
import tkinter as tk



############################################
#définition des constantes
longueur = 500 #taille temporaire a changé ou non
hauteur= 500   #taille temporaire a changé ou non
cellule =25 #taille des cellules temporaires


############################################
#définition des variables globales
l_u = 0
l_d = 0
z= 0
d_u=0
d_d=0
y =0



############################################
#définition des fonctions
def carre():
    Ligne()
    Vertical()

def Ligne():
    l_u,l_d = 0, hauteur
    z =0
    while z <= longueur:
        canvas.create_line(l_u, z, l_d, z ,fill= "black")
        z += cellule
def Vertical():
    d_u,d_d =0, longueur
    y= 0
    while y <= hauteur:
        canvas.create_line(y, d_u, y, d_d,fill="black")
        y += cellule






############################################
#programme principal 
racine= tk.Tk()

racine.title("simulation incendie")
#canvas
canvas= tk.Canvas(racine ,bg = "white", width = longueur, height=hauteur,bd= 2) 
canvas.grid(row =0)
carre()


racine.mainloop()
############################################