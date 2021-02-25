class Nodes(object):
    """
    defines Petri-net elements
    used to declare a model
    """
    PLACE = 'place'
    TRANSITION = 'transition'


class Attributes(object):
    """
    defines access rights required by a given transition
    """
    ROLE = 'role'


class Edges(object):
    """
    Arcs and Inhibitor Arcs connect Nodes
    """
    ARC = 'arc'
    INHIBITOR = 'inhibitor'
