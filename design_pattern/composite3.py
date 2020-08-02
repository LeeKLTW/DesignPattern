# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError("You should implement this!")


class CompositeGraphic(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def render(self) -> None:
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self) -> None:
        print(f"Ellipse: {self.name}")


if __name__=="__main__":
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")
    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()
    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)
    graphic = CompositeGraphic()
    graphic.add(graphic1)
    graphic.add(graphic2)
    graphic.render()
    # Ellipse: 1
    # Ellipse: 2
    # Ellipse: 3
    # Ellipse: 4