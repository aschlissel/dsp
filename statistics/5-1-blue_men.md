[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS, the distribution of heights is roughly normal with parameters mu = 178cm and sigma = 7.7 cm for men, and mu = 163 cm for women and sigma = 7.3 for women. In order to join Blue Man Group, you have to be a male between 5'10 and 6'1. What percentage of the US male population is in this range? Hint: use scipy.stats.norm.cdf.

```python
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

upper_bound = dist.cdf(185.42)
lower_bound = dist.cdf(177.8)

print(upper_bound - lower_bound)
```

>> 0.342746837631

>> 34.27% of the population is between 5'10 and 6'1. (How many of them could perform and are willing to put on all that face makeup is a different story!)
