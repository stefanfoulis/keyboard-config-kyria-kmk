import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = tuple(
        reversed(
            [
                # board.P0_09,
                # board.P0_10,
                # board.P1_11,
                # board.P1_13,
                # board.P1_15,
                # board.P0_02,
                # board.P0_29,
                # board.P0_31,
                board.P0_31,
                board.P0_29,
                board.P0_02,
                board.P1_15,
                board.P1_13,
                board.P1_11,
                board.P0_10,
                board.P0_09,
            ]
        )
    )

    row_pins = (
        board.P1_04,
        board.P0_11,
        board.P1_00,
        board.P0_22,
        # board.P0_22,
        # board.P1_00,
        # board.P0_11,
        # board.P1_04,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.P0_08
    rgb_pixel_pin = board.P0_06
    encoder_pin_0 = board.P1_06
    encoder_pin_1 = board.P0_24

    coord_mapping = []
    coord_mapping.extend(ic(0, x, 8) for x in range(6))
    coord_mapping.extend(ic(4, x, 8) for x in range(5, -1, -1))
    coord_mapping.extend(ic(1, x, 8) for x in range(6))
    coord_mapping.extend(ic(5, x, 8) for x in range(5, -1, -1))
    coord_mapping.extend(ic(2, x, 8) for x in range(8))
    coord_mapping.extend(ic(6, x, 8) for x in range(7, -1, -1))
    coord_mapping.extend(ic(3, x, 8) for x in range(3, 8))
    coord_mapping.extend(ic(7, x, 8) for x in range(7, 2, -1))
