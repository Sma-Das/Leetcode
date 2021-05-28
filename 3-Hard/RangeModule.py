class RangeModule:
    def __init__(self):
        self.range = set()

    def addRange(self, left: int, right: int) -> None:
        self.range.update(range(left, right))

    def queryRange(self, left: int, right: int) -> bool:
        return self.range.issuperset(range(left, right))

    def removeRange(self, left: int, right: int) -> None:
        self.range.difference_update(range(left, right))
