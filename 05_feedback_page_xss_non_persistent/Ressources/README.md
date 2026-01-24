# Comment on obtient le flag?
> On va sur la page "feedback"
> On ecrit "script" en nom et message
> On obtient le flag (oui oui, sans vrai script)

# Pourquoi c'est une faille?
XSS veut dire "Cross-site scripting" et consiste a injecter du code malveillant dans une plateforme, qui est ensuite stocke dans le contenu dynamique du navigateur de l'utilisateur. Le navigateur execute donc les balises du site ET celles du code malveillant.
Ici, c'est pas stocke donc appele "non-persistent".
On peut faire beaucoup de choses avec ca, notamment recuperer des tokens ou des cookies qui, sur certains sites peuvent contenir des informations personnelles/importantes...

# Comment la resoudre/eviter?
Les inputs des users ne doivent pas etre publics quand c'est possible. Quand on a pas le choix il faut controler a fond les inputs avec des interdictions de caracteres speciaux, de sequences de caracteres particulieres, de balises etc. Il existe des bases de donnees/librairies pour ca il me semble.