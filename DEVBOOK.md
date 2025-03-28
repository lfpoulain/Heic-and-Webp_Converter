# Journal de développement

## Version 1.0.0 (2025-01-25)

### Fonctionnalités initiales
- Conversion des images HEIC en JPEG
- Support du glisser-déposer
- Conservation des images originales
- Gestion des fichiers en doublon
- Système de logging pour le suivi des conversions

### Détails techniques
- Utilisation de pillow-heif pour le support HEIC
- Qualité JPEG fixée à 95% pour un bon compromis qualité/taille
- Les images sont automatiquement converties en RGB si nécessaire
- Gestion des erreurs avec logging dans converter.log

## Version 1.1.0 (2025-01-25)

### Modifications
- Suppression automatique des données EXIF lors de la conversion
- Amélioration du message de log pour indiquer la suppression des EXIF

### Détails techniques
- Utilisation d'une nouvelle image vierge pour garantir l'absence totale de métadonnées
- Conservation de la qualité d'image à 95%

## Version 2.0.0 (2025-03-28)

### Nouvelles fonctionnalités
- Support du format WebP en entrée
- Détection automatique et préservation des couches alpha (transparence)
- Conversion en PNG pour les images avec transparence
- Conversion en JPEG pour les images sans transparence
- Création d'un exécutable Windows autonome
- Suppression de la génération du fichier de log

### Détails techniques
- Refactorisation du code avec une fonction de conversion générique
- Détection des canaux alpha via les modes d'image ('RGBA', 'LA', 'P' avec transparence)
- Utilisation de PyInstaller pour créer un exécutable autonome
- Optimisation de la taille de l'exécutable (27 Mo)
- Conservation des logs dans la console uniquement (pour le débogage)
- Interface utilisateur améliorée avec boîtes de dialogue pour les résultats
