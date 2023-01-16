from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class IdentityProxy():
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.get.rand, attr)


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        super().__init__(operand)
        self.dict = dict

    def roots(self):
        neighbors = self.operand.roots()

    def next(self, source):
        neighbors = self.operand.next(source)


class ReplaceRootsProxy(IdentityProxy):

    def __init__(self, operand, newRoots):
        super().__init__(operand)
        self.newRoots = newRoots

    def roots(self):
        return self.newRoots


class SemanticTransitionRelation:
    def intialConfigurations(self):
        pass

    def enabledActions(self, source):
        pass

    def execute(self, action, source):
        pass


class STR2TR(TransitionRelation):
    def __init__(self, op):
        self.operand = op

    def roots(self):
        return self.operand.roots()

    def next(self, source):
        targets = []
        for a in self.operand.actions(source):
            target = self.operand.execute(source, a)
            targets.append(target)
        return targets
