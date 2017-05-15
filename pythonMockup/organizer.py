from pQueue import PQueue
from assignment import Assignment

class Organizer:
    def __init__(self, *args):
        self.assignments = PQueue()
        self.size = 0

        for arg in args:
            self.size += 1
            self.assignments.add(arg)

    def addAssignment(self, assignment):
        if (isinstance(assignment, Assignment)):
            self.assignments.add(assignment)
            self.size += 1

    def popAssignment(self):
        self.size -= 1
        return self.assignments.pop()
