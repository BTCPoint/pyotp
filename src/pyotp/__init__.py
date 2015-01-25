from pyotp.otp import OTP
from pyotp.hotp import HOTP
from pyotp.totp import TOTP
from . import utils

import base64
import random


VERSION = '1.3.0'


def random_base32(length=16, random=random.SystemRandom(),
                  chars=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')):
    return ''.join(
        random.choice(chars)
        for i in range(length)
    )
