from qgis.PyQt import QtGui
from PyQt5.QtGui import QColor

lyr = QgsVectorLayer("/home/hal2920/WorkSSI/JeffersonShapes/Jefferson_at_Beaubien_CL.shp","Type","ogr")
#lyr2 = QgsRasterLayer("type=xyz&url=https://mt1.google.com/vt/lyrs%3Dy%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=18&zmin=0","GEHybrid","wms")

type5 = {
    "Thru":("orange","Thru"),
    "RTOnly":("cyan","RTOnly"),
    "LTOnly":("green","LTOnly"),
    "RTandThru":("red","RTandThru"),
    "LTandThru":("blue","LTandThru")}
    
categories = []
for type,(color,label)in type5.items():
    sym = QgsSymbol.defaultSymbol(lyr.geometryType())
    sym.setColor(QColor(color))
    category = QgsRendererCategory(type,sym,label)
    categories.append(category)
field = "TYPE"

renderer = QgsCategorizedSymbolRenderer(field,categories)

lyr.setRenderer(renderer)

QgsProject.instance().addMapLayer(lyr)
#QgsProject.instance().addMapLayer(lyr2)
