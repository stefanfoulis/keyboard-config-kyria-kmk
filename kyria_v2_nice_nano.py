try:
    from typing import Optional, Type
except ImportError:
    pass

import board
from split_side import SPLIT_SIDE

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.split import SplitSide
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic

PER_SIDE_COL_COUNT = 8
PER_SIDE_ROW_COUNT = 4


# The Kyria (v2) has rows numbered from top to bottom and COLs numbered from inside to
# outside. So on both halves COL0 and COL1 are the cols with only the square of inner
# thumb keys. And COL7 is always the outer-most column.
# fmt: off
LEFT = [
    # On the left side Columns are numbered from right to left. Col0 and Col1 don't
    # have any keys on Row0 and Row1.
    [ 7,  6,  5,  4,  3,  2],          # ROW0
    [15, 14, 13, 12, 11, 10],          # ROW1
    [23, 22, 21, 20, 19, 18, 17, 16],  # ROW2 (17 and 16 are the top thumb keys)
    [            29, 27, 26, 25, 24],  # ROW3 (thumb keys. 28 is skipped, idk why)
]
RIGHT = [  
    # On the right side Columns are numbered from left to right. Col0 and Col1 don't
    # have any keys on Row0 and Row1
    [         2,  3,  4,  5,  6,  7],  # ROW0
    [        10, 11, 12, 13, 14, 15],  # ROW1
    [16, 17, 18, 19, 20, 21, 22, 23],  # ROW2 (17 and 16 are the top thumb keys)
    [24, 25, 26, 27, 29],              # ROW3 (thumb keys. 28 is skipped, idk why)
]
# fmt: on

MATRIX_KEY_COUNT = PER_SIDE_ROW_COUNT * PER_SIDE_COL_COUNT
coord_mapping = []
for row in range(PER_SIDE_ROW_COUNT):
    coord_mapping.extend(LEFT[row])
    # All the values on the right side come after all the value on the left.
    # So add the amount of keys on the left to the right.
    for cell in RIGHT[row]:
        coord_mapping.append(MATRIX_KEY_COUNT + cell)
print(coord_mapping)


class KMKKeyboard(_KMKKeyboard):
    side: Optional[int] = None
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.P0_08
    rgb_pixel_pin = board.P0_06
    coord_mapping = coord_mapping


class KMKKeyboardLeft(KMKKeyboard):
    side = SplitSide.LEFT
    col_pins = (
        board.P0_10,
        board.P0_09,
        board.P1_06,
        board.P1_04,
        board.P0_11,
        board.P1_00,
        board.P0_24,
        board.P0_22,
    )
    row_pins = (
        board.P0_02,
        board.P1_15,
        board.P1_13,
        board.P1_11,
    )
    encoder_pin_0 = board.P0_31
    encoder_pin_1 = board.P0_29


class KMKKeyboardRight(KMKKeyboard):
    side = SplitSide.RIGHT
    col_pins = (
        board.P1_04,
        board.P1_06,
        board.P0_09,
        board.P0_10,
        board.P1_11,
        board.P1_13,
        board.P1_15,
        board.P0_02,
    )
    row_pins = (
        board.P0_22,
        board.P0_24,
        board.P1_00,
        board.P0_11,
    )
    encoder_pin_0 = board.P0_29
    encoder_pin_1 = board.P0_31


def pretty_side(side):
    if side == SplitSide.LEFT:
        return "left"
    elif side == SplitSide.RIGHT:
        return "right"
    return "unknown"


def detect_side_by_pin():
    # FIXME: this isn't working yet :confused:
    import board
    import digitalio

    pin1 = digitalio.DigitalInOut(board.P1_11)
    pin2 = digitalio.DigitalInOut(board.P0_11)
    print(f"pin1: {pin1.value} pin2: {pin2.value}")
    if not pin1.value and not pin2.value:
        # both low means right
        print("Detected Right-Side")
        side = SplitSide.RIGHT
    else:
        print("Detected Left-Side")
        side = SplitSide.LEFT
    pin1.deinit()
    pin2.deinit()
    print(f"detected side: {pretty_side(side)} (by pins)")
    return side


def detect_side_by_mount():
    from storage import getmount

    name = str(getmount("/").label)
    if name.endswith("R"):
        side = SplitSide.RIGHT
    elif name.endswith("L"):
        side = SplitSide.LEFT
    else:
        raise RuntimeError(f"Couldn't detect side from drive name ({name})")
    print(f"detected side: {pretty_side(side)} (by drive name)")
    return side


def detect_side_by_static_file():
    from split_side import SPLIT_SIDE

    print(f"detected side: {pretty_side(SPLIT_SIDE)} (by hardcoded file)")
    return SPLIT_SIDE


def get_side_aware_keyboard_class() -> Type[KMKKeyboard]:
    side = detect_side_by_static_file()
    if side == SplitSide.LEFT:
        return KMKKeyboardLeft
    elif side == SplitSide.RIGHT:
        return KMKKeyboardRight
    raise RuntimeError("Couldn't determine side")
