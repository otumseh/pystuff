from qgis.PyQt import QtGui
from PyQt5.QtGui import QColor

lyr = QgsVectorLayer("/home/hal2920/WorkSSI/JeffersonShapes/Jefferson_at_Beaubien_CL.shp","Gress","ogr")

gress4 = {
    "Ingress":("orange","Ingress"),
    "Egress":("cyan","Egress"),
    'connectTO':("red","connectTO"),
    "connector":("green","connector")}
    
categories = []
for trafficdirection,(color,label)in gress4.items():
    sym = QgsSymbol.defaultSymbol(lyr.geometryType())
    sym.setColor(QColor(color))
    category = QgsRendererCategory(trafficdirection,sym,label)
    categories.append(category)
field = "GRESS"

renderer = QgsCategorizedSymbolRenderer(field,categories)

lyr.setRenderer(renderer)

QgsProject.instance().addMapLayer(lyr)