# based: https://www.journaldev.com/19527/bokeh-python-data-visualization
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [i for i in range(20000)]
y0 = [i**2 for i in x]
y1 = [(2000*i) for i in x]

# output to static HTML file
output_file("log_lines.html")

# create a new plot
p = figure(
   x_axis_label='N', y_axis_label='Iterations'
)

# add some renderers
p.line(x, y0, legend="Y = N^2", line_color="red")
p.line(x, y1, legend="Y = 2000N")
# show the results
show(p)