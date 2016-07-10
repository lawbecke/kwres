import requests
import string
import time

#def get_url():
#    price_max = 500000
#    longitude_min = -80.96712875366207
#    longitude_max=-79.67211532592769
#    latitude_min=43.127442225395875
#    latitude_max=43.68614055675253
#    longitude=-80.4928283691406
#    latitude=43.4464569091797
#    current_page=2
#
#    url = "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&&SortOrder=A&SortBy=1&viewState=l&PropertyTypeGroupID=1"
#
#    url += string.join([
#        "PriceMax=" + str(price_max),
#        PriceMax=500000
#LongitudeMin=-80.96712875366207
#LongitudeMax=-79.67211532592769
#LatitudeMin=43.127442225395875
#LatitudeMax=43.68614055675253
#Longitude=-80.4928283691406&
#Latitude=43.4464569091797
#CurrentPage=2
#
#    ], "&")
#
#    return url
#
#print get_url()

#r = requests.get(get_url)
#print r

URL="https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&PriceMax=500000&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-80.60938644409175&LongitudeMax=-80.02024459838863&LatitudeMin=43.31033384404341&LatitudeMax=43.576056817658994&SortOrder=A&SortBy=1&viewState=l&Longitude=-80.4928283691406&Latitude=43.4464569091797&CurrentPage=1&PropertyTypeGroupID=1"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(URL)

time.sleep(3)
source = driver.execute_script("return document.documentElement.outerHTML")

print source.encode('ascii', 'ignore')

driver.close()
