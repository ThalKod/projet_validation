from model import TransitionRelation


class Graph(TransitionRelation):
    def __init__(self, g, iniS):
        super().__init__()
        self.g = g
        self.initialNode = iniS

    def initial(self):
        return self.initialNode

    def get(self, a):
        return self.g[a]

    def next(self, c):

        return self.g[c]
        # newV =[]
        # res=[]
        # n = 0
        # copy = c
        #
        # for i in range(len(copy)):
        #     for j in range(len(c)):
        #         if i == j:
        #             if copy[i] == 0:
        #                 n = 1
        #             else:
        #                 n = 0
        #             newV.append(n)
        #         else:
        #             newV.append(c[j])
        #     res.append(newV)
        #     newV = []
        # return res



    def roots(self):
        return self.initialNode





