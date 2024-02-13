## Definition
Methods are code blocks that contain a series of statements. These are executed by calling the method and specifying arguments. Methods are always attached to a [[Classes||class]].

```C#
public string MyMethod(string myArgument)  // Defining a method
{
	return myArgument+"!!!";
}

string result = MyMethod("Yippie");  // calling a method

Console.WriteLine(result);  // prints "Yippie!!!"
```
## Characteristics

>Protip: Think of Methods as Verbs

#### Method Signature
The method signature is the combination of a method and its parameter list.
Ex:
```C#
public void DoSomething(int a, int b)  // a method signature
```
The generic version would be: 
`<acessibility> <return type> <method name> (<argument 1>, <argument 2>, ...etc)`

Methods can be public, private, [[Abstract]], sealed, or [[Static]].

#### Method Definition
The method definition is the code block following a method signature. It defines what the method actually does.
```C#
public void MyMethod() 
{
	// Any Code here is refered to as the method definition
}
```