from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class IdentityProxy():
    @abstractmethod
    def __init__(self, operand):
        self.operand = operand

    @abstractmethod
    def __getattr__(self, attr):
        return getattr(self.get.rand, attr)


class ParentTraceProxy(IdentityProxy):

    def __init__(self, operand, dict):
        self.operand = operand
        self.dict = dict

    def roots(self):
        neighbors = self.operand.roots()

    def next(self, source):
        neighbors = self.operand.next(source)


class ReplaceRootsProxy(IdentityProxy):
    @abstractmethod
    def __init__(self, operand, newRoots):
        super.__init__(operand)
        self.newRoots = newRoots

    @abstractmethod
    def roots(self):
        return self.newRoots
