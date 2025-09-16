import os

music_folder = '/run/user/1000/gvfs/mtp:host=Xiaomi_POCO_M3_e9bc7baf1220/Internal shared storage/Music'

image_extensions = ('.png', '.jpg', '.jpeg', '.bmp')

def delete_image_files(folder):
    # Expand the user directory
    folder = os.path.expanduser(folder)
    
    print(f'Scanning folder: {folder}')  # Debugging output
    
    found_images = []  # list to store found image files
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                found_images.append(file_path)  # Add found image to the list
                try:
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
                except Exception as e:
                    print(f'Error deleting {file_path}: {e}')
    
    # Show only found images
    if found_images:
        print("\nFound image files:")
        for image in found_images:
            print(image)
    else:
        print("No image files found.")

# Scan the specified folder
delete_image_files(music_folder)
