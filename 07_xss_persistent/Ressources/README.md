# Comment on obtient le flag?
> On clique le logo de la NSA sur la homepage
> On voit que l'image est chargee par un viewer avec src=nsa , donc on peut remplacer par notre propre data-URI si on le veut
> On encode "<script>alert(42)</script>" en base 64
> on remplace "nsa" direct dans le lien du navigateur par "data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4="

# Pourquoi c'est une faille?
Comme pour l'autre faille xss, mais cette fois cest persistent. Donc on peut encore une fois ajouter un script a la page qui s'execute quand un utilisateur se connecte, et rediriger ses cookies vers un autre site par exemple. Dans ces cookies il peut y avoir des infos personnelles, sensibles, et ca peut meme etre utilise pour voler des informations bancaires (cartes de credit).

# Comment la resoudre/eviter?
Les images doivent plutot est dans une base de donnee, comme toutes les ressources.
Pour tester il y a des scans de securite comme Bright qui vont identifie les  failles XSS en tout genre (DOM, Reflected, Stored/Persistent etc)