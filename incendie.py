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
#DEFINITION DES CONSTANTES
longueur = 500 #taille temporaire a changé ou non
hauteur= 500   #taille temporaire a changé ou non
cellule =25 #taille des cellules temporaires
cote = 20 # nombre de carré
#couleur des cases
couleur_eau = "blue"
couleur_foret ="green" 
couleur_feu= "red"
couleur_prairie="yellow"
couleur_tiede ="grey"
couleur_eteind="black"
nombre_colonne = hauteur // cote
nombre_ligne = longueur //cote



############################################
#définition des variables globales
tableau = None



############################################
#définition des fonctions
def carre():
    Ligne()
    Vertical()

def Ligne():
    l_u,l_d = 0, hauteur
    y = 0
    while y <= longueur:
        canvas.create_line(l_u, y, l_d, y ,fill= "black")
        y += cote
def Vertical():
    d_u,d_d =0, longueur
    x= 0
    while x <= hauteur:
        canvas.create_line(x, d_u, x, d_d,fill="black")
        x += cote

def coord_carre(x, y):
    return x // cote, y //cote



def change_carre(event):
    i, j = coord_carre(event.x, event.y)
    if tableau[i][j] == 1:
        x, y = i * cote, j * cote
        carre =canvas.create_rectangle(x,y, x + cote, y + cote,fill= couleur_eau)
        tableau[i][j] = 2
    elif tableau [i][j] ==2:
        x, y = i * cote, j * cote
        carre =canvas.create_rectangle(x,y, x + cote, y + cote,fill= couleur_foret)
        tableau[i][j]= 3
    elif tableau [i][j] ==3:
        x, y = i * cote, j * cote
        carre =canvas.create_rectangle(x,y, x + cote, y + cote,fill= couleur_prairie)
        tableau[i][j]= 4
    elif tableau [i][j] ==4:
        x, y = i * cote, j * cote
        carre =canvas.create_rectangle(x,y, x + cote, y + cote,fill= "white")
        tableau[i][j]= 1
    



def cree_carre():
    global tableau
    tableau=[]
    for i in range(nombre_colonne):
        tableau.append([1] * nombre_ligne)

def allumage_feu(event):
    i, j = coord_carre(event.x, event.y)
    if tableau[i][j] > 2:
        print("feu")
        x, y = i * cote, j * cote
        carre =canvas.create_rectangle(x,y, x + cote, y + cote,fill= couleur_feu)
        tableau[i][j] = 5

############################################
#programme principal 
racine= tk.Tk()

racine.title("simulation incendie")
#canvas
canvas= tk.Canvas(racine ,bg = "white", width = longueur, height=hauteur,bd= 2,) 
canvas.grid(row =0)
carre()
cree_carre()
canvas.bind("<Button-1>",change_carre)
canvas.bind("<Button-3>",allumage_feu)



racine.mainloop()
############################################