from django.shortcuts import render

# Create your views here.
import plotly.express as px

def visualize_data(request):
    df = px.data.stocks(datetimes=True)
    fig = px.scatter(df, x="date", y="GOOG", trendline="lowess", trendline_options=dict(frac=0.3))
    
    # Convert the Plotly figure to JSON to pass to the template
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {'plot_div': plot_div}
    return render(request, 'plot_plotly/visualization.html', context)
