# Comment on obtient le flag?
> On clique sur "BornToSec" en bas de page
> On regarde le code source de la page
> On voit en commentaire "You must cone from : "https://www.nsa.gov/"."
> En dessous on lit aussi "Let's use this browser : "ft_bornToSec". It will help you a lot.""
> Acceder aux outils de developpement web ("ctrl + maj + i" sur Mozilla)
> Onglet "Network"
> On choisit la derniere requete 
> Copy Value 
> Copy as cURL
> Terminal
> Coller et remplacer user-agent par "ft_bornToSec" et referer par "https://www.nsa.gov/" avec | grep 'flag' a la fin

# Pourquoi c'est une faille?
Faille vraiment abusee en soit.
Aucun site ne doit faire dependre des operations des headers car... bah cette faille.
La balise Referer sert a savoir d'ou vient un utilisateur, donc on peut peut etre faire semblant que beaucoup de traffic vient d'une meme source.

# Comment la resoudre/eviter?
Le back ne doit faire dependre aucune operation de headers de requetes, surtout pas des importantes.
