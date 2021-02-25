"""
counter model

Provides uint counters [P0,P1]
"""


NOLIMIT = 0
""" set max capacity for both counters """


def v1(role, cell, fn):

    user = role("default")

    dec0 = fn("dec0", role=user)  # --p[0]
    dec1 = fn("dec1", role=user)  # --p[1]

    p00 = cell("P0", initial=0, capacity=NOLIMIT).tx(1, dec0)  # let p[0] = 0
    p01 = cell("P1", initial=1, capacity=NOLIMIT).tx(1, dec1)  # let p[1] = 1

    fn("inc0", role=user).tx(1, p00)  # ++p[0]
    fn("inc1", role=user).tx(1, p01)  # ++p[1]
