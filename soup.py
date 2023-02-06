import copy

from model import SemanticTransitionRelation, inputSemanticTransitionRelation


class Rule:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def execute(self, config):
        self.action(config)


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

    def execute(self, source, action):
        t = copy.deepcopy(source)
        action.execute(t)
        return [t]


class InputSoupSemantics(inputSemanticTransitionRelation):
    def __init__(self,program):
        self.program = program
    
    def initialConfigurations(self):
        return [self.program.init]
    
    def enablesActions(self, input, source):
        return filter(lambda r: r.guard(input, source), self.program.rules)
    
    def execute(self, action, input, source):
        target = copy.deepcopy(source)
        n = action(input, target)
        return [target]


