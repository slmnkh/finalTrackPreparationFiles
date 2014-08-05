import mapnik
# Setup the map
map_canvas = mapnik.Map(200, 200)
map_canvas.background = mapnik.Color('rgb(0,0,0,0)') # transparent

# Create a symbolizer to draw the points
style = mapnik.Style()
rule = mapnik.Rule()
point_symbolizer = mapnik.MarkersSymbolizer()
point_symbolizer.allow_overlap = True
point_symbolizer.opacity = 0.5 # semi-transparent
rule.symbols.append(point_symbolizer)
style.rules.append(rule)
map_canvas.append_style('GPS_tracking_points', style)

# Create a layer to hold the points
layer = mapnik.Layer('GPS_tracking_points')
layer.datasource = mapnik.Ogr(file="/home/skhokhar/workspace/trackManipulation/rsc/kml_files/test.kml", layer_by_index=0)
layer.styles.append('GPS_tracking_points')
map_canvas.layers.append(layer)

# Save the map
map_canvas.zoom_all()
mapnik.render_to_file(map_canvas, '/home/skhokhar/workspace/trackManipulation/rsc/kml_files/GPS_tracking_points.png', 'png')