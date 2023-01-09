from dash import dcc
import dash_html_components as html


def get_td(id_val, figure, classname=None):
    return html.Div([
        # html.H3(children='Shareholding Pattern'),

        # html.Div(children='''
        #     Dash: A web application framework for Python.
        # '''),

        dcc.Graph(
            id=id_val,
            figure=figure
        ),
    ], className=classname)


def get_layout(fig):
    return fig.update_layout(
        legend_title_font_color="#001524",
        title={
            'font_size': 18,
            'xanchor': 'center',
            'x': 0.5,
        },
        title_font_family='"Open Sans", verdana, arial, sans-serif',
        title_font_color="#001524",
        font_family='"Open Sans", verdana, arial, sans-serif',
        font_color="#001524",
        font_size=14,
        paper_bgcolor='#EDEADE',
        plot_bgcolor='#EDEADE',
        xaxis_title="",
        yaxis_title="",
        #margin=dict(l=0, r=0, t=0, b=0),
    )
