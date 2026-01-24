# Comment on obtient le flag?
> Accueil > Sign In > I forgot my password
> On arrive sur la page "recover"
> On inspecte le bouton submit et voit une balise input "hidden" "mail" avec pour valeur webmaster@borntosec.com.
> On remplace l'addresse mail
> Submit
> Et c'est gagne

# Pourquoi c'est une faille?
Deja cest bizarre car le formulaire ici ne demande pas d'adresse mail pour retrouver son mot de passe. Normalement cest le cas.
mais en theorie on pourrait utiliser cette methode pour recuperer des adresses mail et en faire ce qu'on veut, mail bombing ou demarcher les clients d'une plateforme par exemple.

# Comment la resoudre/eviter?
Dans le back et surtout pas dans des inputs comme ca. 
Une fonction qui recoit l'email saisi et l'envoi au back, qui lui opere l'envoi. Truc du genre