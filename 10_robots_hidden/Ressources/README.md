Lorsque nous consultons le fichier /robots.txt, on remarque la directive : "Disallow: /.hidden"

Cela indique aux moteurs de recherche de ne pas indexer ce chemin, mais n’empêche pas son accès direct.

En accédant à /.hidden, on découvre une arborescence de répertoires listés publiquement.
Chaque dossier contient d’autres dossiers jusqu’à un fichier nommé README.

L’objectif est de parcourir récursivement tous les chemins jusqu’à trouver un README dont le contenu correspond au flag.
Le script automatise cette recherche en explorant chaque répertoire et en analysant le contenu des fichiers README jusqu’à trouver le bon.

Pour éviter ce problème, il faut :
 - ne pas utiliser robots.txt comme protection
 - désactiver le listing de répertoires
 - bloquer l’accès aux chemins sensibles via la configuration du serveur (ex. Require all denied sur Apache ou autoindex off sur Nginx)