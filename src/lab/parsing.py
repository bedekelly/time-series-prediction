import sexpdata


def normalise_tree(tree):

    def _normalise_tree(tree, wrap=True):
        from lab.tree import Tree

        if type(tree) is list:
            fun, *params = tree
            result = [fun.value(), *(map(_normalise_tree, params))]
        else:
            result = tree

        if wrap:
            result = Tree(result)
        return result

    return _normalise_tree(tree, wrap=False)


def parse(expression):
    return normalise_tree(sexpdata.loads(expression))
