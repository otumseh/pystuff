#!/usr/bin/env python3

# import sys
# import numpy
# import pyproj
import csv
from pyproj import Proj
# set PROJ_DIR=C:\OSGeo4W64\
# pip3 install "C:\Users\Cary Hutchinson\Downloads\pyproj-2.0.1-cp37-cp37m-win_amd64.whl"
'''
EPSG:3587: NAD83(NSRS2007) / Michigan Central
EPSG:3588: NAD83(NSRS2007) / Michigan Central (ft)
EPSG:3589: NAD83(NSRS2007) / Michigan North
EPSG:3590: NAD83(NSRS2007) / Michigan North (ft)
EPSG:3592: NAD83(NSRS2007) / Michigan South
EPSG:3593: NAD83(NSRS2007) / Michigan South (ft)
UTM zone 16 and 17'''

class point_shot(object):
    def __init__(self, name):
        self.name = name
        self.epsg = str()
        self.latitude= float()
        self.longitude= float()
        self.easting= float()
        self.northing= float()
        self.elev = float()
        self.note = str()
        self.latidms= str()
        self.longdms= str()

def read_csv(csvfile, epsg):  #csvfile format: name, easting, northing, elev,note
    try:
    
        all_points = []
        with open(csvfile, mode = 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            
            p1 = Proj(init=epsg , preserve_units=True)
            for row in csv_reader:
                print(f'Row - {row}')
                new_point = point_shot(str(row[0]))
                
                new_point.easting = float(row[1])
                new_point.northing= float(row[2])
                new_point.elev = float(row[3])
                
                if len(row) >= 4:
                    new_point.note = str(row[4])
                    new_point.epsg = epsg              
                
                new_point.longitude, new_point.latitude = p1(new_point.easting, new_point.northing, inverse=True)
                lat_deg = int(new_point.latitude)
                lat_min = int(60*(new_point.latitude-lat_deg))
                lat_sec = abs(3600*(new_point.latitude-lat_deg - lat_min/60))
                lat_min = abs(lat_min)
                d = '\u00b0'
                lon_deg = int(new_point.longitude)
                lon_min = int(60*(new_point.longitude-lon_deg))
                lon_sec = abs(3600*(new_point.longitude-lon_deg - lon_min/60))
                lon_min = abs(lon_min)

                new_point.longdms= str(str(lon_deg) + d + str(lon_min) + "'" + str(f'{lon_sec:3.4f}') + '"')
                new_point.latidms= str(str(lat_deg) + d + str(lat_min) + "'" + str(f'{lat_sec:3.4f}') + '"')
                print(f"DMS = {new_point.longdms} , {new_point.latidms}")
        
                all_points.append(new_point)
        return all_points
    
                
    except Exception as inst:
            print(type(inst)) 
            print(inst.args)
            print(str(inst) + "\n Exception #51 in read csv() \n") 

def write_csv(all_points, new_file):
    with open(new_file, mode = 'w', newline = '') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['name', 'easting', 'northing', 'elev', 'note', 'longitude', 'latitude', 'longitudeDMS', 'latitudeDMS'])

            for point in all_points:
                print(f'point.name = {point.name} , Longitude = {point.longitude} DMS = {point.longdms} , {point.latidms}')
                csv_writer.writerow([point.name, point.easting, point.northing, point.elev, point.note, point.longitude, point.latitude, point.longdms, point.latidms])


if __name__ == "__main__":
    epsg = 'epsg:6499'
    csvfile = r'C:\Users\HAL4810\Desktop\Stuff\Python\CSVs\Test2.csv'
    new_file = r'C:\Users\HAL4810\Desktop\Stuff\Python\CSVs\New_RSU.csv'
    all_points = read_csv(csvfile, epsg)
    write_csv(all_points, new_file)




