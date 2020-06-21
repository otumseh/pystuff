layer = iface.activeLayer()
print(layer)
all_features = layer.getFeatures()
layer.startEditing()
for pipe in all_features:
        
        if pipe['name'] == '1212_1211':
            print('found it ********\n  ')
            pipe_id = pipe.id()
            
            geom = pipe.geometry()
            line = geom.constGet()
            
            print(geom)
            
            geom = pipe.geometry().asPolyline()
            #pointX = geom.vertexAt(0).x() z = line.zAt(0)
            
            z0 = line.zAt(0)
            start_point = QgsPoint(geom[0])
            end_point = QgsPoint(geom[-1])
            print (geom[0])
            print(str(z0))
            



