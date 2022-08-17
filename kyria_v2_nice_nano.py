import board
from split_side import SPLIT_SIDE

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.split import SplitSide
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic

if SPLIT_SIDE == SplitSide.LEFT:
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
    encoder_pin_a = board.P0_31
    encoder_pin_b = board.P0_29
else:
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
    encoder_pin_a = board.P0_29
    encoder_pin_b = board.P0_31


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

MATRIX_KEY_COUNT = len(row_pins) * len(col_pins)
coord_mapping = []
for row in range(len(row_pins)):
    coord_mapping.extend(LEFT[row])
    # All the values on the right side come after all the value on the left.
    # So add the amount of keys on the left to the right.
    for cell in RIGHT[row]:
        coord_mapping.append(MATRIX_KEY_COUNT + cell)
print(coord_mapping)


class KMKKeyboard(_KMKKeyboard):
    col_pins = col_pins
    row_pins = row_pins
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.P0_08
    rgb_pixel_pin = board.P0_06
    encoder_pin_0 = encoder_pin_a
    encoder_pin_1 = encoder_pin_b

    coord_mapping = coord_mapping
