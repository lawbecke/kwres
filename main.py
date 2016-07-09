import urllib2

URL = "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&PriceMax=500000&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-80.96712875366207&LongitudeMax=-79.67211532592769&LatitudeMin=43.127442225395875&LatitudeMax=43.68614055675253&SortOrder=A&SortBy=1&viewState=l&Longitude=-80.4928283691406&Latitude=43.4464569091797&CurrentPage=1&PropertyTypeGroupID=1"

# You need to do this, or https connections fail in mysterious ways.
import socket

response = urllib2.urlopen(URL)
print response.info()
html = response.read()
response.close()
