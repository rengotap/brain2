## Single Responsibility Principle
>Every class, module, or function should have one responsibility or function.

Separated logic is easier to understand as each core functionality has its own class. You can have as many methods as you want, but they should be linked to the responsibility of that class. This makes the code more modular/reusable and makes testing for errors easier.

Single responsibility does not mean single job. Everything it does should be very closely related.

## Open-Closed Principle
>Software entities should be open for extension but closed for modification.

Classes, [[Abstract Classes]], functions, etc. should allow core functions to be generic so they can be built upon. This lets you change a class without having to adapt all [[dependencies]]. Use [[inheritance]] or interfaces to achieve.

TCDU: If you need to add additional functionality to your program, you shouldn't be editing existing classes or methods to do so.

Related: [[Decorator Pattern]]
## Liskov Substitution Principle
>Let Φ(x) be a property provable about objects x of type T. Then Φ(y) should be true for objects y of type S where S is a subtype of T.

In normal English that means that any class that inherits/extends another class should have a use case for all the properties and behavior of that class. (A child class should be able to do everything a parent class can)

For example: A frog object could extend an Amphibian class since it can swim and walk, but a fish object would not extend an Amphibian class since it can only swim.

TLDR: Interfaces should match the needs of the inheriting class.

## Interface Segregation Principle
>Clients should not be forced to rely on methods they do not use.

Use multiple smaller interfaces instead of one large monolithic interface.
An example of bad design:
```c#
public interface IWorker() 
{
	void Work();
	void Eat();
	void Sleep();
}

public class HumanWorker : IWorker
{
	public void Work() {implementation}
	public void Eat() {implementation}
	public void Sleep() {implementation}
}
```
This would be fine for a human worker, but if I wanted to implement something like a robot worker it would be forced to implement Eat() and Sleep() which wouldn't apply to a robot.

Here is a better design:
```c#
public interface IWorkable
{
	void Work();
}

public interface IEatable
{
	void Eat();
}

public interface ISleepable
{
	void Sleep();
}
```
The improved design allows for the following:
```C#
public class HumanWorker: IWorkable, IEatable, ISleepable
{
	public void Work() {implementation}
	public void Eat() {implementation}
	public void Sleep() {implementation}
}

public class RobotWorker: IWorkable
{
	public void Work() {implementaiton}
}
```

TLDR: Keep [[Interfaces]] focused. Use multiple interfaces instead of a single big one.
## **Dependency Inversion Principle**

>High level modules should not import anything from low level modules. Both should depend on abstractions. (ex. interfaces)

It is good design to have classes rely on properties in interfaces instead of on each other. This lets us test blocks of code independently, reuse code, and reduce the complexity of the [[system]].