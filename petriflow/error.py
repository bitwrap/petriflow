class InvalidOutput(Exception):
    pass


class InvalidInput(Exception):
    pass


class GuardFail(Exception):
    pass


class ModelFrozen(Exception):
    pass


class InvalidArc(Exception):
    pass


class InvalidInhibitor(Exception):
    pass


class DuplicateLabel(Exception):
    pass


class UndefinedModel(Exception):
    pass


class UndefinedAction(Exception):
    pass


class UnexpectedState(Exception):
    pass


class SchemaNameCollision(Exception):
    pass
