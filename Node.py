

class Node(object):

    def __init__(self, question):
        self.question = question
        self.type = None
        self.next_node = None
        self.branches = {}

    def apply(self, answer):
        return self.branches.get(answer)

    def next(self, node):
        self.next_node = node
        return self

    def get_next_node(self, answer=None):
        if answer is not None and:
            return self.branches.get(answer)
        return self.next_node

    def branch(self, branch, node):
        self.branches.update({branch :node})
        return self

    def get_branches(self):
        return self.branches.keys()

    def set_empty_branches(self, names):
        self.branches.update({ k : None  for k in names })
        return self

    def set_multi(self):
        self.type = "multi"
        return self

