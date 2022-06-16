import time

import board
import digitalio
from keypad import KeyMatrix
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

matrix = KeyMatrix(row_pins=row_pins, column_pins=col_pins)
state = {}
for r in range(len(row_pins)):
    state[r] = {}
    for c in range(len(col_pins)):
        state[r][c] = False


def state_str_matrix():
    state_str_lst = []
    for cols in state.values():
        row_str = " ".join(["✅" if value else "⬜" for value in cols.values()])
        state_str_lst.append(row_str)
    return "\n".join(state_str_lst)


while True:
    # print("\n" * 3)
    # print("=" * 10)
    # print(time.time())
    # print(matrix)
    # print(f"key_count: {matrix.key_count}")
    while e := matrix.events.get():
        row, col = matrix.key_number_to_row_column(e.key_number)
        state[row][col] = e.pressed
        # print(f"Row: {row} Col: {col}  {e}")
        print("\n" * 20 + state_str_matrix())
    time.sleep(0.25)
