from enum import Enum
from random import randint as rand

def modify_level():
    data = ""

    while True:
        try:
            with open(f"./files/levels/{input('Enter file name: ')}", "r") as file:
                data = file.read()
            break
        except:
            print("File not found")

    class BLOCKS(Enum):
        SOLID = 1
        TRANSPARENT = 5
        SPIKE = 8
        ORB = 36

    def add_block(id: BLOCKS, x: float, y: float):
        nonlocal data
        data += f"\n1,{id.value},2,{30 * x + 15},3,{30 * y + 15};"



    height = 1
    width = 5

    x = 5
    y = 0

    for i in range(50): # create structures
        for dx in range(width): # for every x in structure (left to right)
            for dy in range(height): # for every y in structure (bottom to top)
                id = BLOCKS.TRANSPARENT # set default block to transparent

                if dy == height - 1: # set block to solid if top
                    id = BLOCKS.SOLID
                elif dx == 0 or dx == width - 1: # set block to solid if its on the side
                    id = BLOCKS.SOLID

                add_block(id, x + dx, y + dy) # push the block to data

        if width >= 5:
            for j in range(rand(0, 2)):
                add_block(BLOCKS.SPIKE, x + width // 2 + j, height)
                if width >= 7 and rand(0, 2) == 0:
                    add_block(BLOCKS.SPIKE, x + width // 2 + 2, height)

        x += width

        width += rand(-2, 2) # offset length
        if rand(0, 1) == 0: # add an orb with 50% chance
            add_block(BLOCKS.ORB, x + 2, height + 1)
            x += 5
            height += 2
        else:
            x += 3
            height += rand(-1, 1) # and height randomly

        if width <= 1: # check for non-positive width
            width = 2
        if height <= 0: # check for non-positive height
            height = 1



    filename = input('Enter output file name: ')
    with open(f"./files/levels/{filename}", "w") as file:
        file.write(data)
        print(f"Created ./files/levels/{filename}")

if __name__ == "__main__":
    modify_level()
