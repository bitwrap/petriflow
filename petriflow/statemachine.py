import json

from petriflow.error import *


class StateMachine(object):
    """
    Loads models as state machines
    """

    def __init__(self):
        self.places = {}
        self.transitions = {}

    def to_json(self):
        return json.dumps({
            "places": self.places,
            "transitions": self.transitions
        })

    def __str__(self):
        """ dump state machine rules """
        return {
            "places": self.places,
            "transitions": self.transitions
        }.__str__()

    def _guard_test(self, label, state, guard):
        """
        a guard is valid given that an inhibitor arc
        has targeted a place with zero tokens
        """

        for _, attr in self.places.items():
            i = attr['offset']
            if (state[i] + guard[i]) < 0:
                return

        raise GuardFail(label)

    def initial_vector(self):
        """ build the default state """
        initial = self.empty_vector()

        for _, p in self.places.items():
            initial[p['offset']] = p['initial']

        return initial

    def empty_vector(self):
        """ build empty state vector """
        return [0] * len(self.places)

    def transform(self, state, action, multiple=1):
        """ perform state transformation with vector addition """

        if multiple < 0:
            raise InvalidInput('invalid multiple %s' % multiple)

        if action not in self.transitions:
            raise InvalidInput('unknown action: %s' % action)

        t = self.transitions[action]

        for label, guard in t['guards'].items():
            self._guard_test(label, state, guard)

        out = [0] * len(self.places)
        for _, p in self.places.items():
            i = p['offset']
            n = state[i] + t['delta'][i] * multiple

            if n < 0:
                raise InvalidOutput("underflow state[%i] %s => %i" % (i, p, n))

            if 0 < p["capacity"] < n:
                raise InvalidOutput("overflow state[%i] %s => %i" % (i, p, n))

            out[i] = n

        return out, t['role']
