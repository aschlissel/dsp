# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

```
Adate_start = datetime.strptime('01-02-2013', '%m-%d-%Y')
Adate_stop = datetime.strptime('07-28-2015', '%m-%d-%Y')

Adifference = Adate_stop - Adate_start
print Adifference
```

####b)  
date_start = '12312013'  
date_stop = '05282015'  

```
Bdate_start = datetime.strptime('12312013', '%m%d%Y')
Bdate_stop = datetime.strptime('05282015', '%m%d%Y')

Bdifference = Bdate_stop - Bdate_start
print Bdifference
```

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

```
Cdate_start = datetime.strptime('15-Jan-1994', '%d-%b-%Y')
Cdate_stop = datetime.strptime('14-Jul-2015', '%d-%b-%Y')

Cdifference = Cdate_stop - Cdate_start
print Cdifference
```
