# Convertisseur HEIC/WebP

Un convertisseur simple qui permet de transformer vos images HEIC et WebP en JPEG/PNG en les glissant simplement sur l'icône du programme. Les images avec transparence (canal alpha) sont automatiquement converties en PNG pour préserver la transparence.

## Installation

### Utilisation de l'exécutable (recommandé)
1. Téléchargez le fichier exécutable `HeicWebpConverter.exe` depuis le dossier `dist`
2. Aucune installation supplémentaire n'est nécessaire

### Utilisation du script Python
1. Assurez-vous d'avoir Python installé sur votre système
2. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

### Avec l'exécutable
1. Glissez simplement vos images HEIC ou WebP sur l'icône de `HeicWebpConverter.exe`
2. Une fenêtre de dialogue s'affichera pour vous informer du résultat de la conversion


## Fonctionnalités

- Conversion des images HEIC et WebP
- Préservation automatique des couches alpha (transparence) en convertissant vers PNG
- Conversion en JPEG pour les images sans transparence
- Suppression des données EXIF pour plus de confidentialité
- Interface utilisateur simple avec glisser-déposer
- Aucun fichier de log créé

## Notes

- Les images originales ne sont pas modifiées
- Les nouvelles images auront le même nom que les originales mais avec l'extension .jpg ou .png
- Toutes les données EXIF sont supprimées des images converties pour plus de confidentialité
