# Bienvenue aux travaux pratiques du cours INF1007 ! 🖥️

**Pour cette première semaine de laboratoire, vous aurez comme tâche de compléter votre premier travail pratique (TP) en suivant les instructions ci-dessous.**

Ce premier TP, que nous avons intitulé le TP0, ne requiert aucun travail à remettre et ne sera pas noté. L'objectif du TP0 est simplement de s'assurer que toutes les installations et configurations nécessaires sur votre ordinateur sont effectuées afin de bien démarrer la session. 

> [!IMPORTANT]
> Avant de commencer le TP0, assurez-vous d'avoir pris connaissance des informations contenues dans le document intitulé `introduction.md`. 

## ÉTAPE 1 du TP0 : Téléchargements

Comme première partie du TP0, vous devez installer les outils suivants sur votre ordinateur. Ces outils seront nécessaires pour réaliser les TP et les projets.

### ☑️ Installation de Python et d'Anaconda

Python est le langage de programmation que nous utiliserons tout au long de la session. Pour faciliter son utilisation, nous utiliserons également un environnement virtuel nommé `conda`.

1. Commencez par installer [Anaconda](https://www.anaconda.com/download/success).
2. Une fois installé, ouvrez l'application et cliquez sur l'onglet environnement.
3. Créez un environnement `inf1007` en utilisant la version de python `3.11`

> Note: L'utilisation d'environnements est courante en programmation. Ces derniers permettent d'avoir un meilleur contrôle sur la façon dont Python est exécuté, notamment en isolant les dépendances, les versions de bibliothèques (ou modules) et les configurations afin d'assurer une bonne exécution du code.

### ☑️ Installation de VS Code

Visual Studio Code est un environnement de développement intégré (IDE), c'est-à-dire un logiciel qui vous permettra d'écrire, organiser et exécuter votre code. Il en existe plusieurs autres, mais nous recommandons d'utiliser celui-ci pour le cours. 

1. Commencez par installer [VS Code](https://code.visualstudio.com/).
2. Ensuite, créez un dossier `INF1007` dans vos documents.
3. Ouvrez VS Code puis ouvrez votre dossier `INF1007` dans VS Code
4. Créez un fichier `test.py` depuis VS Code et ouvrez-le.
5. Copiez le code suivant dans votre fichier `test.py`

```python
print('Hello world !')
```
6. Activez votre environnement python `inf1007` créé précedemment:
    1. Appuyez simultanément sur:
        - windows: `ctrl + shift + p` 
        - mac: `command + shift + p`
    2. Sélectionnez `Python: Select Interpreter`
    3. Cliquez sur l'environnement `inf1007` créé précedemment.

    > [!Tip]
    > Note: Il est aussi possible de choisir votre environnement en cliquant en bas à droite de votre écran (à coté de la cloche) quand vous avez ouvert un fichier python.

7. Exécutez le script `test.py` en cliquant en haut à droite sur la flèche.
> Vous devriez voir apparaitre `Hello world !` dans la console en bas de votre fenètre !

> [!Tip]
> Note: N'oubliez pas de vérifier votre environnement avant d'executer du code ! Savoir utiliser le bon environnement est une notion importante qui vous assurera de ne pas perdre des points lors des TPs. 

### ☑️ Installation de Git

`Git` est un logiciel de versionnement très pratique qui vous permet de sauvegarder différentes versions d'un projet à mesure que vous le modifiez. 

- `Git` nous permet, par exemple, de récupérer une version antérieure d'un code. Cela enlève le risque de perdre votre travail, étant donné qu'il est possible de récupérer n'importe quelle version de votre travail que vous aurez répertorié avec `Git`. 

- De plus, `Git` facilite la collaboration en permettant à plusieurs personnes de travailler en même temps sur le même projet, chacun ayant une copie locale sur son ordinateur. 

Cliquez [ici pour installer Git](https://git-scm.com/).

## ÉTAPE 2 du TP0 : Création d'un compte GitHub 

Vous êtes présentement sur une page dans le site web de `GitHub`, un outil qui permet d'entreposer des répertoires `Git`. Avec `GitHub`, il est possible de créer des *répertoires* (ou *repositories*, en anglais), qui nous permettent de sauvegarder un ensemble de fichiers (comme ceux de ce TP0) pour faciliter le partage et la collaboration. 

En utilisant des commandes `Git`, il est possible de sauvegarder une version locale d'un répertoire GitHub sur votre ordinateur, y apporter des changements, puis mettre à jour la version disponible en ligne sur GitHub avec vos modifications. 

Pour chaque TP et projet du cours, un répertoire GitHub vous sera partagé avec les fichiers et les instructions nécessaires. Vous devrez alors faire une copie locale du répertoire sur votre ordinateur, pour ensuite l'ouvrir dans VS Code pour réaliser votre travail. 

Dans ce TP0, nous allons voir les commandes `Git` qui nous permettront de faire cette copie locale (que l'on appelle un `clone`), et ensuite publier vos changements sur GitHub. 

Vous pouvez cliquer [ici](https://github.com) pour créer votre compte GitHub. 

## ÉTAPE 3 du TP0 : Exercices de familiarisation avec les outils Git, GitHub et VS Code

Maintenant que vous avez installé tous les outils nécessaires sur votre ordinateur, vous pouvez commencer l'exercice du TP0 ! :tada:

Rendez-vous au fichier intitulé `exercices.md` pour les instructions. 

## Ressources additionelles (optionnel)

Voici quelques ressources additionnelles pour en apprendre davantage sur les outils présentés :

1. [Cours d'introduction sur Git et GitHub](https://emdupre.github.io/git-course/)
2. [Tutoriel Git sur W3Schools](https://www.w3schools.com/git/)
3. [Guide des erreurs courantes avec Git](https://dangitgit.com/)
4. [Stack Overflow - aide pour vos questions syntaxiques et/ou algorithmiques](https://stackoverflow.com/)









