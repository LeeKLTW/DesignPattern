# -*- coding: utf-8 -*-
class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ':' + self.text
        else:
            return self.tag_name


class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None
        self.state = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)


class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1: i_end_tag]
        remaining = remaining_string[i_end_tag + 1:]

        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining


class OpenTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1: i_end_tag]
        remaining = remaining_string[i_end_tag + 1:]

        node = Node(tag_name, parser.current_node)

        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()
        return remaining


class CloseTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        assert remaining_string[i_start_tag + 1] == '/'
        tag_name = remaining_string[i_start_tag + 2: i_end_tag]
        assert tag_name == parser.current_node.name
        remaining = remaining_string[i_end_tag + 1:].strip()

        parser.current_node = parser.current_node.parent
        parser.state = ChildNode()

        return remaining


