[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Question: Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.  
  
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for number of children under 18 in the household.  
  
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in the household.  
  
Plot the actual and biased distributions and compute their means.  
  

>> Probabilty mass function (Pmf) is another way to represent distribution, in which each value is mapped to its probability. The result is normalized, in which the probabilty of all the values add up to 1.  
  
>> To compute the actual distriution of NUMKDHH, I made a Pmf of NUMKDHH.  
  
```python
resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp['numkdhh'], label='actual')
print 'The actual mean of number of children under 18 in a household is: ', pmf.Mean()
```  
>> The actual mean of number of children under 18 in a household is:  1.02420515504  
  
>> However, it is very important to understand how your data are collected. As the above question explains, when surveying a sample by asking them direct questions of a similar nature, the sample is likely to give a biased result. That's because people in large families (or large classes) are more likely to be in your sample.  
  
>> The biased Pmf demonstrates the data if we were to record them that way. To compute the biased Pmf from the actual Pmf, you would first make a copy of the original Pmf. Then you would re-map each value to its new probabilty. Lastly, you would re-normalize, so that the probability of the values adds up to 1 once again.
  
```python
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

pmf_biased = BiasPmf(pmf, label='biased')

print 'The biased mean of number of children under 18 in a household is: ', pmf_biased.Mean()
```
>> The biased mean of number of children under 18 in a household is:  2.40367910066  

>> The difference between the actual and biased Pmfs is over 1, which is a big difference!  
  
>> You can see the results very clearly when plotted:  
  
```python
biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='family_size', ylabel='PMF')
```

