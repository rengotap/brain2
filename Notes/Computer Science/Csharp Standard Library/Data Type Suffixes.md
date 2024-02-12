The data type suffix helps you explicitly tell the compiler what kind of data you're using.

## List of Data Type Suffixes

**For Integer Literals**
	U = uint
	L = long
	UL = ulong
**For Real Value Literals**
	F = float
	D = double
	M = decimal (D was already taken)
	
*Note: The lowercase version of these suffixes are also valid but should probably be avoided as l may be confused for 1.*
### The Usual Data Types

**Integer Literals**
	int: 32 bit integer
	uint: 32 bit integer, unsigned
	long: 64 bit integer
	ulong: 64 bit integer, unsigned
**Real Value Literals**
	float: 32 bit numeric with 6 digits of precision
	double: 64 bit numeric with 15 digits of precision
	decimal: 128 bit numeric with 28 digits of precision

### Why Use Suffix?
The suffix exists primarily to satisfy the *var* declaration.
By default, the compiler will treat any unspecified integer literal as an *int* and any unspecified real value as *double*.

In other words...
```c#
var x = 4;
var y = 2.7;
```
Is evaluated as...
```c#
int x = 4;
double y = 2.7
```

But using a data type suffix...
```c#
var x = 4L;
var y = 2.7F;
```
Is evaluated as...
```c#
long x = 4;
float y = 2.7;
```
