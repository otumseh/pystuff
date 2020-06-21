layer = iface.activeLayer()
print(layer)
all_features = layer.getFeatures()
layer.startEditing()
for feature in all_features:
        print(feature['NUMBER'])
        if feature['NUMBER'] == '1003':
            print('found it ********\n  ')
            feature['SUMPDIST'] = '18.55'
            geom = feature.geometry()
            print(geom)
            new_feat = QgsFeature()
            point1 = QgsPoint(26132109.5, 644411.8, 940.600)
            #new_feat.setGeometry(point1)
            #new_pnt = QgsGeometry.fromWkt("POINTZ(26132109.5 644411.8 940.48)")
            wkt = "POINTZ(" + str(point1.x()) + " " + str(point1.y()) + " " + str(point1.z()) +")"
            new_pnt = QgsGeometry.fromWkt(wkt)
            geom.get().setX(point1.x())
            geom.get().setY(point1.y())
            geom.get().setZ(point1.z())
            feature.setGeometry(geom)
            
            layer.updateFeature(feature)
            print('feature '+feature['SUMPDIST'])
            print(str(point1.z()))
            print(str(feature.geometry().get().z()))
           
            break
layer.commitChanges()
print(str(feature.geometry().get().z()))


