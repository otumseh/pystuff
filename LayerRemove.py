layer = iface.activeLayer()
#QgsProject.instance().removeMapLayers( [layer.id()] )
structures = layer.getFeatures()
data_prov_struct = layer.dataProvider()
for structure in structures: 
    print(structure['NUMBER'])    