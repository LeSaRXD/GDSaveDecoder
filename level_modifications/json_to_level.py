from json import loads

def dict_to_str(data: dict) -> str:
    return ",".join([key + "," + data[key] for key in data.keys()]) + ";"

level_data = ""

while True:
    try:
        with open("./files/levels/" + input("Enter file name: "), "r") as file:
            level_data = file.read()
        break
    except:
        print("File not found")

level_data = loads(level_data)

data = level_data["header"] + ";"
for block in level_data["blocks"]:
    data += dict_to_str(block) + "\n"

filename = input("Enter output file name: ")
with open("./files/levels/" + filename, "w") as file:
    file.write(data)
    print(f"Created ./files/levels/{filename}")
