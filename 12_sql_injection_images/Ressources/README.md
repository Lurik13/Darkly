Sur la page de recherche d’images, il est possible d’accéder aux métadonnées d’une image en fournissant son identifiant dans un champ input.
Pour tester une éventuelle injection SQL, nous entrons :
1 OR 1=1

Ce qui retourne la liste complète des images stockées en base. Cela confirme que l’input est directement intégré dans la requête SQL sans filtrage.
Afin de déterminer le nombre de colonnes attendues, nous testons plusieurs payloads :
1 OR 1=1 UNION SELECT NULL
1 OR 1=1 UNION SELECT NULL, NULL
La seconde fonctionne, indiquant que la requête d’origine sélectionne deux colonnes.

Nous exploitons ensuite information_schema.columns, qui permet d’énumérer les tables et colonnes d’une base relationnelle :
1 OR 1=1 UNION SELECT column_name, table_name FROM information_schema.columns

Après analyse, la table exploitable est list_images. Nous récupérons ses données avec :
1 OR 1=1 UNION SELECT id, title FROM list_images
Puis nous concaténons plusieurs champs pour extraire l’ensemble du contenu :
1 OR 1=1 UNION SELECT id, CONCAT(url, title, comment) FROM list_images
Cela révèle le message caché contenant un hash MD5 (1928e8083cf461a51303633093573c46), qui une fois décodé (albatroz) puis rehashé en SHA-256 (f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188), permet d’obtenir le flag.


Cette faille existe car l’input utilisateur est injecté directement dans la requête SQL.
Exemple:
$query = "SELECT id, title FROM list_images WHERE id = $input";


Pour éviter ce problème, il faudrait tiliser des requêtes préparées (PDO::prepare)
$q = $pdo->prepare("SELECT id, title FROM list_images WHERE id = :id");
$q->execute(['id' => $input]);
Avec ce système, l’input n’est jamais interprété comme du SQL, seulement comme une valeur. C'est le gros avantage des frameworks.