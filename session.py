import jsons as jsons

from database import Graph


class Session(object):

    def __init__(self, root):
        self.root = root
        self.nodes = [root]
        self.waiting_for_answer = False

    def restart(self):
        self.nodes = [self.root]
        self.waiting_for_answer = False

    def ask(self):
        if self.waiting_for_answer:
            return print_question(self.current_node)
        elif len(self.nodes) == 0:
            return None

        self.current_node = self.nodes.pop()
        self.waiting_for_answer = True

        return print_question(self.current_node)

    def answer(self, answer):
        if self.waiting_for_answer:
            self.nodes.append(self.current_node.get_next_node())

            if self.current_node.type == 'multi':
                for i in answer.split(','):
                    i = i.strip()
                    self.nodes.append(self.current_node.get_next_node(i))

            self.nodes = [x for x in self.nodes if x is not None]
            self.waiting_for_answer = False

    def is_terminal(self):
        return len(self.nodes) == 0


# TODO: should be a member of Question class
def print_question(question):
    answers = "({})".format(", ".join(question.get_branches()))

    if len(question.get_branches()) == 0:
        answers = ""
    return "{}? {}".format(question.question, answers )



if __name__ == "__main__":
    root = Graph.get_graph()

    # write to file util
    with open("graph.json", 'w') as f:
        f.write(jsons.dumps(root))

    # simple run
    session = Session(root)
    answer = ""
    while not session.is_terminal():
        print(session.ask())
        inp = input()
        if inp != "":
            session.answer(inp)

