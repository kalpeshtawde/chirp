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
        legend_title_font_color="white",
        title={
            'font_size': 14,
            'xanchor': 'center',
            'x': 0.5,
        },
        title_font_family='"Open Sans", verdana, arial, sans-serif',
        title_font_color="white",
        font_family='"Open Sans", verdana, arial, sans-serif',
        font_color="#ffffff",
        font_size=11,
        paper_bgcolor='#000000',
        plot_bgcolor='#000000',
        xaxis=dict(
            showgrid=False,
            title="Quarter"
        ),
        yaxis=dict(
            showgrid=False,
            title="ROCE"
        ),
        showlegend=False,
        #margin=dict(l=0, r=0, t=0, b=0),
    )


def get_color_sequence():
    return ["#2a9d8f", "#e9c46a", "#81b29a", "#f4a261", "#e76f51"]