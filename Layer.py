filename = r"Z:/CaryH/Structure DB/18888/Master/18809_PIPEM.shp"

print(filename)
layer_masterpipe = iface.addVectorLayer(filename, "PIPEM", "ogr")
pipes = layer_masterpipe.getFeatures()

