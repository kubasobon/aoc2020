import string
import re


class TreeNode:
    def __init__(self, name):
        self.name = name  # str
        self.parents = set()  # TreeNode
        self.children = {}  # TreeNode: count

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash((self.name))

    def nested_bags(self):
        total = 1
        for node, count in self.children.items():
            total += count * node.nested_bags()
        return total


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

    bag = bags["shiny gold"]
    # Minus the gold bag itself
    total_nested_bags = bag.nested_bags() - 1
    print(f"A shiny gold bag has to contain {total_nested_bags} bags")
