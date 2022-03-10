# TP2 Deep QLearning

Vous trouverez dans ce dépôt :
* Les slides du CM2
* Le notebook et fichiers python à compléter pour ce TP

## 1. Récupération du projet sur GitHubClassroom


1. Les 2 étudiants du binôme (nom1 et nom2) doivent avoir un compte github. Si ce n’est pas le cas, créer un compte sur [github](https://github.com).
2. Un seul des 2 étudiants du binôme (nom1) clique sur le lien de l’assignment des TPs donné en cours.

3. Avec ce lien, l’étudiant nom1 accepte l’invitation et **crée une team** nommée `nom1-nom2`. Le nom du dépôt sera alors : `tp-sma-deeprl-nom1-nom2`. 
4. Le second étudiant nom2 du binôme doit alors:
* Le plus simple:  cliquer sur l’assignment. Il choisit alors de joindre la team existante : `nom1-nom2`.
* Soit l’étudiant nom1 ajoute `nom2` à la team `nom1-nom2`. L'étudiant `nom2`  recoit alors une invitation. L’étudiant `nom2`  accepte l’invitation : dans github, l’étudiant `nom2`  voit la team, et peut modifier le dépôt. L’étudiant `nom2`  ne voit le dépôt que lorsqu’il a fait une modification.

## 2. Installation

1. Activer l'environnement créé pour le TP1:

```
conda activate nnPyTorch
```
2. Installer [gym](https://gym.openai.com)

 -  __Windows __ et __Mac__: 

 ```
pip install gym
pip install pyglet
 ```
Note: faire `ènv.reset()` à chaque début/fin d'épisode.

```
Cela va générer des erreurs liées à MuJoCo mais les autres dépendances seront tout de même correctement installées.

 -  __Linux __: 

```
pip install gym
pip install Box2D
```


## 3. TP

N'oubliez pas d'activer votre environnement avant le lancement de votre TP !

```
conda activate nnPyTorch
```

Vous pouvez maintenant lancer le notebook ([Jupyter notebook](https://jupyter.org)) du TP2 en lancant la commande suivante :

```
cd tp-sma-deeprl-nom1-nom2
jupyter notebook
```
et compléter le TP2  `TP2.ipynb`.

