# Comment on obtient le flag?
> Sur la page d'accueil, clic droit sur le bouton facebook en bas de page
> "Inspecter"
> On remplage le lien "facebook" par "google" ou "youtube" ou "42" par exemple
> On obtient le flag

# Pourquoi c'est une faille?
On pourrait injecter un site simulant facebook et recuperer les identifiants des utilisateurs.
A la place d'obtenir le flag, l'utilisateur pourrait arriver sur une page ressemblant a facebook (avec un lien utilisant un alphabet similaire visuellement) et sans faire attention renseigner ses identifiants de connexion par exemple.
Cette faille utilise la reputation de plateformes reconnues comme Facebook etc en lesquelles les utilisateurs en confiance. Ils voient un logo Facebook et entre leurs informations de connexion sans reflexion apres avoir clique sur le logo.

# Comment la resoudre/eviter?
Stocker les liens de redirection dans une base de donnee en backend et empecher une modification?
Creer un array de liens autorises et ajouter une fonction verifiant les liens?


