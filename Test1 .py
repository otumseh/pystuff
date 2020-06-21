import sys
print(sys.version)
from qgis.PyQt import QtGui

fn = '/home/hal2920/WorkSSI/JeffersonShapes/Jefferson_at_Beaubien_CL.shp'

#layer = iface.addVectorLayer(fn, '', 'ogr')
#
#symbol = QgsLineSymbol.createSimple({'linestyle': 'dash', 'color': 'red'})
#layer.renderer().setSymbol(symbol)
#layer.triggerRepaint()

layer = QgsVectorLayer(fn, 'name', 'ogr')

tf1 = 'DIRECTION'
rangeList = []
opacity = 1

minVal = 0.0
maxVal = 2.0

lab = 'Group 1'

color1 = QtGui.QColor('#ffee00')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color1)
symbol.setOpacity(opacity)

range1 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range1)
#####
minVal = 2.1
maxVal = 4

lab = 'Group 2'

color2 = QtGui.QColor('#00eeff')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color2)
symbol.setOpacity(opacity)

range2 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range2)
#####
groupRenderer = QgsCategorizedSymbolRenderer('', rangeList)
groupRenderer = QgsGraduatedSymbolRenderer('', rangeList)
groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
groupRenderer.setClassAttribute(tf1)

layer.setRenderer(groupRenderer)

QgsProject.instance().addMapLayer(layer)


