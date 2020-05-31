# DesignPattern
###### tags: `degsign_pattern` 
(Creational, structural or behavioral)

## SOLID principle
### Single Responsibility principle
A class should only have a single responsibility, that is, only changes to one 
part of the software's specification should be able to affect the specification 
of the class.

### Open-closed principle
Software entities (class, modules, functions, etc.) should be open for 
extension, but closed for modification.
``
When a single change to a program results in a cascade of changes to dependent 
modules, the design smells of Rigidity. The OCP advises us to refactor the 
system so that further changes of that kind will not cause more modifications. 
If the OCP is applied well, then **further changes of that kind are achieved by 
adding new code, not by changing old code that already works**.
``
### Liskov Substitution principle
"Objects in a program should be replaceable with instances of their subtypes 
without altering the correctness of that program." See also design by contract.

### Interface Segregation principle
"Many client-specific interfaces are better than one general-purpose interface."

### Dependency Inversion principle
One should "depend upon abstractions, [not] concretions."

--------------------------------------------------------------------------------
## pattern

- Overview
### Creational patterns
- [x] Abstract Factory pattern
- [x] [Builder pattern](#Builder-pattern)
- [ ] Factory* pattern
- [ ] Lazy Evaluation
- [ ] Prototype pattern
- [x] Singleton pattern


### Structural patterns
- [ ] [Adapter pattern](#adapter-pattern)
- [x] Bridge pattern
- [ ] Composite pattern
- [x] Decorator pattern
- [x] [Facade    pattern](#facade-pattern)
- [ ] [Flyweight pattern](#flyweight-pattern)


### Behavior patterns
- [x] Command   pattern
- [x] Iterator  pattern, Generator  pattern
- [x] [Observer  pattern](#observer-pattern)
- [ ] [State     pattern](#state-pattern)
- [x] Strategy  pattern
- [x] Template  pattern
- [ ] The chain of Responsibility pattern

- Detail
### Creational patterns

#### Builder pattern
##### Summary & TLDR
TLDR Decouples the creation of a complex object and its representation.
- A builder is a separate component for building an object
- Can either give builder an initializer or return it via a static function
- To make builder **fluent**, `return self`
- Different facets of an object can be built with different builders working 
tandem via a base case 
#### Motivation & when to use it 
#### Example

### Factory
#### Summary
TLDR Creates objects without having to specify the exact class.

#### Motivation & when to use it 
Cannot overload with same sets of arguments with different names. Or init turn into 'optional parameter of hell'
    
#### Example
Two third-party Django packages, `django-widgy`, and `django-query-builder`, use it for generating HTML pages and dynamic SQL queries

### Prototype
#### Summary & TLDR
- To implement a prototype, partially construct an object and store it somewhere
- Deep copy
- Customize
- A factory provides a convenient API for using prototype
#### Motivation & when to use it 
- We make a copy of complicated objects and customize it.(Require copy.deepcopy)
- To make it more convenient, use it with factory.
#### Example


### Singleton
#### Summary & TLDR
#### Motivation & when to use it 
A component which is instantiated only once.
#### Example

### Adapter
#### Summary & TLDR
#### Motivation & when to use it 
A construct which adapts an existing interface X to 
conform the required interface Y.
#### Example


### Bridge
#### Summary & TLDR
#### Motivation & when to use it 
Bridge prevents a 'Cartesian product' complexity explosion.
A mechanism that decouples an interface(hierarchy) from an implementation(hierarchy).
#### Example


### Facade pattern

dictionary.cambridge
> the front of a building, especially a large or attractive building

#### Summary & TLDR
providing a single, simple entry point to a complex system

#### Motivation & when to use it 
Façade is also useful if you have more than one layer in your system. 
You can introduce one façade entry point per layer, and let all layers 
communicate with each other through their façades. 
That promotes loose coupling and keeps the layers as independent as possible.
#### Example
[requests](https://2.python-requests.org/en/master/)


### Flyweight pattern
The flyweight pattern ensures that objects that share a state can use the same 
memory for that shared state. But bear in mind that premature optimization is 
the most effective way to create a program that is too complicated to maintain.
It is normally implemented only after a program has demonstrated memory problems.
#### Summary & TLDR
#### Motivation & when to use it 
#### Example



### Adapter pattern

Adapters are used to allow two preexisting objects to work together, even if their interfaces are not compatible.
Adapter pattern is similar to a simplified decorator pattern. Decorators typically provide the same interface that they replace, whereas adapters map between two different interfaces.
#### Summary & TLDR
#### Motivation & when to use it 
#### Example


### Observer pattern
MVC is an architecture and Observer Pattern is an design pattern. They look similar because MVC uses the observer pattern.

#### Summary & TLDR
#### Motivation & when to use it 
when we want to inform/update one or more objects (observers/subscribers) about a change that happened on a given object (subject/publisher/observable)

#### Example
1. Kivy, the Python Framework for developing user interfaces, 
has a module called Properties, which implements the Observer pattern.
2. The [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
library can be used to add asynchronous messaging support to an application. 
Several messaging protocols are supported, such as HTTP and AMQP. 
RabbitMQ can be used in a Python application to implement a 
publish-subscribe pattern.


### State pattern
A state machine is an abstract machine that has two key components, that is, 
states and transitions.A nice feature of state machines is that they can be 
represented as graphs (called state diagrams)

#### Summary & TLDR
#### Motivation & when to use it 
#### Example
The django-fsm package is a third-party package that can be used to simplify the implementation and usage of state machines in the Django Framework.


--------------------------------------------------------------------------------
## testing
### doctest
```
python -m doctest -v decorator.py
python -m doctest -v generator.py
```

### unittest
```
python -m unittest -v tests/test_structural.py

```

--------------------------------------------------------------------------------
## reference

https://github.com/faif/python-patterns
Mastering Python Design Patterns, By Kamon Ayeva, Sakis Kasampalis, August 2018