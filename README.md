(Creational, structural or behavioral)

# Creational patterns
- [ ] Abstract Factory pattern
- [ ] Factory* pattern
- [ ] Builder pattern


# Structural patterns
- [ ] Adapter   pattern
- [x] Decorator pattern
- [ ] Bridge pattern
- [ ] Facade    pattern


# Behavior patterns
- [ ] The chain of Responsibility pattern
- [ ] Command   pattern
- [ ] [Observer  pattern](#observer-pattern)
- [ ] State     pattern


# Other
- [x] Iterator  pattern, Generator  pattern
- [ ] Strategy  pattern
- [ ] Singleton pattern
- [ ] Template  pattern
- [ ] Flyweight pattern
- [ ] Composite pattern


--------
# Note
## Observer pattern
when we want to inform/update one or more objects (observers/subscribers) about a change that happened on a given object (subject/publisher/observable)

e.g.
1. Kivy, the Python Framework for developing user interfaces, has a module called Properties, which implements the Observer pattern.
2. The [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-three-python.html) library can be used to add asynchronous messaging support to an application. Several messaging protocols are supported, such as HTTP and AMQP. RabbitMQ can be used in a Python application to implement a publish-subscribe pattern

MVC is an architecture and Observer Pattern is an design pattern. They look similar because MVC uses the observer pattern.