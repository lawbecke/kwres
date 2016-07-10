import requests
import string
import time

def get_url():
    culture_id=1
    application_id=1
    records_per_page=9
    maximum_results=9
    property_search_type_id=1
    transaction_type_id=2
    storey_range="0-0"
    bed_range="0-0"
    bath_range="0-0"
    longitude_min="-80.5202083587646"
    longitude_max="-80.46544837951656"
    latitude_min="43.43343188607223"
    latitude_max="43.459479374895054"
    sort_order="A"
    sort_by=1
    view_state="l"
    longitude="-80.4928283691406"
    latitude="43.4464569091797"
    current_page=1
    property_type_group_id=1

    url = "https://www.realtor.ca/Residential/Map.aspx#"

    url += string.join([
        "CultureId=" + str(culture_id),
        "ApplicationId=" + str(application_id),
        "RecordsPerPage=" + str(records_per_page),
        "MaximumResults=" + str(maximum_results),
        "PropertySearchTypeId=" + str(property_search_type_id),
        "TransactionTypeId=" + str(transaction_type_id),
        "StoreyRange=" + str(storey_range),
        "BedRange=" + str(bed_range),
        "BathRange=" + str(bath_range),
        "LongitudeMin=" + str(longitude_min),
        "LongitudeMax=" + str(longitude_max),
        "LatitudeMin=" + str(latitude_min),
        "LatitudeMax=" + str(latitude_max),
        "SortOrder=" + str(sort_order),
        "SortBy=" + str(sort_by),
        "viewState=" + str(view_state),
        "Longitude=" + str(longitude),
        "Latitude=" + str(latitude),
        "CurrentPage=" + str(current_page),
        "PropertyTypeGroupID=" + str(property_type_group_id)
    ], "&")

    return url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = get_url()
driver.get(url)

# TODO - check how much sleeping is required.
time.sleep(3)
source = driver.execute_script("return document.documentElement.outerHTML")

print source.encode('ascii', 'ignore')

driver.close()
