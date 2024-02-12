Random generates a random number.

At least that's what it should do but declaring it normally won't cause it to be truly random.
```c#
Random r = new Random();  // Not that random
```

Instead, try seeding the random using:
```c#
Random r = new Random(Guid.NewGuid().GetHashCode());
```
This also isn't truly random, but it is a closer approximation.