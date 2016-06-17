[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Question: Using the variable totalweight_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?  
  
>> Cohen's *d* compares the difference between groups to the variability within groups. It is computed by subtracting the means of each group and dividing that over the pooled standard deviation. Before computing Cohen's *d*, I created a histogram comparing the frequency of values that occur in each group. The histogram showed that the weights between the two groups were very similar. With that in mind, I knew that the solution would be a small number.  
  
>> First, I created two groups of babies: first babies and babies born subsequently. Although this is done with first.py, I did it myself to practice.  
  
```python
import thinkstats2
import nsfg
import thinkplot
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
```
  
>> Then, I assigned weights to the two groups.
  
```python
weight1 = firsts.totalwgt_lb
weight2 = others.totalwgt_lb
```
  
>>After creating these variables, I plotted a histogram to help visualize the solution.
  
```python
first_hist = thinkstats2.Hist(weight1)
other_hist = thinkstats2.Hist(weight2)
width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Show(xlabel='weight', ylabel='frequency')
```
  
>> Once I knew that I was looking for a small number, I used the Cohen's weight function from ThinkStats2. The inserted comments helped me understand what the function was doing.  
  
```python
def Cohens_d(weight1, weight2):
    #subtract weight2 - weight 1 to get a positive number
    diff = weight2.mean() - weight1.mean()

    #variance: describes spread of distribution (standard deviation squared)
    #in the following steps, we are making a pooled variance to serve as the denominator
    var1 = weight1.var()
    var2 = weight2.var()

    n1, n2 = len(weight1), len(weight2)

    pooled_var = ((n1 * var1) + (n2 * var2)) / (n1 + n2)

    #we need the square root of pooled_var to arrive at the pooled standard deviation
    d = diff / math.sqrt(pooled_var)
    return d
```
  
Answer  
>> The difference in means is 0.0886729270726 standard deviations. Although it was more than the difference in means of pregnancy lengths (0.029 standard deviations), less than 0.1 standard deviations is very small. Thus, first babies are slightly lighter than other babies (remember, I subtracted weight2 from weight1 to get a positive number), but it is not by much at all.
