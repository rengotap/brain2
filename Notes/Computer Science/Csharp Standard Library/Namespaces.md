## Definition

The namespace keyword declares a scope that contains a set of related classes.
## Characteristics
C# imports by namespace, not by [[Classes||class]].
```C#
using MyNamespace;  // local import of a namespace
using System.Linq;
```

As of .NET 6 / C# 10, the global modifier can be included in a namespace import.
```C#
global using MyNamespace;  // global import of a namespace
global using System.Linq;
```
To improve code readability, consider putting global namespace imports in a separate file such as `GlobalImports.cs`


## Implicitly Imported Namespaces by SDK

The following namespaces are implicitly imported in the `<ProjectName>.GlobalUsings.g.cs` file. It can be found under `obj\Debug\net8.0` in the [[Solution Explorer]].
	side note: the .g in `<filename>.g.cs` implies that the file was automatically to differentiate it from human written files.

#### Microsoft.NET.Sdk
```C#
System
System.Collections.Generic
System.IO
System.Linq
System.Net.Http
System.Threading
System.Threading.Tasks
```

#### Microsoft.NET.Sdk.Web
Same as Microsoft.NET.Sdk, plus:
```C#
System.Net.Http.Json
Microsoft.AspNetCore.Builder
Microsoft.AspNetCore.Hosting
Microsoft.AspNetCore.Http
Microsoft.AspNetCore.Routing
Microsoft.AspNetCore.Configuration
Microsoft.AspNetCore.DependencyInjection
Microsoft.AspNetCore.Hosting
Microsoft.AspNetCore.Logging
```

#### Microsoft.NET.Sdk.Worker
Same as Microsoft.NET.Sdk, plus:
```C#
Microsoft.Extentions.Configuration
Microsoft.Extentions.DependencyInjection
Microsoft.Extentions.Hosting
Microsoft.Extentions.Logging
```

>These can be disabled by removing he `<ImplicitUsings>` element from the project file OR by changing its value to disabled like so: `<ImplicitUsings>disabled</ImplicitUsings>`