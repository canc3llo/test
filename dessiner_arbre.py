import turtle
import random

def dessiner_arbre(longueur : float , angle_min : float , angle_max : float , nombre_sous_arbres_min : int ,
                   nombre_sous_arbres_max : int , facteur_min : float , facteur_max : float , longueur_min : float ):
   
    if longueur <= longueur_min:
        return
    #on rajoute qqchose
    
    sous_arbres_tot = random.randint(nombre_sous_arbres_min, nombre_sous_arbres_max)
    angle_tot = angle_max - angle_min
    angle_add = angle_tot / (sous_arbres_tot - 1)
    
    if turtle.position() == (0.00, 0.00):
        turtle.setheading(90)
        turtle.forward(longueur)

    angle = angle_max
    i = 0
    while(i < sous_arbres_tot):
        #sauvegarde
        turtle_pos = turtle.position()
        turtle_ang = turtle.heading()
        
        #appliquer angle
        turtle.setheading(angle + turtle_ang)
        
        #avance nvl longueur
        r = random.uniform(facteur_min, facteur_max)
        new_long = r * longueur
        turtle.forward(new_long)
        
        #recursive
        dessiner_arbre(new_long, angle_min, angle_max, nombre_sous_arbres_min, nombre_sous_arbres_max, facteur_min, facteur_max, longueur_min)
        
        #revenir
        turtle.goto(turtle_pos)
        turtle.setheading(turtle_ang)
        
        #nvl angle
        angle -= angle_add
        
        i += 1
        
    turtle.backward(longueur)        


turtle.screensize(1000, 1000)
turtle.setheading(90)
dessiner_arbre(120, -10, 10, 2, 2, 0.4, 0.9, 5)
turtle.done()
    
