## Definition
The Null Coalescing replaces null pointers with a default value.

## The "??" Operator
>`<value a> ?? <value b>` : returns value `a` if `a` is not null. Otherwise it returns value `b`.
>	`a` can be a nullable type. 
>	`b` must be non nullable.

Example:
```C#
string a = null;
string b = "foo";

Console.WriteLine(a ?? b);  // outputs "Foo"
Console.WriteLine(a);  // outputs null
```
## The "??=" Operator
> `<value a> ??= <value b>` :  assigns the value `b` to value `a` if the value of `a` is null.
>	`a` can be a nullable type. 
>	`b` must be non nullable.

Example:
```C#
string a = null;
string b = "foo";

Console.WriteLine(a ?? b);; // outputs "Foo";
Console.WriteLine(a);  // outputs "Foo";
```

Adding an exclamation point after an input is called the null forgiving operator. It doesn't do anything at runtime, but disables the compiler warning about null.