# -*- coding: utf-8 -*-

# words = ['hello', 'world']
# parts = ['<ul>']
# for w in words:
#   parts.append(f'<li>{w}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))


class HtmlElement:
  indent_size = 2

  def __init__(self, name='', text=''):
    self.name = name
    self.text = text
    self.elements = []

  def __str(self, indent):
    lines = []
    i = ' ' * (indent * self.indent_size)
    lines.append(f'{i}<{self.name}>')

    if self.text:
      i1 = ' '*((indent + 1) * self.indent_size)
      lines.append(f'{i1}{self.text}')

    for e in self.elements:
      lines.append(e.__str(indent+1))

    lines.append(f'{i}</{self.name}>')

    return '\n'.join(lines)

  def __str__(self):
    return self.__str(0)

  # call builder from its own class
  @staticmethod
  def create(name):
    return HtmlBuilder(name)


class HtmlBuilder:
  __root = HtmlElement()

  def __init__(self, root_name):
    self.root_name = root_name
    self.__root.name = root_name

  # the build function
  def add_children(self,child_name,child_text):
    self.__root.elements.append(HtmlElement(child_name,child_text))

  # ! return self to call it fluently
  def add_children_fluent(self,child_name,child_text):
    self.__root.elements.append(HtmlElement(child_name,child_text))
    return self

  def __str__(self):
    return str(self.__root)

  def clear(self):
    self.__root = HtmlElement(self.root_name)


if __name__ == '__main__':
  builder = HtmlElement.create('ul')
  builder.add_children_fluent('li','hello').add_children_fluent('li','world')
  print(builder)