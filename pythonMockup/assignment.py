class Assignment:

    def __init__(self, title, text, due):
        self.title = title
        self.text = text
        self.due = due # due date in seconds since the epoch

    def __eq__(self, other):
        return self.due == other.due

    def __ne__(self, other):
        return self.due != other.due

    def __lt__(self, other):
        return self.due < other.due

    def __gt__(self, other):
        return self.due > other.due

    def __le__(self, other):
        return self.due <= other.due

    def __ge__(self, other):
        return self.due >= other.due



    def __repr__(self):
        return "Assignment: {0} - Due: {1}".format(self.title, self.due)

    def getTitle(self):
        return self.title

    def getText(self):
        return self.text

    def getDueDate(self):
        return self.due



