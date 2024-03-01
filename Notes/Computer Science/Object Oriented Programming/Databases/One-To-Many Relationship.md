## Definition
A one-to-many relationship occurs when one [[Record]] in a [[Table]] can be associated with one or more records in another table.

> Example: A business has many employees, but the employees all work for a single business.

## Implementation
The way to implement this is to include a [[Foreign Key]] in the many sided table pointing at the [[Primary Key]] of the one sided table.