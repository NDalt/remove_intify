# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default

import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

split = Split(
    split_flip=True,
    # Ferris Sweep communicates on RX position of Pro Micro pinout, requires PIO
    data_pin=board.D1,
    use_pio=True,
    uart_flip=True,
)

layers_ext = Layers()
mod_tap = ModTap()
mouse_key = MouseKeys()
media_key = MediaKeys()
keyboard.modules = [layers_ext, mod_tap, split, mouse_key, media_key]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# Mod-taps
A_SFT = KC.MT(KC.A, KC.LSFT)
SCLN_SFT = KC.MT(KC.SCLN, KC.LSFT)
X_CTL = KC.MT(KC.A, KC.LCTRL)
C_ALT = KC.MT(KC.A, KC.LALT)
COM_ALT = KC.MT(KC.COMM, KC.LALT)
DOT_CTL = KC.MT(KC.DOT, KC.LCTRL)

# Layer tap for other home row keys
S_L5 = KC.LT(5, KC.S)
D_L1 = KC.LT(1, KC.D)
F_L3 = KC.LT(3, KC.F)
J_L4 = KC.LT(4, KC.J)
K_L2 = KC.LT(2, KC.K)
L_L6 = KC.LT(6, KC.L)
SPC_L7 = KC.LT(7, KC.SPC)

# Mods
CTL_ALT = KC.LCTL(KC.LALT)

# fmt: off
keyboard.keymap = [
    [  # QWERTY
     KC.Q,  KC.W,  KC.E, KC.R,    KC.T,   KC.Y, KC.U,    KC.I,    KC.O,     KC.P,
    A_SFT,  S_L5,  D_L1, F_L3,    KC.G,   KC.H, J_L4,    K_L2,    L_L6, SCLN_SFT,
     KC.Z, X_CTL, C_ALT, KC.V,    KC.B,   KC.N, KC.M, COM_ALT, DOT_CTL,  KC.SLSH,
                         KC.0, KC.BSPC, SPC_L7, KC.1,
    ],
    [  # MOUSE
    _______,   _______, _______,   _______, _______, _______, KC.MB_LMB, KC.MW_UP, KC.MB_LMB,  _______,
    _______, KC.MB_RMB, _______, KC.MB_LMB, _______, _______,  KC.MS_LT, KC.MS_DN,  KC.MS_UP, KC.MS_RT,
    _______,   _______, _______,   _______, _______, _______,   _______, KC.MW_DN,   _______,  _______,
                               _______, _______, _______, _______,
    ],
    [  # NAVIGATION
    _______, _______, KC.PGUP, _______, _______, _______, _______, _______, _______, _______,
    KC.LEFT,   KC.UP, KC.DOWN, KC.RGHT, _______, _______, KC.LGUI, CTL_ALT,  KC.MEH, KC.HYPR,
    _______, KC.HOME, KC.PGDN,  KC.END, _______, _______, _______, _______, _______, _______,
                               _______, _______, _______, _______,
    ],
    [  # RIGHT SYMBOLS
    _______, _______, _______, _______, _______, _______, KC.UNDS, KC.PIPE, KC.QUOT, _______,
    KC.CIRC, KC.ASTR, KC.AMPR, _______, _______, KC.HASH, KC.TILD, KC.SLSH, KC.DQUO,  KC.DLR,
    _______, _______, _______, _______, _______, _______, KC.MINS, KC.BSLS,  KC.GRV, _______,
                               _______, _______, _______, _______,
    ],
    [  # LEFT SYMBOLS
    _______, KC.COLN, KC.LABK, KC.RABK, KC.SCLN, _______, _______, _______, _______, _______,
    KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN,   KC.AT, _______, _______,  KC.EQL, KC.PLUS, KC.PERC,
    _______, KC.EXLM, KC.LBRC, KC.RBRC, _______, _______, _______, _______, _______, _______,
                               KC.VOLD, _______, _______, KC.VOLU,
    ],
    [  # FUNCTION
    _______, _______, _______, _______, _______, _______, KC.F7, KC.F8, KC.F9, KC.F10,
    _______, _______, _______, _______, _______, _______, KC.F4, KC.F5, KC.F6, KC.F11,
    _______, _______, _______, _______, _______, _______, KC.F1, KC.F2, KC.F3, KC.F12,
                               _______, _______, _______, _______,
    ],
    [  # NUMBERS
    KC.SLSH,   KC.N7,   KC.N8,   KC.N9, KC.PLUS, _______, _______, _______, _______, _______,
      KC.N0,   KC.N1,   KC.N2,   KC.N3, KC.MINS, _______, _______, _______, _______, _______,
    KC.ASTR,   KC.N4,   KC.N5,   KC.N6,  KC.EQL, _______, _______, _______, _______, _______,
                               _______, _______, _______, _______,
    ],
    [  # ALWAYS AVAILABLE
    _______, _______, KC.COLN,  KC.ESC, _______, _______, _______, _______, _______,  KC.DEL,
    _______, KC.PERC, KC.SLSH,  KC.ENT, _______, KC.DF(1), KC.LGUI, _______, _______, _______,
    _______, _______, _______, KC.PERC, _______, KC.DF(0), KC.RALT, KC.RCTL, _______, KC.RESET,
                               _______,  KC.TAB, _______, _______,
    ],
    # [  # BLANK
    # _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    # _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    # _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    #                            _______, _______, _______, _______,
    # ],
]

if __name__ == "__main__":
    keyboard.go()