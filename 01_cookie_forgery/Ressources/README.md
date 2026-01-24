# Comment on obtient le flag?
> Sur la page d'accueil acceder aux outils de developpement web ("ctrl + maj + i" sur Mozilla)
> Onglet "storage"
> On trouve un cookie i_am_admin avec pour valeur "b326b5062b2f0e69046810717534cb09" 
> On decrypte la valeur sur https://md5decrypt.net : il s'agit de "false" en md5.
> Sur le meme site, on encrypte "true" em md5 et obtient "b326b5062b2f0e69046810717534cb09"
> On remplace la valeur md5 "false" de notre cookie par la valeur md5 "true"
> On actualise la page et obtient le flag dans une alerte

# Pourquoi c'est une faille?
C'est tellement gros que c'est difficile a prendre au serieux, mais faire la demarche ci-dessus pourrait en theorie donner un acces admin au site, et donc permettre de faire tout ce qu'on veut.

# Comment la resoudre/eviter?
Il faut toujours eviter de stocker des informations importantes dans des cookies, a commencer par l'acces admin EVIDEMMENT.
En plus md5 est vraiment pas secure donc il vaudrait mieux utiliser bcrypt.
Et enfin DE TOUTE FACON on fait normalement dependre les droits administrateurs de l'utilisateur lui-meme. C'est en se connectant en tant qu'admin qu'on en obtient les droits.