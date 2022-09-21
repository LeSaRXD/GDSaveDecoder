from os import makedirs
from save_modifications import decode_save, encode_save
from level_modifications import decode_level, modify_level, encode_level

makedirs("./files/levels", exist_ok=True)

decode_save.decode_save()
decode_level.decode_level()
modify_level.modify_level()
encode_level.encode_level()
encode_save.encode_save()
