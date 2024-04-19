# What are design patterns?

Design patterns are typical repeatable solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.


# Interfaces in python

An interface defines a contract between a class and its users. It specifies a set of methods that a class must implement in order to be considered compatible with the interface. In Python, interfaces can be implemented using abstract base classes (ABCs).

For example, suppose we have a Shape interface that specifies a single method, area(). We can define the Shape interface in Python using the abc module as follows:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

Now, any class that implements the Shape interface must provide an implementation of the area() method.

## Implementing interfaces in Python
To implement an interface in Python, we create a class that inherits from the interface’s abstract base class. We then provide implementations for all the required methods.

For example, suppose we want to implement the Shape interface for a Rectangle class. We can do so as follows:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
Notice that we didn’t explicitly inherit from the Shape interface. Instead, we provided an implementation of the area() method, which is all that’s required to be compatible with the Shape interface.

# What is an abstract class?
An abstract class is a class that cannot be instantiated directly. Instead, it’s intended to be subclassed by other classes that provide concrete implementations of its abstract methods. Abstract classes are useful for defining a common interface for a group of related classes.

For example, suppose we have a Vehicle abstract class that defines a common interface for all types of vehicles. We can define the Vehicle abstract class in Python using the abc module as follows:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass

Now, any class that inherits from the Vehicle abstract class must provide concrete implementations of the start_engine(), stop_engine(), accelerate(), and brake() methods.

## Implementing abstract classes in Python
To implement an abstract class in Python, we create a subclass that inherits from the abstract class and provides concrete implementations of its abstract methods.

For example, suppose we want to implement the Vehicle abstract class for a Car class. We can do so as follows:

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine...")
    
    def stop_engine(self):
        print("Stopping car engine...")
    
    def accelerate(self):
        print("Accelerating car...")
    
    def brake(self):
        print("Applying car brakes...")
Notice that we provided concrete implementations of all the abstract methods defined in the Vehicle abstract class.

# Differences between interfaces and abstract classes
Interfaces and abstract classes have some similarities, but there are also some key differences. Interfaces focus on defining a contract between a class and its users, while abstract classes focus on defining a common interface for a group of related classes.

In general, interfaces cannot define any implementation, while abstract classes can define both abstract methods and concrete methods. This means that interfaces are more restrictive than abstract classes.

Another difference between interfaces and abstract classes is that a class can implement multiple interfaces, but it can only inherit from a single abstract class. This makes interfaces more flexible than abstract classes in terms of class design.

# When to use interfaces and abstract classes
Interfaces are useful when you want to define a contract between a class and its users. They’re particularly useful for defining APIs and ensuring that classes are compatible with each other.

Abstract classes, on the other hand, are useful when you want to define a common interface for a group of related classes. They’re particularly useful for implementing a template method pattern, where the abstract class defines a skeleton for an algorithm and the concrete subclasses provide specific implementations for each step.

# Creational Design Pattern

These patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

## Singleton Design pattern

A class of which only a single instance can exist. Its aim is to ensure a class is instantiated only once and has a global point of access to it. 

Consider using this pattern when:

1. No clear owner of the object, ie global object
2. Lazy instantiation (only instantiate object when needed) helps performance
3. Need a single global way to access the object

## Global object Pattern

When developing applications, especially those of considerable complexity, we often find ourselves in scenarios where we need to share an object's state across different parts of the system. While global variables can serve this purpose, they're generally frowned upon due to the complications and unpredictability they can introduce.

Instead, the Global Object Pattern presents a more controlled and elegant solution to this dilemma. At its core, this pattern aims to provide a singular shared instance of an object across the entire application, ensuring that the state remains consistent and synchronized.

The Global Object Pattern typically leverages the Singleton pattern (which we explained earlier in this lesson) to ensure a class has only one instance and provides a global point to access it. The main advantage of using this pattern is the control and predictability it offers. Changes made to the global object from one module will reflect in all others, ensuring synchronized behavior.

## The factory and abstract factory pattern

Factory method is specified in base class and implemented in derived classes. Factory method is capable of creating several derived classes. It defines an interface for creating objects but lets the subclasses decide which class to instantiate.

Abstract factory pattern leads to creation of instance of several families of classes.This is often used to encapsulate platform dependencies.

## Builder Pattern

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called builders. The Builder pattern lets you construct complex objects step by step. The Builder doesn't allow other objects to access the product while it's being built.

## Object Pool Pattern

Object pool pattern is a software creational design pattern which is used in situations where the cost of initializing a class instance is very high. 

Basically, an Object pool is a container which contains some amount of objects. So, when an object is taken from the pool, it is not available in the pool until it is put back.

# Structural design pattern

These patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

## Adapter pattern

Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate. 
An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes. The wrapped object isn’t even aware of the adapter. For example, you can wrap an object that operates in meters and kilometers with an adapter that converts all of the data to imperial units such as feet and miles.

Adapters can not only convert data into various formats but can also help objects with different interfaces collaborate. Here’s how it works:

The adapter gets an interface, compatible with one of the existing objects.
Using this interface, the existing object can safely call the adapter’s methods.
Upon receiving a call, the adapter passes the request to the second object, but in a format and order that the second object expects.

## Decorator Pattern

Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors. 
It is much easier to implement Decorator Method in Python because of its built-in feature. It is not equivalent to the Inheritance because the new feature is added only to that particular object, not to the entire subclass.

## Facade Pattern

Facade Method is a Structural Design pattern that provides a simpler unified interface to a more complex system. The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems. It is an essential part Gang of Four design patterns. It provides an easier way to access methods of the underlying systems by providing a single entry point.

Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes but all the tasks separately. As the whole system is quite complex, we need to abstract the complexities of the subsystems. We need a system that can automate the whole task without the disturbance or interference of us. 

## Proxy Pattern

The Proxy method is Structural design pattern that allows you to provide the replacement for an another object. Here, we use different classes to represent the functionalities of another class. The most important part is that here we create an object having original object functionality to provide to the outer world.
The meaning of word Proxy is “in place of” or “on behalf of” that directly explains the Proxy Method.

Proxies are also called surrogates, handles, and wrappers. They are closely related in structure, but not purpose, to Adapters and Decorators.

A real-world example can be a cheque or credit card is a proxy for what is in our bank account. It can be used in place of cash and provides a means of accessing that cash when required. And that’s exactly what the Proxy pattern does – “Controls and manage access to the object they are protecting“.

## Flyweight pattern

Flyweight method is a Structural Design Pattern that focus on minimizing the number of objects that are required by the program at the run-time. Basically, it creates a Flyweight object which is shared by multiple contexts. It is created in such a fashion that you can not distinguish between an object and a Flyweight Object. One important feature of flyweight objects is that they are immutable. This means that they cannot be modified once they have been constructed.
To implement the Flyweight method in Python, we use Dictionary that stores reference to the object which have already been created, every object is associated with a key.
