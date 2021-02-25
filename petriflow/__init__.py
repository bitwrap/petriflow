from petriflow.error import UndefinedAction
from petriflow.metamodel import MetaModel
from petriflow.statemachine import StateMachine


Models = {}
"""
reference to all loaded models
"""


class Model(StateMachine):
    """
    Load a given model definition as a StateMachine
    """

    def __init__(self, schema, model):
        super().__init__()
        self.schema = schema
        mm = MetaModel()
        model(mm.role, mm.cell, mm.defun)
        mm.reindex()
        self.places = mm.places
        self.transitions = mm.transitions
        global Models
        Models[schema] = self

    def action_offset(self, action):
        """ lookup action index by name """
        if action not in self.transitions:
            raise UndefinedAction(action)

        return self.transitions[action]['offset']
