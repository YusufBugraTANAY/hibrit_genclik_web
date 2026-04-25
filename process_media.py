import os
from PIL import Image
from pillow_heif import register_heif_opener
import shutil

register_heif_opener()

projects_dir = r"public/images/projects"
old_folder_name = "KA152 Let's Do it in the Social Field"
new_folder_name = "ka152-social-field"

old_folder_path = os.path.join(projects_dir, old_folder_name)
new_folder_path = os.path.join(projects_dir, new_folder_name)

# 1. Rename folder if it exists
if os.path.exists(old_folder_path):
    print(f"Renaming folder from '{old_folder_name}' to '{new_folder_name}'...")
    try:
        shutil.move(old_folder_path, new_folder_path)
    except Exception as e:
        print(f"Error renaming folder: {e}")
        exit(1)
        
target_dir = new_folder_path if os.path.exists(new_folder_path) else old_folder_path

if not os.path.exists(target_dir):
    print(f"Directory {target_dir} not found!")
    exit(1)

# 2. Process files in the target directory
img_count = 1
vid_count = 1

for filename in sorted(os.listdir(target_dir)):
    file_path = os.path.join(target_dir, filename)
    if not os.path.isfile(file_path):
        continue
        
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == ".heic":
        new_name = f"{img_count}.jpg"
        new_path = os.path.join(target_dir, new_name)
        print(f"Converting {filename} -> {new_name} ...")
        try:
            img = Image.open(file_path)
            img = img.convert("RGB")
            img.save(new_path, "JPEG", quality=85)
            img.close()
            os.remove(file_path)
            img_count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    elif ext == ".mov" or ext == ".mp4":
        new_name = f"vid-{vid_count}{ext}"
        new_path = os.path.join(target_dir, new_name)
        print(f"Renaming video {filename} -> {new_name} ...")
        try:
            os.rename(file_path, new_path)
            vid_count += 1
        except Exception as e:
            print(f"Error renaming {file_path}: {e}")
    else:
        # Just rename nicely
        if ext in [".jpg", ".png", ".jpeg"]:
            new_name = f"{img_count}{ext}"
            new_path = os.path.join(target_dir, new_name)
            if file_path != new_path:
                try:
                    os.rename(file_path, new_path)
                    img_count += 1
                except Exception as e:
                    print(f"Error renaming {file_path}: {e}")
            else:
                img_count += 1

print("Media processing complete!")
