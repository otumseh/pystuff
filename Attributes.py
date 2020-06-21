layer = iface.activeLayer()
print(layer)
all_features = layer.getFeatures()
layer.startEditing()
for feature in all_features:
    if feature['NUMBER'] == '1337':
        att = feature.attributes()
        print(att)
    else:
        print(feature['CODE'])
    if feature['NUMBER'] == '1345':
        print(feature['NUMBER'])
        feature.setAttributes(att)
        layer.updateFeature(feature)
        att = feature.attributes()
        print(att)
        
        
        
    
    