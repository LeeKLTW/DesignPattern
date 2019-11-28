# DesignPattern

(Creational, structural or behavioral)

## schedule & overview
### Creational patterns
- [ ] Factory* pattern
- [x] Abstract Factory pattern
- [x] Builder pattern
- [ ] Lazy Evaluation
- [ ] Prototype pattern
- [x] Singleton pattern


### Structural patterns
- [ ] [Adapter pattern](#adapter-pattern)
- [x] Decorator pattern
- [x] Bridge pattern
- [x] [Facade    pattern](#facade-pattern)
- [ ] [Flyweight pattern](#flyweight-pattern)
- [ ] Composite pattern


### Behavior patterns
- [x] Iterator  pattern, Generator  pattern
- [ ] The chain of Responsibility pattern
- [x] Command   pattern
- [x] [Observer  pattern](#observer-pattern)
- [ ] [State     pattern](#state-pattern)
- [x] Template  pattern
- [x] Strategy  pattern


--------
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

--------
## Note
### SOLID principle

#### Single Responsibility principle

#### Open-closed principle

Software entities (class, modules, functions, etc.) should be open for extension, but closed for modification.
``
When a single change to a program results in a cascade of changes to dependent modules, the design smells of Rigidity. The OCP advises us to refactor the system so that further changes of that kind will not cause more modifications. If the OCP is applied well, then **further changes of that kind are achieved by adding new code, not by changing old code that already works**.
``

#### Liskov Substitution principle

#### Interface Segregation principle

#### Dependency Inversion principle


## pattern details

### Builder
- A builder is a seperate component for building an object
- Can either give builder an initializer or return it via a static function
- To make builder **fluent**, `return self`
- Different facets of an object can be built with different builders working 
tandem via a base case 


### Facade pattern

dictionary.cambridge
> the front of a building, especially a large or attractive building

providing a single, simple entry point to a complex system

Façade is also useful if you have more than one layer in your system. You can introduce one façade entry point per layer, and let all layers communicate with each other through their façades. That promotes loose coupling and keeps the layers as independent as possible.

[requests](https://2.python-requests.org/en/master/)


### Flyweight pattern

The flyweight pattern ensures that objects that share a state can use the same memory for that shared state. 
But bear in mind that premature optimization is the most effective way to create a program that is too complicated to maintain.
It is normally implemented only after a program has demonstrated memory problems


### Adapter pattern

Adapters are used to allow two preexisting objects to work together, even if their interfaces are not compatible.
Adapter pattern is similar to a simplified decorator pattern. Decorators typically provide the same interface that they replace, whereas adapters map between two different interfaces.


### Observer pattern
when we want to inform/update one or more objects (observers/subscribers) about a change that happened on a given object (subject/publisher/observable)

e.g.
1. Kivy, the Python Framework for developing user interfaces, has a module called Properties, which implements the Observer pattern.
2. The [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-three-python.html) library can be used to add asynchronous messaging support to an application. Several messaging protocols are supported, such as HTTP and AMQP. RabbitMQ can be used in a Python application to implement a publish-subscribe pattern

MVC is an architecture and Observer Pattern is an design pattern. They look similar because MVC uses the observer pattern.

### State pattern
A state machine is an abstract machine that has two key components, that is, states and transitions.

A nice feature of state machines is that they can be represented as graphs (called state diagrams)

The django-fsm package is a third-party package that can be used to simplify the implementation and usage of state machines in the Django Framework.

--------
# reference

https://github.com/faif/python-patterns
