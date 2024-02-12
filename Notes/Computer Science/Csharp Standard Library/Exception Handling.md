## Catching all Exceptions
```C#
try 
{
	// Unsafe Code
} 
catch (Exception ex)
{
	// Error Handling
	WriteLine($"{ex.GetType()} says {ex.Message}");
}
```

## Catching Specific Exceptions
```C#
try
{
	// Unsafe Code
}
catch (FormatException)
{
	WriteLine("The number you entered is not a valid number format.");
}
catch (Exception ex) {
	WriteLine($"{ex.GetType()} says {ex.Message}");
}
```