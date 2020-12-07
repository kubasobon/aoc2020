import string
import re


class TreeNode:
    def __init__(self, name):
        self.name = name  # str
        self.parents = set()  # TreeNode
        self.children = {}  # TreeNode: count

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash((self.name))


clipper = re.compile(r"(.*?) bag(?:s|)")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = (l.strip(string.whitespace) for l in f.readlines())

    bags = {}

    for rule in data:
        # parse rule elements
        parent_name, children_joined = rule.split("contain")
        parent_name = clipper.findall(parent_name)[0].strip(string.whitespace)
        children_data = [
            ch.strip(string.whitespace + ",") for ch in clipper.findall(children_joined)
        ]

        # ensure parent
        if parent_name in bags:
            bag = bags[parent_name]
        else:
            bag = TreeNode(parent_name)

        # create parent <-> children links
        for child_data in children_data:
            if child_data == "no other":
                break
            count, name = child_data.split(" ", maxsplit=1)
            count = int(count)
            if name in bags:
                child = bags[name]
            else:
                child = TreeNode(name)
            child.parents.add(bag)
            bag.children[child] = count
            bags[child.name] = child

        bags[bag.name] = bag

    query = "shiny gold"
    bag = bags[query]
    ancestors = set()
    to_check = set()
    ancestors.update(bag.parents)
    to_check.update(bag.parents)
    while len(to_check) > 0:
        next_to_check = set()
        for item in to_check:
            for parent in item.parents:
                if parent in ancestors:
                    continue
                next_to_check.add(parent)
            if item in ancestors:
                continue
            ancestors.add(item)
        to_check = next_to_check

    print(f"A {query} bag fits into {len(ancestors)} bags")
