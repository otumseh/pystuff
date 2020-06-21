from qgis.gui import QgsMapToolEmitPoint

def display_point( pointTool ): 

    print ('{:.4f}, {:.4f})'.format(pointTool[0], pointTool[1]))

# a reference to our map canvas 
canvas = iface.mapCanvas() 

# this QGIS tool emits as QgsPoint after each click on the map canvas
pointTool = QgsMapToolEmitPoint(canvas)

pointTool.canvasClicked.connect( display_point )

canvas.setMapTool( pointTool )