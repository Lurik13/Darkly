Pour referencer un site web, il y a deux fichiers qui nous interessent : sitemap.xml et robots.txt.

Sitemap.xml est un protocole permettant à l'administrateur d'informer les moteurs de recherche des adresses d'un site web disponibles pour l'indexation automatique.

robots.txt est une ressource de format texte qui peut être placée à la racine d'un site web, et qui contient une liste des ressources du site qui ne sont pas censées être indexées par les robots d'indexation des moteurs de recherche.

Lorsque nous allons sur le chemin '/robots.txt', il y a un "Disallow: /whatever". Une fois sur '/whatever', nous avons acces au fichier 'htpasswd', dont le contenu est : 
root:437394baff5aa33daa618be47b75cb49

En effet, htpasswd permet de créer et de maintenir les fichiers textes où sont stockés les noms d'utilisateurs et mots de passe pour l'authentification de base des utilisateurs HTTP. 437394baff5aa33daa618be47b75cb49 correspond au mot de passe hache de l'utilisateur root. Apres decryption, nous obtenons "qwerty123@". Il suffit de se connecter avec root et qwerty123@ sur le chemin '/admin' pour obtenir le flag.

Pour eviter ce probleme, il suffit de modifier le fichier de configuration du serveur HTTP (nginx, apache) et bloquer tous les fichiers sensibles avec un "Require all denied", par exemple.