Dans le footer, nous avons une liste de reseaux sociaux et, depuis la console, nous avons la possibilite de modifier l'url dans la balise href. Le backend ne verifie pas la valeur de l'adresse. 

On modifie l'adresse en mettant youtube ou google ou quoique soit, on clique sur le lien et on obtient le flag.

Pourquoi cest chiant : On peut mettre un faux facebook avec un caractere a en cyrillique par exemple et recuperer les identifiants de connexion d'un utilisateur pas mefiant.

Patch : Il faudrait stocker les adresses en backend et enlever la possibilite de les changer, ou bien faire une fonction verifiant les adresses par rapport a un array stocker en back end. 
