An interface is a contract that must be fulfilled by [[Classes]] and [[Structs]] that implement them.

An interface declares **what a class should have**
an an inheriting class defines **how it should be done**

Interfaces are preceded by a capital "I" ex: `IPrey`

```C#
interface IPrey
{
	void Flee();  // any inheriting class should be able to flee
}

interface IPredator
{
	void Hunt();  // any inheriting class should be able to flee
}

class Rabbit : IPrey
{
	public void Flee()
	{
		// the rabbit runs away
	}
}

class Hawk : IPredator
{
	public void Hunt()
	{
		// the hawk searches for small rodents to eat
	}
}

class Fish : IPrey, IPredator
{
	// INHERITING FROM BOTH INTERFACES REQUIRES THE CLASS TO IMPLEMENT BOTH.
	public void Flee()
	{
		// the fish swims away
	}
	public void Hunt()
	{
		// the fish searches for smaller fish to eat
	}
}
```