import urllib2

req = urllib2.Request('http://real-chart.finance.yahoo.com/table.csv?s=%5EFTSE&d=7&e=11&f=2015&g=d&a=0&b=3&c=1984&ignore=.csv')
response = urllib2.urlopen(req)
the_page = response.read()