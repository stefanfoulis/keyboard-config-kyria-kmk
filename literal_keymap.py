from kmk.keys import KC

__all__ = ["keymap"]

# Edit your layout below
# Original based on a default QMK Kyria Layout - https://config.qmk.fm/#/splitkb/kyria/rev1/LAYOUT

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

COPY = KC.LCTL(KC.INS)
PASTE = KC.LSHIFT(KC.INS)

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
keymap = [
    [
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,                                                       KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSPC,
        KC.SPC,     KC.A,       KC.S,       KC.D,       KC.F,       KC.G,                                                       KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.ENT,
        KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,        KC.LBRC,    KC.CAPS,    LRED,      KC.RBRC,    KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.RSHIFT,
                                            W_TILING,   KC.LALT,    KC.LGUI,     SPC_LSHIFT, LBLUE,      LGREEN,    ENT_RSHIFT, KC.RCTL,    COPY,       PASTE, 
    ],
    # BLUE (movement)
    [
        KC.TRNS,    KC.ESC,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.PGUP,    KC.BSPC,    KC.UP,      KC.DEL,     KC.PGDOWN,  KC.TRNS,
        KC.TRNS,    SHFT_TAB,   KC.TAB,     KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.HOME,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.END,     KC.TRNS,
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    SHFT_TAB,   KC.TAB,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    # GREEN (symbols)
    [
        KC.TRNS,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,                                                    KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.MINUS,   KC.PLUS,    KC.TRNS,
        KC.TRNS,    KC.QUOTE,   KC.DQUO,    KC.BSLASH,  KC.LPRN,    KC.LCBR,                                                    KC.RCBR,    KC.RPRN,    KC.SLSH,    KC.UNDS,    KC.EQL,     KC.TRNS,
        KC.TRNS,    KC.GRAVE,   KC.TILD,    KC.PIPE,    KC.LBRC,    KC.LABK,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.RABK,    KC.RBRC,    KC.COMM,    KC.DOT,     KC.QUES,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    # RED (numbers and F*)
    [
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,                                                      KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.TRNS,
        KC.TRNS,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                                                      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.TRNS,
        KC.TRNS,    KC.F11,     KC.F12,     KC.F13,     KC.F14,     KC.F15,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.F16,     KC.F17,     KC.F18,     KC.F19,     KC.F20,     KC.TRNS,
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

abc = {c: getattr(KC, c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
n123 = {c: getattr(KC, f"N{c}") for c in "1234567890"}
f123 = {c: getattr(KC, f"F{c}") for c in range(1, 35)}
move = {
    "↲": KC.ENT,
    "↑": KC.UP,
    "↓": KC.DOWN,
    "←": KC.LEFT,
    "→": KC.RIGHT,
    "⇞": KC.PGUP,
    "⇟": KC.PGDOWN,
    "⇱": KC.HOME,
    "⇲": KC.END,
    "␈": KC.BACKSPACE,
    "␡": KC.DEL,
}
L = {"A"}
