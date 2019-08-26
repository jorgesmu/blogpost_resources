# based: https://www.journaldev.com/19527/bokeh-python-data-visualization
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [i for i in range(1000)]
y0 = [i**2 for i in x]
y1 = [(i*(i+1)/2) for i in x]

# create a new plot
p = figure(
   x_axis_label='N', y_axis_label='Iterations'
)

# add some renderers
p.line(x, y0, legend="Y = N^2", line_color="red")
p.line(x, y1, legend="Y = N(N+1)/2")
# show the results
show(p)