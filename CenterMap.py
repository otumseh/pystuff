from qgis.gui import QgsMapCanvas
layer = iface.activeLayer()
ex = layer.extent()
cent = iface.mapCanvas().center()

point1 = QgsPointXY(26134100.0,643792.0)
point2 = QgsPoint(26132801.0,645013.0)
rectan = QgsRectangle(26132801.0,643792.0, 26134100.0,645013.0)
iface.mapCanvas().setExtent(rectan)
iface.mapCanvas().setCenter(point1)

