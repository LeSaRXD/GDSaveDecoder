from base64 import b64decode
from zlib import decompress as gunzip, MAX_WBITS

def decode_save(is_main=False):
    code = ""

    with open("/home/lesar/.steam/steam/steamapps/compatdata/322170/pfx/drive_c/users/steamuser/AppData/Local/GeometryDash/CCLocalLevels.dat", "rb") as file:
        code = file.read()

    code = bytes([i ^ 11 for i in code])
    code = b64decode(code + b"==", b"-_")
    
    try:
        code = gunzip(code, MAX_WBITS)
    except:
        try:
            code = gunzip(code, -MAX_WBITS)
        except:
            try:
                code = gunzip(code, MAX_WBITS | 16)
            except:
                print("couldn't decompress")
                return
    
    code = code.decode("utf-8")
    code = code.replace("<k>", "\n<k>")
    code = code.replace("<d>", "\n<d>")
    code = code.replace("</d>", "\n</d>")
    
    with open(f".{'.' if is_main else ''}/files/CCLocalLevels.xml", "w") as file:
        file.write(code)
        print("Saved ../files/CCLocalLevels.xml")

if __name__ == "__main__":
    decode_save(True)