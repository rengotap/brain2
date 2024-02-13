## Breakpoints
Breakpoints are used to pause the program's execution at a specified line or condition for debugging.

>Press <kbd>F9</kbd> to add or remove a breakpoint on a selected line.

Breakpoints can be made more complex by right clicking the breakpoint and selecting `Conditions`. This opens a small window this allows you to modify the breakpoint's behavior. 
#### Conditional Breakpoint
An expression can be added to a breakpoint so that the breakpoint is only triggered if the condition returns true.
#### Hit Counter
A hit counter can be added to trigger the breakpoint after it has been passed or "hit" after a certain amount of times.
#### Disable Once Hit
The breakpoint can be configured to stop triggering after it has been passed once.
#### Sequential Breakpoints
The fourth checkbox allows the breakpoint to enable only once another breakpoint has been reached. This is used for sequential debugging.

## Break Mode

> Press <kbd>F5</kbd> to start the debugger.

The debugger will pause when it reaches a breakpoint. At this point the debugging toolbar will open and several new tabs will appear as output.
#### Immediate Window/Debug Console
Enables live interaction with the code. Allows you to interrogate the code by entering the names of variables and run basic functions.
#### Locals
Shows the current name, value, and type of local variables.
#### Watch
Shows any [[Watch Expressions]] that have been defined. A watch expression can be defined by right clicking on an expression and selecting "Add Watch".
#### Call Stack
Shows the stack of function calls.
#### Exception Settings


## Debugging Toolbar

> The toolbar can be navigated using either the GUI buttons, or various [[Hotkeys]].

**Continue** ( <kbd>F5</kbd>): will cause the program to continue until it hits the next breakpoint or the program ends.

**Hot Reload**: will reload all compiled code changes without needing to restart the entire app. This is good for making minor tweaks.

**Break All**:  will break into the next available line of code. Use it to break out of loops.

**Stop** (<kbd>Shift</kbd>+<kbd>F5</kbd>): This button will stop the debugging session and return you to the editor screen.

**Restart** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F5</kbd>): This button will stop the current run and immediately restart with the debugger attached.

**Show Next Statement**: Moves the current cursor to the next statement that will execute. Good if you want to see what runs after a certain function ends.

**Step Into**(<kbd>F11</kbd>): The code progresses one line; if the line is a function call, the debugger executes the method line by line.

**Step Over**(<kbd>F10</kbd>): The code progresses one line; if the line is a function call, the method is executed in one move.

**Step Out**(<kbd>Shift</kbd>+<kbd>F11</kbd>)

**Show Threads in Source**: Allows you to examine and work with [[Threads]] in the application.
