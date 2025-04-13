import os
import shutil
import random
from pathlib import Path
from IPython.display import display, Markdown

# 🔧 Define source and destination paths
original_root = "dataset"  # Change to your dataset path
balanced_root = "balanced_dataset"
os.makedirs(balanced_root, exist_ok=True)

# 📂 Class folders mapping
class_folders = {
    'Real': 'Real',
    'Altered-Easy': 'Altered-Easy',
    'Altered-Medium': 'Altered-Medium',
    'Altered-Hard': 'Altered-Hard'
}

# ✅ Step 1: Collect BMP images from each class
class_images = {}
for class_name, folder in class_folders.items():
    folder_path = os.path.join(original_root, folder)
    images = [img for img in os.listdir(folder_path) if img.lower().endswith(".bmp")]
    class_images[class_name] = images
    display(Markdown(f"**{class_name}**: Found `{len(images)}` BMP images"))

# ✅ Step 2: Determine minimum class size
target_samples = min(len(images) for images in class_images.values())
display(Markdown(f"### 🟢 Balancing all classes to `{target_samples}` samples each"))

# ✅ Step 3: Create balanced dataset
for class_name, images in class_images.items():
    # Create class subfolder
    dest_folder = os.path.join(balanced_root, class_name)
    os.makedirs(dest_folder, exist_ok=True)

    # Randomly sample `target_samples` images
    sampled = random.sample(images, target_samples)

    for img_name in sampled:
        src = os.path.join(original_root, class_name, img_name)
        dst = os.path.join(dest_folder, img_name)
        shutil.copy2(src, dst)

    display(Markdown(f"✅ Copied `{len(sampled)}` images to `{dest_folder}`"))

display(Markdown("### ✅ Dataset balancing complete!"))
