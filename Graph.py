from model import TransitionRelation


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
        newV =[]
        res=[]
        n = 0
        copy = c

        for i in range(len(copy)):
            for j in range(len(c)):
                if i == j:
                    if copy[i] == 0:
                        n = 1
                    else:
                        n = 0
                    newV.append(n)
                else:
                    newV.append(c[j])
            res.append(newV)
            newV = []
        return res



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


