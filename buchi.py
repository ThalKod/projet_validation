import copy

#TODO complete buchi
class buchiSemantics():
    def __init__(self, initial,delta,predicate):
        self.initial = initial
        self.delta = delta
        self.predicate = predicate

    def initialConfigurations(self):
        return [self.initial]

    def enabledActions(self, i, conf):
        actions = []
        for a in self.delta[conf]:
            if a[0](i):
                actions.append(a)
        return actions

    def execute(self, source,action):
        t = copy.deepcopy(source)
        action.execute(t)
        return [t]


semantic = buchiSemantics()