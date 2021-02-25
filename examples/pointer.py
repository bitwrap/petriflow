"""
Pointer model
Defines valid states managing on-chain pointers to content or resources.
"""


def v1(role, cell, fn):
    user = role("default")

    rev = cell("revision")                    # track all updates
    disabled = cell("disabled", capacity=1)   # flag disabled entries
    new = cell("new", initial=1, capacity=1)  # allow create one-per-stream

    # fn0 - create()
    create = fn("create", role=user)
    new.tx(1, create)                 # only once
    create.tx(1, rev)                 # start on version 1

    # fn1 - disable()
    rm = fn("disable", role=user)
    rm.tx(1, disabled)                # no multiple disable
    rm.tx(1, rev)                     # ++revision

    # fn2 - enable()
    enable = fn("enable", role=user)
    disabled.tx(1, enable)            # remove disabled marker
    enable.tx(1, rev)                 # ++revision

    # fn3 - update()
    update = fn("update", role=user)
    disabled.guard(1, update)         # pre-condition: not disabled
    update.tx(1, rev)                 # ++revision
