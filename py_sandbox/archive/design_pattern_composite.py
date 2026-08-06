'''
Objective: practice composite design patterns, focused on being able to treat individual objects
    and composites of those objects in a uniform way

Example: Leaves are treated as parts of branches, and branches are parts of trees

source: https://refactoring.guru/design-patterns/composite/python/example
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self,parent:Component):
        self._parent = parent
    def add(self,component:Component) -> None:
        pass
    def remove(self, component:Component) -> None:
        pass
    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []
    def add(self, component:Component) -> None:
        self._children.append(component)
        component.parent = self

    def operation(self) -> str:
        res = []
        for ichild in self._children:
            res.append(ichild.operation())
        return res

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

def client_code(component: Component) -> None:
    """ The client code works with all of the components via the base interface. """
    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    """ Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes. """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")

if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)

