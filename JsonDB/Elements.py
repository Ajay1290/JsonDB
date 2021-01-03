class List(type([])):
    
    def __init__(self):
        pass


class Node(type({})):
    
    def __init__(self):
        pass


class Dict(Node):
    
    def __init__(self, default=None , nullable=True):
        pass