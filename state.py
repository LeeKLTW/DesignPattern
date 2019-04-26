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
        pass

    def process(self, remaining_string):
        pass

    def start(self):
        pass

class FirstTag:
    def process(self, remaining_string, parser):
        pass

class OpenTag:
    def process(self, remaining_string, parser):
        pass

class CloseTag:
    def process(self, remaining_string, parser):
        pass

