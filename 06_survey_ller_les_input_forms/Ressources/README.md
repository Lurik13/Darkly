# Comment on obtient le flag?
> Sur la page survey on voit un formulaire avec des valeurs de 1 a 10
> On inspecte l'element
> On remplace la valeur de "2" par 100000 par exemple
> On selectionne le 2
> On obtient le flag

# Pourquoi c'est une faille?
On pourrait fausser les resultats de peu importe quoi, le truc pour lequel c'est utilise. De l'XP sur un ou voter pour les victoires de la musique jsais pas.

# Comment la resoudre/eviter?
En mettant une fonction verifiant que la valeur est bien de 1 a 10 en back. Peut etre devoir se connecter pour voter, un vote par IP.
Et peut etre une autre fonction en front pour assurer un affichage correct?
