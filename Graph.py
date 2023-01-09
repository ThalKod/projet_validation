from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class Graph(TransitionRelation):
    def __init__(self, g, iniS):
        super().__init__()
        self.g = g
        self.iniS = iniS

    def initial(self):
        return self.iniS

    def get(self, a):
        return self.g[a]

    def next(self, c):


    def roots(self):
        return self.iniS
        pass



class NBits(TransitionRelation):
    def __init__(self, g, iniS):
        super().__init__()
        self.g = g
        self.iniS = iniS


    #
    def next(self, vect):
        nb_bits = len(vect)
        res = []

        for bit in vect:
            inv_bit = not bit
            res.append()


