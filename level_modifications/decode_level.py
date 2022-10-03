from zlib import decompress as gunzip, MAX_WBITS
from base64 import b64decode

def decode_level(is_main=False):
    data = ""

    with open(f".{'.' if is_main else ''}/files/CCLocalLevels.xml", "r") as file:
        data = file.read()

    name = ""

    while True:
        name = input("Enter level name: ")

        name_start_index = data.lower().find(f"<s>{name}") + 3
        if name_start_index <= 3:
            print("Level name not found")
            continue

        name_end_index = data.find("</s>", name_start_index)

        name = data[name_start_index:name_end_index]

        if input(f"Is '{data[name_start_index:name_end_index]}' your level? (Y/n): ").lower() != "n":
            global level_start_index, level_end_index
            level_start_index = data.find("<s>", data.find("<k>k4</k>", name_end_index)) + 3
            level_end_index = data.find("</s>", level_start_index)
            break

    level_data = data[level_start_index:level_end_index]

    level_data = level_data.encode("utf-8")

    level_data = b64decode(level_data + b"==", b"-_")
    try:
        level_data = gunzip(level_data, MAX_WBITS | 16)
    except:
        try:
            level_data = gunzip(level_data, -MAX_WBITS)
        except:
            try:
                level_data = gunzip(level_data, MAX_WBITS)
            except:
                print("couldn't decompress")
                return

    level_data = level_data.decode("utf-8")

    level_data = level_data.replace(",", ",\n")
    level_data = level_data.replace("|", "|\n")
    level_data = level_data.replace(";", ";\n") # add newlines for readability

    with open(f".{'.' if is_main else ''}/files/levels/{name.replace(' ', '_')}.txt", "w") as output:
        output.write(level_data)

    print(f"Created .{'.' if is_main else ''}/files/levels/{name.replace(' ', '_')}.txt")

if __name__ == "__main__":
    decode_level(True)
