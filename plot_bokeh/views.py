from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html


def visualize_date(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(title="Bokeh Example")
    p.line(x, y, line_width=2)
    bokeh_script = file_html(p, CDN)
    return render(request, 'plot_bokeh/visualization.html', {'bokeh_script': bokeh_script})
    