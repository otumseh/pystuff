from qgis.PyQt import QtGui
from PyQt5.QtGui import QColor

lyr = QgsVectorLayer("/home/hal2920/WorkSSI/JeffersonShapes/Jefferson_at_Beaubien_CL.shp","DIR","ogr")
#lyr1 = QgsRasterLayer("type=xyz&url=http://a.tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0","OSM","wms")
lyr2 = QgsRasterLayer("type=xyz&url=https://mt1.google.com/vt/lyrs%3Dy%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=18&zmin=0","GEHybrid","wms")

direction4 = {
    "NB":("orange","NB"),
    "SB":("cyan","SB"),
    "EB":("green","EB"),
    "WB":("red","WB")}
    
categories = []
for direction,(color,label)in direction4.items():
    sym = QgsSymbol.defaultSymbol(lyr.geometryType())
    sym.setColor(QColor(color))
    category = QgsRendererCategory(direction,sym,label)
    categories.append(category)
field = "DIRECTION"

renderer = QgsCategorizedSymbolRenderer(field,categories)

lyr.setRenderer(renderer)

QgsProject.instance().addMapLayer(lyr)
#QgsProject.instance().addMapLayer(lyr1)
QgsProject.instance().addMapLayer(lyr2)