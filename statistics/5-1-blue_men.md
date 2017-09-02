[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

If male heights are normally distributed, then you can use scipy's normal distribution function to simulate the US population.

```python
import scipy
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

low = 70
high = 73

```

The heights need to be converted to cm.

```python
def to_cm(inch):
    return inch*2.54

low_cm = round(to_cm(low),2)
high_cm = round(to_cm(high),2)
cdf_low = round(dist.cdf(low_cm),2)
cdf_high = round(dist.cdf(high_cm),2)

```

```python
print("Approximately {}% of men are shorter than {}cm".format(cdf_low*100,low_cm))

>>> Approximately 49.0% of men are shorter than 177.8cm

print("Approximately {}% of men are shorter than {}cm".format(cdf_high*100,high_cm))

>>> Approximately 83.0% of men are shorter than 185.42cm

print("Approximately {}% of men are between 70 inches and 73 inches".format(round(cdf_high-cdf_low,2)*100))

>>>Approximately 34.0% of men are between 70 inches and 73 inches

```

About 34% of men are eligible to join BMG.

I am part of the 66%. :cry:
