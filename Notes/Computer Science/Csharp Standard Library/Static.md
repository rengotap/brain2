## What It Is

Static is a modifier that states that an object or member can't be instantiated. Static members have only one copy of the member, regardless of instance. That means that static values belong to the type rather than the object.

If multiple instances of a class are created,  the last updated value of a static member will be available to all instances of that class. Static classes are sealed (you can't inherit other classes from intance classes)

Static functions can't capture local variables or instance state. 
A static local function can't capture local variables or instance state.


## How to Use It

A static class cannot be instantiated. All members of a static class are static and are accessed via the class name directly, without creating an instance of the class.

```c#
public class MyBaseC
{
    public struct MyStruct
    {
        public static int x = 100;
    }
}
```
To refer to static member x the full name must be used.

```C#
Console.WriteLine(MyBaseC.MyStruct.x);
```

If `static` is applied to a class, all members of the class must be `static`
[[Classes]], [[Interfaces]], and static classes can have static constructors.

## When to Use It

>"Does it make sense to call this method, even if no object has been constructed yet?" If so, it should definitely be static.

Static classes provide an easy way to access methods that do not need to work differently for different objects (EX: a mathematical operation)

Create a pure function. The only thing it depends upon is its parameters, no instance quirks.