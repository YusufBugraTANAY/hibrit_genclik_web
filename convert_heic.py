import os
from PIL import Image
from pillow_heif import register_heif_opener
import shutil

register_heif_opener()

projects_dir = r"public/images/projects"

# Walk through the directories
for root, dirs, files in os.walk(projects_dir):
    heic_files = [f for f in files if f.lower().endswith(".heic")]
    if not heic_files:
        continue
    
    print(f"Processing folder: {root}")
    
    # Check if there's already a file that has '1' in its name (like 1.HEIC)
    cover_file = None
    other_files = []
    
    for f in heic_files:
        if f.startswith("1."):
            cover_file = f
        else:
            other_files.append(f)
            
    # Sort the other files just to have a deterministic order
    other_files.sort()
    
    # Let's create the final mapping of old_name -> new_name (jpg)
    conversion_map = {}
    
    if cover_file:
        conversion_map[cover_file] = "1.jpg"
        
    # Assign names 2.jpg to 10.jpg for the rest
    counter = 2
    for f in other_files:
        conversion_map[f] = f"{counter}.jpg"
        counter += 1
        
    for old_name, new_name in conversion_map.items():
        old_path = os.path.join(root, old_name)
        new_path = os.path.join(root, new_name)
        
        try:
            print(f"Converting {old_name} -> {new_name} ...")
            img = Image.open(old_path)
            # Convert to RGB to save as JPEG
            img = img.convert("RGB")
            img.save(new_path, "JPEG", quality=85)
            
            # Close image to free file handles before deleting
            img.close()
            
            # Delete original
            os.remove(old_path)
        except Exception as e:
            print(f"Error processing {old_path}: {e}")

# Rename the folder from the long Unicode name to 'ka154-afetlere-karsi'
bad_folder_name = "KA154 Gençlerin Öncülüğünde Afetlere Karşı Hep Birlikte"
bad_folder_path = os.path.join(projects_dir, bad_folder_name)
good_folder_path = os.path.join(projects_dir, "ka154-afetlere-karsi")

if os.path.exists(bad_folder_path):
    print("Renaming folder...")
    try:
        shutil.move(bad_folder_path, good_folder_path)
        print("Folder successfully renamed.")
    except Exception as e:
        print(f"Error renaming folder: {e}")

print("Done!")
