(Creational, structural or behavioral)

# Creational patterns
- [ ] Abstract Factory pattern
- [ ] Factory* pattern
- [ ] Builder pattern
- [ ] Singleton pattern


# Structural patterns
- [ ] Adapter   pattern
- [x] Decorator pattern
- [ ] Bridge pattern
- [ ] Facade    pattern
- [ ] Flyweight pattern
- [ ] Composite pattern


# Behavior patterns
- [x] Iterator  pattern, Generator  pattern
- [ ] The chain of Responsibility pattern
- [ ] Command   pattern
- [ ] [Observer  pattern](#observer-pattern)
- [ ] State     pattern
- [ ] Template  pattern
- [ ] Strategy  pattern


# Other

--------
# doctest
```
python -m doctest -v decorator.py
python -m doctest -v generator.py
```
--------
# Note
## Observer pattern
when we want to inform/update one or more objects (observers/subscribers) about a change that happened on a given object (subject/publisher/observable)

e.g.
1. Kivy, the Python Framework for developing user interfaces, has a module called Properties, which implements the Observer pattern.
2. The [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-three-python.html) library can be used to add asynchronous messaging support to an application. Several messaging protocols are supported, such as HTTP and AMQP. RabbitMQ can be used in a Python application to implement a publish-subscribe pattern

MVC is an architecture and Observer Pattern is an design pattern. They look similar because MVC uses the observer pattern.