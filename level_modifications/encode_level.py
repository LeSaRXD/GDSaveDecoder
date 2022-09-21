from zlib import compress as gzip
from base64 import b64encode

def encode_level(is_main=False):
    level_data = ""

    while True:
        try:
            with open(f".{'.' if is_main else ''}/files/levels/{input('Enter file name: ')}", "r") as file:
                level_data = file.read()
            break
        except:
            print("file not found")

    level_data = level_data.replace("\n", "") # remove added newlines

    level_data = level_data.encode("utf-8")
    level_data = gzip(level_data)
    level_data = b64encode(level_data, b"-_")
    level_data = level_data.decode("utf-8")



    with open(f".{'.' if is_main else ''}/files/CCLocalLevels.xml", "r") as file:
        data = file.read()

    name = ""

    while True:
        name = input("Enter level name: ")

        name_start_index = data.find(f"<s>{name}") + 3
        if name_start_index <= 3:
            print("Level name not found")
            continue

        name_end_index = data.find("</s>", name_start_index)

        name = data[name_start_index:name_end_index]

        if input(f"Is '{data[name_start_index:name_end_index]}' your level? (y/n): ").lower() == "y":
            global level_start_index, level_end_index
            level_start_index = data.find("<s>", data.find("<k>k4</k>", name_end_index)) + 3
            level_end_index = data.find("</s>", level_start_index)
            break

    data = data[:level_start_index] + level_data + data[level_end_index:]

    with open(f".{'.' if is_main else ''}/files/CCLocalLevels.xml", "w") as file:
        file.write(data)

    print(f"Updated .{'.' if is_main else ''}/files/CCLocalLevel.xml")

if __name__ == "__main__":
    encode_level(True)
