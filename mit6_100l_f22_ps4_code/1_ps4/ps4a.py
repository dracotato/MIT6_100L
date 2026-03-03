# Problem Set 4A
# Name: dracotato
# Collaborators: N/A

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(
    5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))
)


# Custom functions
# ----------------


def is_leaf(node):
    return not any([node.get_left_child(), node.get_right_child()])


def find_tree_height(tree):
    """
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    """

    # base
    if is_leaf(tree):
        return 0

    # recursion
    return (
        max(
            find_tree_height(tree.get_left_child()),
            find_tree_height(tree.get_right_child()),
        )
        + 1  # count this node
    )


def is_heap(tree, compare_func):
    """
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    """
    # base
    if is_leaf(tree):
        return True

    # recursion (not the for loop)
    for child in [tree.get_left_child(), tree.get_right_child()]:
        if child:
            if not compare_func(child.get_value(), tree.get_value()):
                return False  # no need for any more checks
            elif not is_heap(child, compare_func):
                return False

    # All of the above passed
    return True


if __name__ == "__main__":
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
