# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:58:06 2021
@author: umutc
"""
import json
from area import area
#function to bound box
#currently works as coord_list = multiploygon, limiter = polygon
def bbox(area_geometry, area_limiter):
    #determining area type and converting it as a readable file
    memo = 0
    if area_geometry['type'] == "MultiPolygon":
        coord_list = area_geometry['coordinates'][0][0]
        memo += 1
    elif area_geometry['type'] == "Polygon":
        coord_list = area_geometry['coordinates'][0]
        memo -= 1
    limiter = area_limiter['coordinates'][0]
    num1 = len(coord_list)
    num2 = len(area_limiter['coordinates'][0]) - 3
    #we don't need to calculate 0-0+ kind of situations because there will be no wrong position
    #example a = (a,-4), b = (b, 5) if we compare the y axis with limiter a, b will be always in the bounds.
    #if I remember or find a new situations, I'll update
    for i in range(num1):
        memo2 = 0
        for x in range(num2):
            #0-0-, x1, y1, y2(x1<x2, y1<y2 )
            if coord_list[i][0] < 0 and limiter[x][0] < 0:
                #1-1-
                if coord_list[i][1] < 0 and limiter[x][1] < 0:
                    if coord_list[i][1] < limiter[x][1]:
                        return False
                #1+1+
                elif coord_list[i][1] > 0 and limiter[x][1] > 0:
                    if coord_list[i][1] < limiter[x][1]:
                        return False
                #0-0- flagging
                if memo2 == 0 and coord_list[i][0] < limiter[x][0]:
                    return False
                elif memo2 == 1 and coord_list[i][0] > limiter[x][0]:
                    return False

            #0+0+
            elif coord_list[i][0] < 0 and limiter[x][0] > 0:
                #1-1-
                if coord_list[i][1] < 0 and limiter[x][1] < 0:
                    if coord_list[i][1] < limiter[x][1]:
                        return False
                #1+1+
                elif coord_list[x][1] > 0 and limiter[i][1] > 0:
                    if coord_list[x][1] < limiter[i][1]:
                        return False 
                #0+0+ flagging 
                if memo2 == 0 and coord_list[i][0] < limiter[x][0]:
                    return False
                elif memo2 == 1 and coord_list[i][0] > limiter[x][0]:
                    return False

            #x2, y1, y2
            if coord_list[i][0] < 0 and limiter[x + 2][0] < 0:
                #1-1-
                if coord_list[i][1] < 0 and limiter[x + 2][1] < 0:
                    if coord_list[i][1] > limiter[x + 2][1]:
                        return False
                #1+1+
                elif coord_list[i][1] > 0 and limiter[x + 2][1] > 0:
                    if coord_list[i][1] > limiter[x + 2][1]:
                        return False
                #0-0- flagging 
                if memo2 == 0 and coord_list[i][0] > limiter[x + 2][0]:
                    return False
                elif memo2 == 1 and coord_list[i][0] < limiter[x + 2][0]:
                    return False

            #0+0+
            elif coord_list[i][0] > 0 and limiter[x + 2][0] > 0:
                #1-1-
                if coord_list[i][1] < 0 and limiter[x + 2][1] < 0:
                    if coord_list[i][1] > limiter[x + 2][1]:
                        return False
                #1+1+
                elif coord_list[x][1] > 0 and limiter[i][1] > 0:
                    if coord_list[x][1] > limiter[i][1]:
                        return False
                #0+0+ flagging   
                if memo2 == 0 and coord_list[i][0] > limiter[x + 2][0]:
                    return False
                elif memo2 == 1 and coord_list[i][0] < limiter[x + 2][0]:
                    return False
            memo2 += 1 
    return [[coord_list]] if memo > 0 else [coord_list]

#function to select area 
def selected_area(lon, lat, lon2, lat2):
    if lat > lat2:
        remember = lat2
        lat2 = lat
        lat = remember
    if lon > lon2:
        remember = lon2
        lon2 = lon
        lon = remember
    cut ={
        "type": "Polygon",
        "coordinates": [
          [
            [
              lon,
              lat
            ],
            [
              lon2,
              lat
            ],
            [
              lon2,
              lat2
            ],
            [
              lon,
              lat2
            ],
            [
              lon,
              lat
            ]
          ]
        ]
        }
    return cut

#function to determine limiter geometry type and finding area of polygons in it
def data_type_area(area_json):
    while True:
        areas_total = 0
        a = input("**************************\n1 for area calculating with a limiter rectangular polygon\n**************************\n'q' for quiting\n**************************\n: ")
        if a == "1":
            try:
                lat = float(input("Latitude: "))
                lon = float(input("Longitude: "))
                lat2 = float(input("Latitude 2: "))
                lon2= float(input("Longitude 2: "))
                for data in area_json['features']:
                    if bbox(data['geometry'], selected_area(lon, lat, lon2, lat2)) != False:
                        areas_total += area(data['geometry'])
                print(f"\nTotal area is: {areas_total} m^2\n")
            except:
                print("\nError\n")
        elif a == "q":
            print("\nProgram successfully initialized\n")
            break
        else:
            print("\nYou entered wrong command\n")


#fire up file
def app_open():
    while True:
        a = input("\n**************************\n1 to proccess GeoJson file\n**************************\n'q' to quit\n**************************\n: ")
        if a == "1":
            try:
                string = input("**************************\nEnter your GeoJson file name which is in the same directory with this program and enter without '.json'\n**************************\n: ")
                string = string + ".json"
                file = open(string)
                data = json.load(file)
                data_type_area(data)
                file.close()
            except:
                print("\nFile does not exists\n")
        elif a == "q":
            print("\nProgram successfully initialized")
            break
        else:
            print("\You entered wrong command\n")
if __name__ == "__main__":
    app_open()