from base64 import b64encode
from zlib import compress as gzip
from enum import Enum



class Gamemode(Enum):
    CUBE = 0
    SHIP = 1
    BALL = 2
    UFO = 3
    WAVE = 4
    ROBOT = 5
    SPIDER = 6

class Speed(Enum):
    NORMAL = 0
    SLOW = 1
    X2 = 2
    X3 = 3
    X4 = 4



class HSV:
    def __init__(self, hue=0, saturation=0, value=0, add_saturation=False, add_value=False) -> None:
        self.hue = hue
        self.saturation = saturation
        self.value = value
    
        self.add_saturation = add_saturation
        self.add_value = add_value

    def __repr__(self) -> str:
        return f"{self.hue}a{self.saturation}a{self.value}a{+self.add_saturation}a{+self.add_value}"

class Color:
    def __init__(self, id: int, r: int, g: int, b: int, a: float, blending: bool, copy_color_id=-1, copy_color_hsv=HSV(), copy_color_opacity=False) -> None:
        self.id = id

        self.r = r
        self.g = g
        self.b = b
        self.a = a

        self.blending = blending

        self.copy_color_id = copy_color_id
        self.copy_color_hsv = copy_color_hsv
        self.copy_color_opacity = copy_color_opacity
        
    def __repr__(self) -> str:
        r = f"1_{self.r}_2_{self.g}_3_{self.b}_6_{self.id}_7_{self.a}"
        if self.blending:
            r += f"_5_1"
        if self.copy_color_id >= 0:
            r += f"_9_{self.copy_color_id}_10_{self.copy_color_hsv}_17_{+self.copy_color_opacity}"

        return r

class Block:
    def __init__(self, id: int, x: float, y: float, attrs: dict) -> None:
        self.id = id

        self.x = x
        self.y = y

        self.attrs = attrs
    
    def __repr__(self) -> str:
        info = {
            1: self.id,
            2: (30 * self.x) + 15,
            3: (30 * self.y) + 15
        }
        info.update(self.attrs)
    
        return ",".join([f"{str(key)},{str(value)}" for key, value in info.items()]) + ";"



class LevelData:
    def __init__(self, blocks: list[Block]=[], colors: list[Color]=[], gamemode=Gamemode.CUBE, mini=False, speed=Speed.NORMAL, dual=False, is_2_player=False, bg_id=0, ground_id=0, ground_line_solid=False, font=0) -> None:
        # gameplay
        self.blocks = blocks

        self.gamemode = gamemode
        self.mini = mini
        self.speed = speed

        self.dual = dual
        self.is_2_player = is_2_player

        # visuals
        self.colors = colors

        self.bg_id = bg_id
        self.ground_id = ground_id
        self.ground_line_solid = ground_line_solid

        self.font = font
        
    def __repr__(self) -> str:
        header = {
            "kA2": self.gamemode.value,
            "kA3": +self.mini,
            "kA4": self.speed.value,
            "kA6": self.ground_id,
            "kA7": self.bg_id,
            "kA10": +self.is_2_player,
            "kA17": self.ground_line_solid + 1,
            "kA18": self.font
        }

        if len(self.colors) > 0:
            header["kS38"] = "|".join(self.colors) + "|"
        
        r_str = ",".join([f"{key},{value}" for key, value in header.items()])
        r_str += ";"

        r_str += ";".join([str(block) for block in self.blocks])

        return r_str

    @property
    def encoded(self) -> str:
        return b64encode(gzip(str(self).encode('utf-8')), b'-_').decode('utf-8')

class Level:
    def __init__(self, name: str, level_data: LevelData, description="", verified=False) -> None:
        self.name = name
        self.description = description

        self.level_data = level_data

        self.verified = verified
    
    def __repr__(self):
        info = {
            "kCEK": 4,
            "k2": self.name,
            "k4": self.level_data.encoded,
            "k5": "Player",
            "k21": 2,
            "k50": 35
        }

        if self.description != "":
            info["k3"] = b64encode(self.description.encode('utf-8'), b'-_').decode('utf-8')

        if self.verified:
            info["k14"] = True
        
        def parse(value):
            # if int
            if isinstance(value, int):
                return f"<i>{value}</i>"
            # if float
            if isinstance(value, float):
                return f"<r>{value}</r>"
            # if bool
            if isinstance(value, bool):
                if value:
                    return "<t />"
                return "<f />"           
            # everything else is string
            return f"<s>{value}</s>"
        
        return "<d>\n" + "\n".join([f"<k>{key}</k>{parse(value)}" for key, value in info.items()]) + "\n</d>"

    def insert_into_file(self, filename="./files/CCLocalLevels.xml") -> None:
        data = ""
        with open(filename, "r") as file:
            data = file.read()
        with open(filename.replace(".xml", "_old.xml"), "w") as file:
            file.write(data)
         
        max_k = 0
        while f"<k>k_{max_k}</k>" in data:
            max_k += 1

        for k in range(max_k, 0, -1):
            data = data.replace(f"<k>k_{k - 1}</k>", f"<k>k_{k}</k>")

        insert_pos = data.find("\n", data.find("<t", data.find("<k>_isArr</k>")))

        data = data[:insert_pos] + "\n<k>k_0</k>\n" + str(self) + data[insert_pos:]

        with open(filename, "w") as file:
            file.write(data)
        