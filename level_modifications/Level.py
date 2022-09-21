from base64 import b64encode
from operator import is_
from zlib import compress as gzip

class GDLevel:
    def __init__(self, name: str, description="", level_data="", is_verified=False) -> None:
        self.name = name
        self.description = description
        self.is_verified = is_verified
        self.level_data = level_data
        
    @property
    def save_str(self):
        return f"<d><k>kCEK</k><i>4</i><k>k2</k><s>{self.name}</s><k>k3</k><s>{b64encode(self.description.encode('utf-8'), b'-_').decode('utf-8')}</s><k>k4</k><s>{'' if self.level_data == '' else b64encode(gzip(self.level_data.encode('utf-8')), b'-_').decode('utf-8')}</s><k>k5</k><s>Player</s>{'<k>k14</k><t />' if self.is_verified else ''}<k>k21</k><i>2</i><k>k50</k><i>35</i></d>"

level1 = GDLevel("cool level", "cool level description", is_verified=True)
print(level1.save_str)