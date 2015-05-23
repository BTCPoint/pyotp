import random

from pyotp.otp import OTP
from pyotp.hotp import HOTP
from pyotp.totp import TOTP
from . import utils

VERSION = '1.3.0'


def random_base32(length=16, r=random.SystemRandom(),
                  chars=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')):
    return ''.join(
        r.choice(chars)
        for _ in range(length)
    )
