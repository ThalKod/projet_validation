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


