[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

When comparing the length of the pregnancy vs. the total weight of the babies, it is apparent that first babies are very slightly lighter than other babies and have slightly longer pregnancies.


```python
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

>>> -0.088672927072601743

```

```python
CohenEffectSize(firsts.prglngth, others.prglngth)

>>>0.028879044654449834

```
