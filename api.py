#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from geolocation.google_maps import GoogleMaps
g_m = GoogleMaps(api_key='AIzaSyDHODerdoNle7IxQX6DrGktpY94r0PlgU')
from osmapi import OsmApi
from postcodes import PostCoder
pc = PostCoder()
Userpc = raw_input("Enter Postcode")
pcr = pc.get(Userpc)
print "Postcode Data"
print pcr
#location = g_m.search(location=Userpc)
#locate = location.first()
#print locate.city
print pcr.lat
from police_api import PoliceAPI 
UserLat = 52.63473
UserLong = -1.137514
papi = PoliceAPI()
locate = papi.locate_neighbourhood(UserLat, UserLong) 
print "Police Data"
print locate
print locate.force
OSM = OsmApi()
#print "       "
#print "       "
#print "OSM Data"
#print OSM.NodeGet(123)



# ------
# 200
# 'application/json'
