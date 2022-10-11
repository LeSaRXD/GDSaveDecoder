from base64 import b64encode
from zlib import compress as gzip
from sys import platform
from os import getlogin

def encode_save(is_main=False):
    code = ""

    with open(f".{'.' if is_main else ''}/files/CCLocalLevels.xml", "r") as file:
        code = file.read()

    code = code.replace("\n", "")
    code = code.encode("utf-8")

    code = gzip(code)
    code = b64encode(code, b"-_")
    code = bytes([i ^ 11 for i in code])

    filename = ""
    if platform == "linux":
        filename = f"/home/{getlogin()}/.steam/steam/steamapps/compatdata/322170/pfx/drive_c/users/steamuser/AppData/Local/GeometryDash/CCLocalLevels.dat"
    else:
        filename = f"C:/Users/{getlogin()}/AppData/Local/GeometryDash/CCLocalLevels.dat"
    
    with open(filename, "wb") as file:
        file.write(code)
        print(f"Saved {filename}")

if __name__ == "__main__":
    encode_save(True)
