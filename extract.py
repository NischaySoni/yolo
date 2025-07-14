import tarfile
import os
from tqdm import tqdm

# Path to your tar.gz file
archive_path = 'C:/Users/lenovo/OneDrive/Desktop/IP/nistspecmaxhold128data.tar.gz'

# Destination folder
output_path = 'C:/Users/lenovo/OneDrive/Desktop/IP/NIST-128'

# Extract with progress bar
with tarfile.open(archive_path, 'r:gz') as tar:
    members = tar.getmembers()
    print(f"Total files to extract: {len(members)}")
    
    for member in tqdm(members, desc="Extracting", unit="file"):
        tar.extract(member, path=output_path)

print("✅ Extraction completed.")
