from os.path import dirname, join

from bokeh.models import Range1d
from bokeh.plotting import figure, show, output_file
from bokeh.util.dependencies import import_required

pd = import_required('pandas', 'get it suckah')

colormap = {'chemical explosion': 'orange', 'quarry blast': 'green', 'earthquake': 'violet',
            'sonic boom': 'magenta', 'explosion': 'blue', 'landslide': 'brown', 'mining explosion': 'black'}

title = "QUAKIN' IN MAH BOOTS"
p = figure(title=title)
p.xaxis.axis_label = 'Magnitude'
p.yaxis.axis_label = 'Depth'

quakes = pd.read_csv(join(dirname(__file__), 'resource/earthquakes.csv'))
p.circle(quakes['mag'], quakes['depth'], color=[colormap[x] for x in quakes['type']], fill_alpha=0.2, size=10)
p.y_range = Range1d(700, -10)

output_file("Earthquake Visualization.html", title=title)

show(p)
