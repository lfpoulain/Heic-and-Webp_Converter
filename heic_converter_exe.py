import sys
import os
from pillow_heif import register_heif_opener
from PIL import Image
import logging
import tkinter as tk
from tkinter import messagebox

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

def convert_image(input_path):
    """
    Convertit un fichier HEIC ou WebP en JPEG/PNG et supprime toutes les données EXIF.
    Les images avec canal alpha sont converties en PNG pour préserver la transparence.
    
    Args:
        input_path (str): Chemin vers le fichier à convertir
        
    Returns:
        tuple: (success, result) où success est un booléen indiquant si la conversion a réussi
               et result est soit le chemin du fichier de sortie, soit un message d'erreur
    """
    try:
        # Enregistrer le support HEIF si nécessaire
        if input_path.lower().endswith('.heic'):
            register_heif_opener()
        
        # Vérifier si le fichier existe
        if not os.path.exists(input_path):
            error_msg = f"Le fichier {input_path} n'existe pas"
            logging.error(error_msg)
            return False, error_msg

        # Ouvrir l'image
        with Image.open(input_path) as img:
            # Déterminer le format de sortie en fonction de la présence d'un canal alpha
            has_alpha = img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info)
            
            if has_alpha:
                # Si l'image a un canal alpha, convertir en PNG
                output_ext = '.png'
                output_format = 'PNG'
                # Conserver le mode avec alpha
                if img.mode != 'RGBA' and img.mode != 'LA':
                    img = img.convert('RGBA')
            else:
                # Sinon, convertir en JPEG
                output_ext = '.jpg'
                output_format = 'JPEG'
                # Convertir en RGB (nécessaire pour JPEG)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
            
            # Créer le nom du fichier de sortie
            output_path = os.path.splitext(input_path)[0] + output_ext
            
            # Si le fichier de sortie existe déjà, ajouter un numéro
            counter = 1
            while os.path.exists(output_path):
                base, _ = os.path.splitext(input_path)
                output_path = f"{base}_{counter}{output_ext}"
                counter += 1

            # Créer une nouvelle image sans EXIF
            data = list(img.getdata())
            image_without_exif = Image.new(img.mode, img.size)
            image_without_exif.putdata(data)
            
            # Sauvegarder l'image sans EXIF
            if output_format == 'JPEG':
                image_without_exif.save(output_path, output_format, quality=95)
            else:
                image_without_exif.save(output_path, output_format)
        
        logging.info(f"Conversion réussie (sans EXIF) : {input_path} -> {output_path}")
        return True, output_path
        
    except Exception as e:
        error_msg = f"Erreur lors de la conversion de {input_path}: {str(e)}"
        logging.error(error_msg)
        return False, error_msg

def convert_heic_to_jpeg(heic_path):
    """
    Fonction de compatibilité qui appelle la nouvelle fonction convert_image
    """
    return convert_image(heic_path)

def main():
    setup_logging()
    
    # Créer une fenêtre Tkinter cachée (nécessaire pour les boîtes de dialogue)
    root = tk.Tk()
    root.withdraw()

    # Vérifier si des fichiers ont été fournis
    if len(sys.argv) < 2:
        messagebox.showerror("Erreur", "Aucun fichier n'a été fourni. Glissez des fichiers HEIC ou WebP sur l'exécutable.")
        return

    success_count = 0
    error_count = 0
    error_messages = []

    # Traiter chaque fichier
    for file_path in sys.argv[1:]:
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext in ['.heic', '.webp']:
            success, result = convert_image(file_path)
            if success:
                success_count += 1
            else:
                error_count += 1
                error_messages.append(result)
        else:
            error_count += 1
            error_messages.append(f"Le fichier {file_path} n'est pas un fichier pris en charge (HEIC, WebP)")

    # Afficher le résumé
    message = f"Conversion terminée !\n\n"
    message += f"Images converties avec succès : {success_count}\n"
    message += f"Erreurs : {error_count}\n"
    
    if error_messages:
        message += "\nDétails des erreurs :\n"
        message += "\n".join(error_messages)

    messagebox.showinfo("Résultat de la conversion", message)

if __name__ == "__main__":
    main()
