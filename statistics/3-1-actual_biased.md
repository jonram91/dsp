[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

When simulating the observed number of children under 18 when surveying the children themselves, the distributions are vastly different. Due to this bias, surveying may not necessarily be the best way to determine family size.

```python
resp = nsfg.ReadFemResp()

list(resp)

pmf = thinkstats2.Pmf(resp.numkdhh, label='actual numkdhh')
```

![Response_Ch3](thinkstats/images/PMF%20Actual%20vs%20Biased.png)
