import dash_html_components as html
from django_plotly_dash import DjangoDash

from screener.plotly.shareholding_plot import shareholding
from screener.plotly.results_bar_plot import results_bar
from screener.plotly.ratios_plot import ratios
from screener.plotly.cashflow_plot import cashflow
from screener.plotly.common import get_td


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash(
    name="stockplot",
    external_stylesheets=external_stylesheets,
)

shareholding_fig, shareholding_pie_fig = shareholding()
results_bar_fig, results_eps_area_fig = results_bar()
ratios_area_fig = ratios()
cashflow_line_fig = cashflow()

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        get_td("graph3", results_bar_fig),
    ], className='row'),
    html.Div([
        get_td("graph1", shareholding_fig, "six columns"),
        get_td("graph2", shareholding_pie_fig, "six columns"),
    ], className='row'),
    html.Div([
        get_td("graph4", results_eps_area_fig),
    ], className='row'),
    html.Div([
        get_td("graph5", ratios_area_fig),
    ], className='row'),
    html.Div([
        get_td("graph6", cashflow_line_fig),
    ], className='row'),
])
