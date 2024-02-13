NuGet is the package manager for Visual Studio

Packages can be added by right clicking a project in the [[Solution Explorer]] and selecting *Manage NuGet Packages*

Added packages are referenced in the .csproj project file.
```XML
 <ItemGroup>
   <PackageReference Include="Serilog" Version="3.1.1" />
 </ItemGroup>
```