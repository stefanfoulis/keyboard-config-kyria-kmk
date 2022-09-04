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

# Edit your layout below
# Currently, that's a default QMK Kyria Layout - https://config.qmk.fm/#/splitkb/kyria/rev1/LAYOUT

A_SHIFT = KC.MT(KC.A, KC.LSHIFT)
S_CTL = KC.MT(KC.S, KC.LCTL)
D_ALT = KC.MT(KC.D, KC.LALT)
F_GUI = KC.MT(KC.F, KC.LGUI)
J_GUI = KC.MT(KC.J, KC.RGUI)
K_ALT = KC.MT(KC.K, KC.RALT)
L_CTL = KC.MT(KC.L, KC.RCTL)
SCLN_SHIFT = KC.MT(KC.SCLN, KC.RSHIFT)

LGREEN = KC.MO(2)
LBLUE = KC.MO(1)
LRED = KC.MO(3)
W_TILING = KC.MO(4)

ESC_LCTL = KC.MT(KC.ESC, KC.LCTL)
QUOTE_RCTL = KC.MT(KC.QUOTE, KC.RCTL)
ENT_LALT = KC.MT(KC.ENT, KC.LALT)
MINUS_RCTL = KC.MT(KC.MINUS, KC.RCTL)
ENT_RSHIFT = KC.MT(KC.ENT, KC.RSHIFT)
SPC_LSHIFT = KC.MT(KC.SPC, KC.LSHIFT)

SHFT_TAB = KC.LSHIFT(KC.TAB)

# Window Tiling
W_FULL = KC.LGUI(KC.UP)
W_LEFT = KC.LGUI(KC.LEFT)
W_RIGHT = KC.LGUI(KC.RGHT)
W_NORM = KC.LGUI(KC.DOWN)

W_SCR_UP = KC.LSHIFT(KC.LGUI(KC.UP))
W_SCR_DWN = KC.LSHIFT(KC.LGUI(KC.DOWN))
W_SCR_LEFT = KC.LSHIFT(KC.LGUI(KC.LEFT))
W_SCR_RGHT = KC.LSHIFT(KC.LGUI(KC.RGHT))


# fmt: off
keyboard.keymap = [
    [
        KC.MPLY,    KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,                                                       KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.VOLU,
        KC.MNXT,    A_SHIFT,    S_CTL,      D_ALT,      F_GUI,      KC.G,                                                       KC.H,       J_GUI,      K_ALT,      L_CTL,      SCLN_SHIFT, KC.VOLD,
        KC.MPRV,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,        KC.LBRC,    KC.CAPS,    LRED,      KC.RBRC,    KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.MUTE,
                                            W_TILING,   KC.LALT,     KC.LGUI,    SPC_LSHIFT, LBLUE,      LGREEN,    ENT_RSHIFT, KC.RCTL,    KC.RGUI,    KC.APP,
    ],
    # BLUE
    [
        KC.TRNS,    KC.ESC,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.PGUP,    KC.HOME,    KC.UP,      KC.END,     KC.TRNS,    KC.DEL,
        KC.TRNS,    SHFT_TAB,   KC.TAB,     KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.PGDN,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.TRNS,    KC.INS,
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.SLCK,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.BSPC,    KC.DEL,     KC.TRNS,    KC.TRNS,    KC.PSCR,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    # GREEN
    [
        KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                                                      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.EQL,
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,                                                    KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PLUS,
        KC.PIPE,    KC.BSLS,    KC.COLN,    KC.SCLN,    KC.MINS,    KC.LBRC,    KC.LCBR,    KC.TRNS,    KC.TRNS,    KC.RCBR,    KC.RBRC,    KC.UNDS,    KC.COMM,    KC.DOT,     KC.SLSH,    KC.QUES,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    # RED
    [
        KC.TRNS,    KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.TRNS,                                                    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,    KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.TRNS,                                                    KC.TRNS,    KC.RSFT,    KC.RCTL,    KC.LALT,    KC.RGUI,    KC.TRNS,
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    # Window Tiling
    [
        KC.TRNS,    KC.TRNS,    KC.TRNS,    W_SCR_UP,   KC.TRNS,    KC.TRNS,                                                    KC.TRNS,    KC.TRNS,    W_FULL,   KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,    KC.TRNS,    W_SCR_LEFT, W_SCR_DWN,  W_SCR_RGHT, KC.TRNS,                                                    KC.TRNS,    W_LEFT,     W_NORM,   W_RIGHT,    KC.TRNS,    KC.TRNS,
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.MPLY,  KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
]
# fmt: on

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
