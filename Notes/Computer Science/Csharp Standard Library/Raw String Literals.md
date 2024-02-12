## Definition

Raw sting literals store text without the need to use escape characters. They start and end with triple quotes.

> These were only introduced in C# 11(released in November 2022) so they may not be available for certain legacy projects

```C#
string rawStringLiteral = """
						triple quotes preserve the
						spacing of the saved str. 
						""";
```

## Use Case

These are a godsend for saving xml, JSON, and yaml as strings.

Example JSON use case:
```C#
var person = new {FirstName = "Hugh", Age = 42};

string json = $$"""
				{
					"first_name": "{{person.FirstName}}",
					"age": {{person.Age}},
					"math": "{{{1+2}}}"
				}
				""";
```

The resulting JSON would look like this:
```JSON
{
	"first_name": "Hugh",
	"age": 62,
	"math": "{3}"
}
```


> The double dollar signs tell Roslyn to treat single curly braces as normal string values. Only pairs of double curly braces will be treated as a replaced/interpolated expression.