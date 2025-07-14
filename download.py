import requests
import os

# Target URL
url = "https://data.researchdatafinder.qut.edu.au/dataset/25cd66cb-1b82-4030-aeb2-df81b8d549e6/resource/03189ee3-9a4d-46a1-a668-2b98b58017de/download/raddet40k128hw001tv2.tar.gz"

# Output file name
filename = "raddet40k128hw001tv2.tar.gz"

# Check if file partially exists
start_byte = os.path.getsize(filename) if os.path.exists(filename) else 0
headers = {
    "Range": f"bytes={start_byte}-",
    "User-Agent": "Mozilla/5.0",              # Some servers reject non-browser agents
    "Accept-Encoding": "identity"             # Ask for raw bytes (disable gzip decode)
}

# Send request with streaming and manual decoding
response = requests.get(url, headers=headers, stream=True)
response.raise_for_status()

# Total size to download
total_size = int(response.headers.get("Content-Length", 0)) + start_byte

# Open file in append binary mode
with open(filename, "ab") as f:
    downloaded = start_byte
    for chunk in response.raw.stream(8192, decode_content=False):
        if chunk:
            f.write(chunk)
            downloaded += len(chunk)
            done = int(50 * downloaded / total_size)
            print(f"\r[{'=' * done}{' ' * (50 - done)}] {downloaded / 1024 / 1024:.2f} MB / {total_size / 1024 / 1024:.2f} MB", end='')

print("\n✅ Download completed successfully.")
