from json import dumps

def str_to_dict(data: str) -> dict:
    data = data.split(",")

    d = dict()

    for i in range(0, len(data) - 1, 2):
        d[data[i]] = data[i + 1]

    return d

data = ""

while True:
    try:
        with open("./files/levels/" + input("Enter file name: "), "r") as file:
            data = file.read()
        break
    except:
        print("FIle not found")

data = data.replace("\n", "")
data = data.split(";")

level_data = {
    "header": "",
    "blocks": []
}

level_data["header"] = data[0]
level_data["blocks"] = [str_to_dict(line) for line in data[1:] if line != ""]

filename = input("Enter output file name: ")
with open("./files/levels/" + filename, "w") as file:
    file.write(dumps(level_data, indent=4))
    print(f"Created ./files/levels/{filename}")