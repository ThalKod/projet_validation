from model import TransitionRelation

class NBits(TransitionRelation):
    def __init__(self, roots:list, n:int):
        super().__init__()
        self.g = g
        self.iniS = iniS

    def roots(self):
        return self.initials
    # def next(self,source):
    #     newV = []
    #     res = []
    #     n = 0
    #     copy = source
    #     print(copy)
    #     for i in range(len(copy)):
    #         for j in range(len(source)):
    #             if (i == j):
    #                 if (copy[i] == 0):
    #                     n = 1
    #                 else:
    #                     n = 0
    #                 newV.append(n)
    #             else:
    #                 newV.append(source[j])
    #         res.append(newV)
    #         newV = []
    #     return res

    def roots(self):
        return self.initial


