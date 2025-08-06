# Exercices à réaliser pour le TP0

Ce document contient les instructions pour réaliser quelques exercices pour vous familiariser avec les outils que vous venez d'installer, tels que VS Code, Git et GitHub. 

## Exercice 1 : Faire une copie locale (`clone`) d'un répertoire GitHub

Pour utiliser un répertoire situé sur GitHub, il est possible de faire une copie locale du répertoire sur notre ordinateur. On appelle cette copie un `clone`. Une fois cette copie effectuée, cela nous permet d'effectuer des modifications aux fichiers (par exemple, ajouter du code). Une fois les modifications effectuées sur notre copie locale, il est ensuite possible de 'pousser' ces changements vers le répertoire situé sur GitHub. De cette façon, les autres gens qui ont accès au répertoire GitHub pourront voir la nouvelle version du répertoire avec vos changements. 

Comme premier exercice, vous allez créer un `clone` du répertoire du TP0 sur votre ordinateur. Les étapes à suivre sont les suivantes. 

1. Sur votre ordinateur, créer un dossier pour y ajouter le TP0. (Vous pouvez, par exemple, créer un dossier nommé "INF1007" dans lequel vous pourrez y placer tous les TP et les projets du cours). 
2. Ouvrir VS Code
3. Ouvrir un terminal dans VS Code (voir la capture d'écran suivante)

<img width="4042" height="1595" alt="Image" src="https://github.com/user-attachments/assets/0c0fe95d-77e2-4a50-82c4-274310956f62" /> 

4. En utilisant la commande `cd` ("change directory"), changer le chemin du terminal pour le chemin vers le dossier que vous venez de créer (par exemple, votre dossier "INF1007").



5. Sur la page web du répertoire du TP0 sur GitHub, appuyer sur le bouton suivant pour copier le lien du répertoire (vous pourrez ensuite faire CTRL+V pour le coller). 



5. Maintenant, utiliser la commande `git clone`, suivie du lien du répertoire que vous venez de copier. Appuyer sur la touche "Entrée" pour exécuter la commande. Si le `git clone` a bien fonctionné, vous devriez voir un message similaire à celui dans la capture d'écran ci-dessous. Sinon, n'hésitez pas à nous demander de l'aide :) 


Maintenant que vous avez fait le `git clone`, les fichiers du TP0 devraient maintenant apparaître dans le dossier que vous avez créé sur votre ordinateur. Vérifiez que c'est le cas en ouvrant le dossier dans VS Code, en suivant la procédure de la capture d'écran ci-dessous (vous pouvez aussi cliquer sur : `File` > `Open Folder`). 


Une fois le dossier ouvert dans VS Code, vous devriez pouvoir voir les fichiers du TP0 sur l'onglet de gauche. Cliquez sur le fichier python `TP0.py` pour l'ouvrir. 

## Exercice 2 : Calcul de l'aire d'un cercle

Maintenant que vous avez ouvert le fichier `TP0.py`, nous allons écrire quelques lignes de code à l'intérieur, pour se pratiquer à exécuter du code dans VS Code. 

Comme exercice, on vous propose de calculer l'aire d'un cercle à partir d'un rayon entré par l'utilisateur. 

Vous pouvez suivre les étapes suivantes pour vous guider : 

1. La fonction `input()` est une fonction intégrée dans Python qui permet de demander à l'utilisateur d'entrer une valeur dans le terminal. En utilisant la fonction `input()`, ajouter une ligne de code qui, lorsque exécutée, permettra de demander à l'utilisateur d'entrer la valeur du rayon dans le terminal. Vous pouvez suivre [cet exemple](https://www.w3schools.com/python/ref_func_input.asp) pour vous aider.

2. Ensuite, ajouter une ligne de code qui permettra d'utiliser la valeur entrée par l'utilisateur pour effectuer le calcul d'un cercle.

3. Finalement, en utilisant la fonction `print()` intégrée dans Python, ajouter une autre ligne de code pour afficher l'aire du cercle dans le terminal. Vous pouvez suivre [cet exemple](https://www.w3schools.com/python/ref_func_print.asp) pour vous aider à utiliser la fonction `print()`

Votre résultat final devrait ressembler à ceci : 



## Exercice 3 : Mettre à jour le répertoire sur GitHub avec vos changements  

Maintenant que vous avez effectué des modifications au fichier TP0.py, il est maintenant temps de mettre à jour le répertoire sur GitHub avec votre code qui permet d'ajouter l'aire d'un cercle. 

Pour ce faire, nous allons utiliser les commnades `Git` suivantes. Avant de poursuivre, assurez-vous d'avoir sauvegardé vos changements (par exemple, avec `File` > `Save`, ou bien `CTRL+S`). 

1. Nous allons d'abord utiliser la commande `git status` pour s'assurer que git reconnaît bien qu'il a eu des changements au répertoire depuis le `clone`. Pour ce faire, entrez la commande suivante dans votre terminal de VS Code :



Ici, on voit que `Git` reconnaît qu'il y eu des changements dans le fichier `TP0.py` : 

2. Maintenant, nous allons utiliser la commande `git add` pour ajouter le fichier TP0.py. Cette commande indique à `Git` que vous souhaitez inclure les modifications d'un certain fichier lorsque vous utiliserez la prochaine commande (c'est-à-dire, `git commit`).

Note : si vous souhaitez ajouter tous les fichiers de votre répertoire, vous pouvez aussi faire `git add .`, et le `.` va ajouter tout le contenu du répertoire. 

3. Il est maintenant temps d'utiliser la commande `git commit`, qui permet de créer une "version" de notre travail qui sera répertoriée par `Git`. En d'autres mots, à chaque fois qu'on fait un `git commit`, le contenu des fichiers ajoutés précedemment avec `git add` sera sauvegardé dans l'historique de notre projet, et on pourra accéder à toutes ces versions en naviguant les anciens `commits`. Pour effectuer un `commit`, on utilise la commande `git commit` suivi de `-m`, pour ensuite ajouter un message personnalisé. Généralement, on ajoute un message descriptif sur les modifications qu'on vient d'apporter (par exemple "ajout de l'aire d'un cercle").

4. 





