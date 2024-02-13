## Definition
Unit testing is a bug fixing method that test a small "unit" before its integrated into a larger system

#### Unit
A unit is typically a method or function. Unit testing is performed on a single unit of code, isolated frim its dependencies. Each unit should have multiple tests with both typical and atypical inputs

## Unit Test Parts
**Arrange** - Declares and instantiates variables for input and output
	ex: declaring vars
**Act** - Executes the unit being tested
	ex: calling a method that is being tested
**Assert** - A belief that if not true, indicates a failed test
	ex: 2+2 should equal 4.  If 2+2 != 4, the test should fail.

An example unit test in C# xUnit:
```C#
[Fact]
public void TestAdding2And2()
{
    // Arrange: Setup inputs and unit being tested
    double a = 2;
    double b = 2;
    double expected = 4;
    Calculator calc = new();

    // Act: Execute the function to test
    double actual = calc.Add(a, b);

    // Assert: Compare expected to actual results
    Assert.Equal(expected, actual);
}
```

> In Visual Studio the [[Hotkeys||hotkey]] to run all unit tests is <kbd>Ctrl</kbd>+<kbd>R</kbd>,<kbd>A</kbd>