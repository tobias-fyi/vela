# Chapter 01

> Applied SQL Data Analytics

* [Central Tendency](#central-tendency)
* [Dispersion](#dispersion)
* [Bivariate Analysis](#bivariate-analysis)
  * [Scatterplots](#scatterplots)
  * [Pearson Correlation Coefficient](#pearson-correlation-coefficient)
  * [Time Series](#time-series)

## Central Tendency

The most typical value for the variable.

* Mode
  * If multiple values are tied for most common: multimodal
* Mean / Avg
  * Sensitive to outliers
  * Outliers cause skew in the dataset
* Median

## Dispersion

How close together / spread out the data points are in a variable.

* Range
  * Difference between highest and lowest values
  * Sensitive to outliers
  * Doesn't provide any insight into the middle of the bunch
* Standard Deviation / Variance
  * The sqrt of the avg of the squared differences between each data point and mean
* Interquartile range
  * Difference between the first quartile and the third quartile
  * Not as sensitive to outliers

## Bivariate Analysis

### Scatterplots

Scatterplots are most useful with a smaller number of data points. If it is too crowded, try sampling ~200 data points from the population to plot.

Some things to look for in the scatterplot:

* Trends
  * Upward / downward linear trends
  * Quadratic
  * Exponential
  * Inverse
  * Logistic (like step function of sigmoid)
* Patterns
  * It is detecting changes in patterns that is often the most important thing.
  * Periodicity
* Outliers
  * In bivariate analysis, best to remove the stark outliers to reduce noise

### Pearson Correlation Coefficient

Method for quantifying linear correlation. Denoted by the letter `r`, and ranges from -1 (negative) to 1 (positive), indicating how well the plot fits a linear trend.

The key point is _linear_. This will not accurately show non-linear trends. Also, fewer data points means less robust calculation, as usual.

### Time Series
