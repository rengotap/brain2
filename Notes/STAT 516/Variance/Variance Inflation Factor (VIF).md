A measure to detect [[Multicollinearity]].

#TODO: Change me
~~Out of your x variables, which ones could be ursed to report the others?~~

~~Can the information stored in a variable be found in the other variables in a model?~~
## Formula

> $\frac{1}{1-R^2}$

In practice, the computer will give us our VIF values.
## Characteristics

As a general rule of thumb:
$VIF = 1 \rightarrow X_{j}$ : not involved in any [[Multicollinearity]].
$VIF > 10 \rightarrow X_{j}$ : involved in severe [[Multicollinearity]].

766
LOW VIF DOES NOT IMPLY THAT SOMETHING IS A GOOD VARIABLE
However, it could be a good variable to *consider*.

Likewise, a high VIF does not imply that something is a bad variable. It could be a good variable to consider.

Accuracy is to bias as variance is to precision
Variation in y is $r^2$6666666666666666666666666666666666666666666666666666666666666666666666666666666666666556
