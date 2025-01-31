# GitHub User Activity Tracker

Ce projet permet de récupérer et d'analyser les activités publiques d'un utilisateur GitHub en utilisant l'API GitHub. Il génère un rapport détaillé des interactions de l'utilisateur avec les dépôts GitHub sous forme d'un fichier texte.

## Fonctionnalités

- Récupération des événements publics d'un utilisateur GitHub.
- Classification des événements par type d'activité.
- Agrégation des actions effectuées sur chaque dépôt.
- Génération d'un rapport récapitulatif sous format texte.

## Prérequis

- Python 3.x
- Bibliothèque requests

## Installation

- Clonez ce dépôt :

```
git clone https://github.com/votre-repo/github-activity-tracker.git
cd github-activity-tracker
```

- Installez les dépendances nécessaires :

```
pip install requests
```

## Utilisation

Exécutez le script Python :

```
python github.py
```

Saisissez le nom d'utilisateur GitHub lorsque demandé.

Un fichier texte sera généré dans le dossier tracking/ contenant un résumé des activités de l'utilisateur.

## Exemple de sortie

Si un utilisateur a effectué plusieurs pushs sur un dépôt nommé repo-example, le fichier généré contiendra une ligne comme :

L'utilisateur a poussé des commits 3 fois vers le repo repo-example.

Structure du projet

/github-activity-tracker
│── script.py           # Script principal
│── tracking/           # Dossier contenant les fichiers générés
│── README.md           # Documentation

## Améliorations futures

- Ajout d'une interface graphique.
- Support de plusieurs utilisateurs simultanément.
- Exportation des données en format JSON ou CSV.
