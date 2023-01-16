import copy

from model import SemanticTransitionRelation


class Rule:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def execute(self, config):
        return [self.action(config)]


class SoupProgram:
    def __init__(self, ini):
        self.ini = ini
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)





class SoupSemantics(SemanticTransitionRelation):

    def __init__(self,program):
        self.program = program

    def initialConfigurations(self):
        return [self.program.ini]

    def enabledActions(self,source):
        return filter(lambda r:r.guard(source),self.program.rules)

    def execute(self,action, source):
        t = copy.deepcopy(source)
        return action.execute(t)





