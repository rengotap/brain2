
Operator: '?'

Standard Form:
 ```
<condition A> ? <returns if A is true> : <returns if A is false>
```

```c#
public string WeatherReport(float temp) 
{
	return temp < 55.7? "too cold" : "perfect weather!";
}

WeatherReport(20.5)  // output: too cold
WeatherReport(62.3)  // output: perfect weather!
```
