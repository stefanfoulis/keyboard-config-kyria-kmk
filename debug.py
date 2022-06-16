import time

import board
import digitalio
from storage import getmount


def detect_side():
    name = str(getmount("/").label)
    if name.endswith("L"):
        return "L"
    elif name.endswith("R"):
        return "R"


side = detect_side()


if side == "L":
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


col_io_pins = [digitalio.DigitalInOut(pin) for pin in col_pins]
row_io_pins = [digitalio.DigitalInOut(pin) for pin in row_pins]


def debug_raw_keymap():
    rows = []
    cols = []
    for i, pin in enumerate(col_io_pins):
        cols.append(f"COL{i} {pin.value}")
    for i, pin in enumerate(row_io_pins):
        rows.append(f"ROW{i} {pin.value}")
    return rows, cols


def debug_raw_keymap_str():
    rows, cols = debug_raw_keymap()
    return "\n".join(rows + cols)


def d():
    while True:

        print("\n" * 10)
        print(debug_raw_keymap_str())
        time.sleep(0.1)
