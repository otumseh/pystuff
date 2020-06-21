file_name = r'C:\Users\Cary\Documents\Programming\Python\QGIS\Masters\18809\18809_US41_Marquette_Structures_CSV - Field.shp'
layer_localstruct = iface.addVectorLayer(file_name, "STRUCL", "ogr")
features = layer_localstruct.getFeatures()
k = int(0)
for feature in features:
    k += 1
print(str(k))

    