import os
import tarfile

# List of tar.gz files in the same folder
tar_files = [
    "raddet40k128hw001tv2.tar.gz",
    "raddet40k128hw009tv2.tar.gz",
    "nistspecmaxhold128data.tar.gz"
]

# Valid image extensions to check
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')

# Loop through each file
for tar_name in tar_files:
    if os.path.exists(tar_name):
        print(f"\n✅ {tar_name} exists.")
        try:
            with tarfile.open(tar_name, 'r') as tar:
                members = tar.getmembers()
                image_count = sum(1 for m in members if m.name.lower().endswith(image_extensions))
                print(f"📸 Contains {image_count} image(s).")
        except Exception as e:
            print(f"❌ Error reading {tar_name}: {e}")
    else:
        print(f"\n❌ {tar_name} does NOT exist.")
