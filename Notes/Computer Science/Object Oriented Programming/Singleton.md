
## Definition
A Singleton is a type of [[Design Pattern]] that restricts the instantiation of [[Classes]] to a singular instance.
Singletons ensure that objects have only one instance and provide easy access to that instance.

Easiest way to make is a sealed class with a public constructor (don't do this though, it isn't thread safe).

## Use Case
Singletons should be used when only a single instance of a class should be made available to all clients in the program. Ex: A single database object that needs to be used by different parts of the program.

Singletons are better than global variables as they do not pollute the namespace.

## Drawbacks
- Violates the Single Responsibility Principle of the [[S.O.L.I.D. Design Principles]]. It solves two issues at a time.
- It can mask bad design by allowing components of the program know too much about each other.
- It may make the code harder to unit test.
## C# Code
```C#
internal class Singleton
{
    private static Singleton instance = null;
    private static readonly object padlock = new object();

    Singleton() {}

    public static Singleton Instance
    {
        get
        {
            lock (padlock) {
                if (instance == null) {
                    instance = new Singleton();
                }
                return instance;
            }
        }
    }
    
    public Object SampleMethod() 
    {
	    return Object;
    }
}
```

The singleton can be accessed at any point using:

```C#
Object obj = Singleton.Instance.SampleMethod();
```

![[Pasted image 20240206112044.png]]