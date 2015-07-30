#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import responses
import cgi
from postcodes import PostCoder
from geolocation.google_maps import GoogleMaps
g_m = GoogleMaps(api_key='AIzaSyAGwOOqFQPqt6xyG3UPVkh9dXGeNN4_kpg')
#gmaps = googlemaps.Client(key='AIzaSyAGwOOqFQPqt6xyG3UPVkh9dXGeNN4_kpg')
#from osmapi import OsmApi

pc = PostCoder()
#Userpc = raw_input("Enter Postcode")
print "Content-Type: text/html"
print
print """
<html>
  <head>
<style>
body {
  background-color: #d3d3d3;
  margin: 0 15%;
  font-family: Roboto;
  }
h1 {
  background-color: #4169E1;
  text-align: center;
  color: #ffffff;
  font-family: Roboto Condensed;
  font-weight: Bold;
  border-bottom: 20px solid #4169E1;
  margin-top: 10px;
  } 
h2 {
  font-family: Roboto Condensed;
  font-weight: normal;
  border-bottom: 6px solid #610000;
  }
 h3 {
  font-family: Roboto Condensed;
  font-weight: normal;
  border-bottom: 6px solid #4169E1;
  } 
</style>
</head>
    <h1> Here is Some Stuff</h1>
   <h2> Enter Postcode </h2>
   <form method="post" action="webapi.py">
            <p>command: <input type="text" name="command"/></p>
        </form>


"""
form = cgi.FieldStorage()
Userpc = form["command"].value
if command != "" :
     print "<p> Finding Data For Postcode" + Userpc + "</p>" 
pcr = pc.get(Userpc)
pcr2 = pcr["geo"]
UserLat = pcr2["lat"]
UserLong = pcr2["lng"]
location = g_m.search(location=Userpc)
#locate = location.first()
#print locate.city
print location
from police_api import PoliceAPI 
papi = PoliceAPI()
locate = papi.locate_neighbourhood(UserLat, UserLong) 
print "Police Data for" + Userpc
#print "<h2>" + locate + "</h2>"
print "<h2> Force </h2<"
print "<h2> Contact details </h2> "
print  
print "<h3>" + locate.force + "</h3>"
print "<h3>" + papi.get.crimes.area + "</h3>"
#OSM = OsmApi()
#print "       "
#print "       "
#print "OSM Data"
#print OSM.NodeGet(123)




# ------
# 200
# 'application/json'
