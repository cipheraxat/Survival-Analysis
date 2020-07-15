# Nelson Aalen Estimator

This estimator is a proper non-parametric estimator of the quantity known as **cumulative hazard function**.

In lifelines, this estimator is available as the **NelsonAalenFitter**.

## Explanation Of The Plots

### NA Estimator Plot

![](https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/NA%20Estimator.png)

##### What this plot is all about ?

This is the plot representing the **Hazard Function**(H(t)), hence the rate of change of this plot will give the **commulative hazard function**. As the rate of change or 
we can say slope of this curve is high in the beginning, a little bit uniform in between and increases again after the duration 65. We can conclude that the Hazard Rate for 
the Techno Churn data is more at the beginning and at the end points, having some uniform and normal variation in between tenure 10-65.

### Smoothening The Hazard Plot

![](https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smooth%20NA%20Estimator.png)

Interpretation of the cumulative hazard function can be difficultve, hence we have derived a more-interpretable hazard function using a **kernel smoother**, which smoothes the difference of 
cummulative hazard function(How do we know this ? Have a look at this [insight](https://github.com/Abhijit2505/Survival-Analysis/new/master/Abhijit/Nelson%20Aalen%20Estimator#Insight). 
We use a **bandwidth** parameter to control the amount of smoothening.

### Interpretation of Bandwidth

![](https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothness%20and%20Bandwidth.png)

As you can see in the above plot, as the **Bandwidth** increases, the curve becomes smoother for the same X-axis duration. This thing can be a personal choice of choosing bandwidth
depending upon the dataset and the outputs required.

### Plotting Smoother Plots for different Column Variables

<a><img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothening%20(Dependent).png" height='400'></a>
<a><img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothening%20(Gender).png" height='400'><a>
<a><img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothening%20(PaperlessBilling).png" height='265'></a>
<a><img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothening%20(Partner).png" height='265'><a>
<a><img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Smoothening(PhoneService).png" height='265'><a>

##### Let's Explain the Plot

* **Dependent** - People who are dependent on someone, has a lower hazard rate than the non-dependent ones.
* **Gender** - Non uniform hazard rates, can't conclude anything from the Gender column, hence there is no affect on churning dure to the Gender of the customer.
* **PaperlessBilling** - Customers who prefer paperless billing has a higher hazard rate, although the change of rate is almost similar dor both the plots.
* **Partner** - Customers not having a partner has a higher hazard rate and customer having partner has a very small rate(slope) change of hazard.
* **PhoneService** - Non uniform variation, can's conclude anything except one thing that the slope variation is small.

### Insight

Have a look at the following,

<img src = "https://github.com/Abhijit2505/Survival-Analysis/blob/master/Abhijit/Nelson%20Aalen%20Estimator/NA%20Estimator%20Plots/Insight.png" height="550">

You can see how the **NA Estimator** values change after smoothening for the same duration columns, because the kernel smoother just smooths out the difference of the commulative 
hazard function or we can say it just tries to smooth the change in rate of the hazard function.
