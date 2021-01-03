import inspect

class Map:
    
    map = {}
    
    def __init_subclass__(cls, **kwargs):
        Map.map = cls.map
    
    @staticmethod
    def harvest_map():
        return Map.map

class Model:

    nodes = []
    
    def __init_subclass__(cls, **kwargs):
        Model.nodes.append(Model.harvest_attr(cls))
        
    @classmethod
    def harvest_attr(cls, c):
        attributes = inspect.getmembers(c, lambda a:not(inspect.isroutine(a)))
        attr = []
        for a in attributes:
            if not(a[0].startswith('__') and a[0].endswith('__')):
                if a[0] != 'nodes':
                    attr.append(a)
        try:
            d = { c.__tablename__ : attr }
        except Exception:
            d = { c.__name__ : attr }
        return d
    
    @staticmethod
    def harvest_nodes():
        return Model.nodes