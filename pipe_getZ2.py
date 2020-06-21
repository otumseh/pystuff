layer = iface.activeLayer()
print(layer)
all_features = layer.getFeatures()
layer.startEditing()
for pipe in all_features:
        
        if pipe['name'] == '1212_1211':
            print('found it ********\n  ')
            pipe_id = pipe.id()
            
            geom = pipe.geometry()
            line = geom.constGet() #line returns a QgsLineString object
        
            z = line.zAt(1) # z value of first vertex
            print(str(z))
            


