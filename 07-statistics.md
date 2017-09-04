# Statistics

# Table of Contents

[1. Introduction](#section-a)  
[2. Why We Are Using Think Stats](#section-b)  
[3. Instructions for Cloning the Repo](#section-c)  
[4. Required Exercises](#section-d)  
[5. Optional Exercises](#section-e)  
[6. Recommended Reading](#section-f)  
[7. Resources](#section-g)

## <a name="section-a"></a>1.  Introduction

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)

Use Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) book for getting up to speed with core ideas in statistics and how to approach them programmatically. This book is available online, or you can buy a paper copy if you would like.

Use this book as a reference when answering the 6 required statistics questions below.  The Think Stats book is approximately 200 pages in length.  **It is recommended that you read the entire book, particularly if you are less familiar with introductory statistical concepts.**

Complete the following exercises along with the questions in this file. Some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

## <a name="section-b"></a>2.  Why We Are Using Think Stats 

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the [ThinkStats repository on GitHub](https://github.com/AllenDowney/ThinkStats2).  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  **You could import it, or you could write your own code to practice python and develop a deeper understanding of the concept.** 

Think Stats uses a higher degree of python complexity from the python tutorials and introductions to python concepts, and that is intentional to prepare you for the bootcamp.  

**One of the skills to learn here is to understand other people’s code.  And this author is quite experienced, so it’s good to learn how functions and imports work.**

---

## <a name="section-c"></a>3.  Instructions for Cloning the Repo 
Using the [code referenced in the book](https://github.com/AllenDowney/ThinkStats2), follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/metisgh/prework  
(Windows):  C:/ds/metis/metisgh/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/metisgh/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/metisgh/prework/ThinkStats2/code
```

---


## <a name="section-d"></a>4.  Required Exercises

*Include your Python code, results and explanation (where applicable).*

### Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

When comparing the length of the pregnancy vs. the total weight of the babies, it is apparent that first babies are very slightly lighter than other babies and have slightly longer pregnancies.


```python
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

>>> -0.088672927072601743

```

```python
CohenEffectSize(firsts.prglngth, others.prglngth)

>>>0.028879044654449834

```


### Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

When simulating the observed number of children under 18 when surveying the children themselves, the distributions are vastly different. Due to this bias, surveying may not necessarily be the best way to determine family size.

```python
resp = nsfg.ReadFemResp()

list(resp)

pmf = thinkstats2.Pmf(resp.numkdhh, label='actual numkdhh')
```

![Response_Ch3](thinkstats/images/PMF%20Actual%20vs%20Biased.png)


### Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Considering the CDF, which is quite close to a straight line, the distribution is indeed uniform.

![Response_Ch4_1](thinkstats/images/cdf-ch4.png)

Furthermore, the PMF shows equal probability for all values in the sample.

![Response_Ch4_2](thinkstats/images/pmf-ch4.png)


### Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

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


### Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

```
In order to best understand Bayes' Theorem, I've decided to take a step-by-step approach to this problem.

To begin, let's consider a sample of 10,000 pairs of siblings.

```

```python
sample = 10000
prob_identical = (1/300)
identical_twins = sample*prob_identical

identical_twins

>>> 33.333333333333336

```

There are about 33 (10,000 * 1/300) pairs of identical twins.

```python

identical_twin_bros = identical_twins/2

identical_twin_bros

>>> 16.666666666666668

```

Of those identical twins, half of them will be twin brothers.

```python

prob_fraternal = (1/125)
fraternal_twins = sample*prob_fraternal
fraternal_twins

>>> 80.0

```

There are 80 (10,000 * 1/125) pairs of fraternal twins.

```python
fraternal_twin_bros = fraternal_twins/4
fraternal_twin_bros

>>> 20.0

```

The denominator/all possible pairs of brothers that could be identical twins is the sum of fraternal twins and identical twins.

```python
total_twin_bros = identical_twin_bros + fraternal_twin_bros

total_twin_bros

>>> 36.66666666666667

```

Therefore, the probability that any given pair of twins is an identical pair of twin brothers is the total number of twin brothers divided by all twin brothers.


```python
identical_twin_bros/total_twin_bros

>>>0.45454545454545453
```

There is a 45% chance that Elvis had an identical twin.

---

### Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

Both frequentist and Bayesian statistics utilize models and data to determine and measure the relationship between variables. 

For example, linear regression can estimate the coefficients of a model that can predict the values of an outcome variable.

A Bayesian model can use prior knowledge which can come from either a previous model or industry/domain knowledge and calculate the probability that those coefficients are within a specific range.

Therefore, Bayesian statistical models use both prior knowledge and the data to determine the relationship between variables whereas frequentist statistics uses the data to determine the correlation.

However, frequentist models can use industry/domain/prior knowledge to determine what variables to include in the model. 

---

## <a name="section-e"></a>5.  Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

### Q7. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

### Q8. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

### Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
### Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
### Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

---

## <a name="section-f"></a>6.  Recommended Reading

Read Allen Downey's [Think Bayes](http://greenteapress.com/thinkbayes/) book.  It is available online for free, or you can buy a paper copy if you would like.

[<img src="img/think_bayes.png" title="Think Bayes"/>](http://greenteapress.com/thinkbayes/) 

---

## <a name="section-g"></a>7.  More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.
