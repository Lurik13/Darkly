Sur le site web BornToSec, il y a trois onglets : Home, Survey et Members. Pour aller sur chacun d'entre eux, il faut le préciser dans le chemin à la suite de page= :
http://10.12.200.36/?page=survey

Toutefois, si on tente une route (page) inexistante, on tombe sur une alerte qui nous guide vers la voie du Path Traversal.
http://10.12.200.36/?page=mem
L'objectif, à travers cette attaque, est d'accéder à des fichiers et répertoires stockés en dehors du dossier racine du site web. Avec un peu de chance, on peut y trouver le code source de l'application, ou bien des fichiers de configuration.

Le fichier etc/passwd d'UNIX est un fichier couramment utilisé pour démontrer le traversement de répertoires, car il est souvent utilisé par les pirates pour tenter de cracker les mots de passe. Il suffit juste de remonter plusieurs dossiers parents pour trouver le réel emplacement de ce fichier et obtenir le flag.
http://10.12.200.36/?page=/../../../../../../../etc/passwd

Pour éviter ce problème, il suffit de ne pas stocker les fichiers de configuration sensibles à la racine du projet. Il est également préférable de limiter les permissions des fichiers. L'idéal pour BornToSec aurait été d'accéder aux onglets via le chemin '/survey' plutôt que '/?page=survey' car l'utilisation de query params pour changer d'onglet est infructueuse : '/survey' ne doit être géré que par le front !
