#to enter the value in days and convert in form year, month and days.

days =int ( input("enter the days :"))
year =int ( days / 360 )
month = int (( days / 30 )-(12 * year ))
days= days % 30

print (year , "year :", month ,"months :", days ,"days")
