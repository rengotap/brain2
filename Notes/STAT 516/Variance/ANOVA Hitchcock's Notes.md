## One-Way Analysis of Variance

With regression, we related two quantitative, typically continuous variables.
 Often we wish to relate a quantitative response variable with a qualitative (or simply discrete) independent variable, also called a factor.

● In particular, we wish to compare the mean response value at several levels of the discrete independent variable.

Example:  We wish to compare the mean wage of farm laborers for 3 different races (black, white, Hispanic).  Is there a difference in true mean wage among the ethnic groups?

● If there were only 2 levels, could do a:
`Two Sample T Test`

● For 3 or more levels, must use the [[Analysis of Variance (ANOVA)]].

● The Analysis of Variance tests whether the means of _t_ populations are equal.  We test:
$H_0: M_1 = M_2 = M_3$
$H_a:$ At least one equality is not satisfied (at least two population means differ)

● Suppose we have _t_ = 4 populations.  Why not test:
$H_0: M_1 = M_2$
$H_1: M_1 = M_3$
$H_1: M_1 = M_4$
with a series of t-tests?

● If each test has a = .05, probability of correctly failing to reject H0 in all 6 tests (when all nulls are true) is:
$0.95^6 = .735$
→ Actual significance level of the procedure is 0.265, not 0.05 → We will make some Type I error with probability 0.265 if all 4 means are truly equal.
## Why Analyze Variances to Compare Means?

● Look at Figure 6.1, page 248.

Case I and Case II:  Both have independent samples from 3 populations.

● The positions of the 3 sample means are the same in each case.

● In which case would we conclude a definite difference among population means m1, m2, m3?

Case I?

Case II?

● This comparison of variances is at the heart of ANOVA.

## Assumptions for the ANOVA test:

**(1) There are _t_ independent samples taken from _t_ populations having means m1, m2, …, mt .**

**(2) Each population has the same variance, s2.**

**(3) Each population has a normal distribution.**

● The data (observed values of the response variable) are denoted:

● Each sample has size _n__i_, for a total of             observations.

Example:  $Y_{47}$ = 7th observation in the 4th sample

Notation

The _i_-th level’s total:  $y_{i.}$ (sum over j)

The _i_-th level’s mean: $\bar{y_{i.}}$ 

The overall total:  $y_{..}$

The overall mean:  ![](file:///C:/Users/renat/AppData/Local/Temp/msohtmlclip1/01/clip_image004.gif)  

Estimating the variance s2

● For _i_ = 1, …, _t_, the sum of squares for each level is

$SS_i = \sum^{n_i}_{j=1}(y_{ij} - \bar{y_i.})^2$
$SS_i= \sum^{ni}_{j=1} y_{ij}^2 - \frac{Y_{i.}^2}{n_i}$

● Adding all the $SS_i$’s gives the pooled sum of squares:
$SS_p = ∑_i SS_i$

● Dividing by our degrees of freedom gives our estimate of $σ^2$:

$S^2_p = \frac{SS_p}{(∑n_i)-t}$
$S^2_p = \frac{∑_i(n_i - 1)s_i^2}{∑n_i -t}$

● Recall:  For 2-sample t-test, pooled sample variance was:

● This is the correct estimate of s2 if all _t_ populations have equal variances.

● We will have to check this assumption.

Development of ANOVA F-test

● Assume sample sizes all equal to _n_:

_n_1 = _n_2 = … = _n_t (= _n_) ← balanced data

● Suppose H0: m1 = m2 = … = mt (= m) is true.

● Then each sample mean ![](file:///C:/Users/renat/AppData/Local/Temp/msohtmlclip1/01/clip_image005.gif) has mean          and variance

● Treat these group sample means as the “data” and treat the overall sample mean as the “mean” of the group means.  Then an estimate of s2 / _n_ is:

Recall:

Consider the statistic:

● With normal data, the ratio of two independent estimates of a common variance has an F-distribution.

→ If H0 true, we expect F* has an F-distribution.

● If H0 false (m1, m2, …, mt not all equal), the sample means should be more spread out.

→

→

General ANOVA Formulas (Balanced or Unbalanced)

● We want to compare the variance between (among) the sample means with the variance within the different groups.

● Variance between group means measured by:

and, after dividing by the “between groups” degrees of freedom,

● Variance within groups measured by:

and, after dividing by the “within groups” degrees of freedom,

● In general, our F-ratio is:

● Under H0, F* has an F-distribution with:

● The total sum of squares for the data:

can be partitioned into

● The degrees of freedom are also partitioned:

● This can be summarized in the ANOVA table:

Source             df                    SS            MS                  F

Example:  Table 6.4 (p. 253) gives yields (in pounds/acre) for 4 different varieties of rice (4 observations for each variety)

![](file:///C:/Users/renat/AppData/Local/Temp/msohtmlclip1/01/clip_image007.gif)  

![](file:///C:/Users/renat/AppData/Local/Temp/msohtmlclip1/01/clip_image009.gif)

SSB =

![](file:///C:/Users/renat/AppData/Local/Temp/msohtmlclip1/01/clip_image011.gif)

SSW =

ANOVA table for Rice Data:

● Back to original question:  Do the four rice varieties have equal population mean yields or not?

H0: m1 = m2 = m3 = m4

Ha: At least one equality is not true

Test statistic:

At a = 0.05, compare to:

Conclusion:

“Treatment Effects” Linear Model:

Our ANOVA model equation:

Denote the _i_-th “treatment effect” by:

● The ANOVA model can now be written as:

● Note that our ANOVA test of:

H0: m1 = m2 = … = mt

is the same as testing:

Note:  For balanced data,

E(MSB) =                              and E(MSW) =

If H0 is true (all ti = 0):

If H0 is false: