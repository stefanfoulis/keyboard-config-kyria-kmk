# originally copied from https://github.com/KMKfw/kmk_firmware/blob/e7d306cf300b3ad2a3c1b148e9da64a368ed6ae8/boards/kyria/main.py
try:
    from typing import Type
except ImportError:
    pass
import time

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitType
from kyria_v2_nice_nano import KMKKeyboard, get_side_aware_keyboard_class

print()
print()
print("=" * 80)
print(f"{time.time()}")

keyboard_class: Type[KMKKeyboard] = get_side_aware_keyboard_class()
keyboard = keyboard_class()
print(f"side: {keyboard.side} {keyboard}")
# keyboard.debug_enabled = True


keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())

# Using drive names (KYRIAL, KYRIAR) to recognize sides; use split_side arg if you're not doing it
split = Split(
    split_type=SplitType.BLE,
    split_side=keyboard.side,
    split_flip=False,
    debug_enabled=True,
)
keyboard.modules.append(split)

# Uncomment below if you're having RGB
rgb_ext = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=10,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
    val_default=10,
    val_limit=32,
)
keyboard.extensions.append(rgb_ext)

from keymap import keymap

keyboard.keymap = keymap

# Uncomment below if using an encoder
# Edit your encoder layout below
encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
)
keyboard.modules.append(encoder_handler)


if __name__ == "__main__":
    # detect_side()
    # print("Not starting... ready for REPL")
    print("yay! keyboard.go()!")
    keyboard.go()
