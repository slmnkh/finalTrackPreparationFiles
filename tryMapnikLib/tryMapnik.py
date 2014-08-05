import mapnik
import cairo

m = mapnik.Map(15000, 15000, "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs") # end result: OpenStreetMap projection
m.background = mapnik.Color(0, 0, 0, 0)

bbox = mapnik.Envelope(-10000000, 2000000, -4000000, -19000000) # must be adjusted
m.zoom_to_box(bbox)

s = mapnik.Style()
r = mapnik.Rule()

polygonSymbolizer = mapnik.PolygonSymbolizer()
polygonSymbolizer.fill_opacity = 0.0
r.symbols.append(polygonSymbolizer)

lineSymbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1.0)
r.symbols.append(lineSymbolizer)

s.rules.append(r)
m.append_style('My Style',s)

lyr = mapnik.Layer('/home/skhokhar/workspace/trackManipulation/rsc/kml_files/test', '+init=epsg:4326')
lyr.datasource = mapnik.Ogr(file = '/home/skhokhar/workspace/trackManipulation/rsc/kml_files/test.kml', layer = '/home/skhokhar/workspace/trackManipulation/rsc/kml_files/test')
lyr.styles.append('My Style')
m.layers.append(lyr)

# mapnik.render_to_file(m,'./path.png', 'png')

myfile = open('/home/skhokhar/workspace/trackManipulation/rsc/kml_files/path.pdf', 'wb')
surface = cairo.PDFSurface(myfile.name, m.width, m.height)
mapnik.render(m, surface)
surface.finish()