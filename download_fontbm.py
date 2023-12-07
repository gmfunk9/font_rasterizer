import subprocess
import os
import sys
import stat

# Function to check if fontbm exists and download it if it does not
def check_and_download_fontbm(fontbm_path):
    if not os.path.isfile(fontbm_path):
        print("fontbm not found. Downloading fontbm...")
        
        try:
            # Assuming Linux x64 for this example
            subprocess.run([
                "curl", "-L",
                "https://github.com/vladimirgamalyan/fontbm/releases/download/v0.6.1/fontbm",
                "-o", "fontbm"
            ], check=True)

            os.chmod(fontbm_path, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

            print("fontbm downloaded and set as executable.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while downloading fontbm: {e}")
            sys.exit(1)


fontbm_path = "./fontbm"
check_and_download_fontbm(fontbm_path)