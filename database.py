from Node import Node


class Graph(object):

    @staticmethod
    def get_graph():
        root = Node("when you diagnose with type 2")
        root.next(Node("what kind of doctor diagnose it").next(
            Node("what kind of treatment").set_multi()
                .branch("no medication", None)
                .branch("non insulin", Node("what non insulin do you take"))
                .branch("insulin", Node("which insulin do you take").next(
                    Node("what is the freq")
                ))
                .next(Node("do you suffer").set_multi()
                        .branch("diabit nuthrepy", Node("have you been seeing nuthrepy"))
                        .branch("diabit nuthrepy2", Node("have you been seeing nuthrepy2").set_empty_branches(['yes', 'no']).next(
                            Node("what was your last cretine value")
                        ))
                        .branch("diabit reyno", Node("have you been seeing"))
                        .branch("diabit cardio", Node("have you been seeing"))
                        .next(Node("have you have suffer from something").next(
                            Node("have you diagnose with the following").set_empty_branches(['yes', 'no']).next(
                                Node("do you follow a low sugar diet").set_empty_branches(['yes', 'no']).next(
                                    Node("how many times a week do you excersize").next(None)
                                )
                            )
                        ))
                )
        ))
        return root

