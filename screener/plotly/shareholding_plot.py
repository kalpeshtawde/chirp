import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from screener.models import Shareholding
from screener.plotly.common import get_layout


def shareholding():
    shr = Shareholding.objects.all()

    shr_latest = shr.order_by('-date').first()

    df = pd.DataFrame(
        data={
            "Promoters %": [r.promoters_pct for r in shr],
            "FIIs %": [r.fii_pct for r in shr],
            "DIIs %": [r.dii_pct for r in shr],
            "Government %": [r.government_pct for r in shr],
            "Public %": [r.public_pct for r in shr],
        },
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in shr], name="Date"
        ),
    )

    fig = px.line(
        df,
        title="Shareholding",
        color_discrete_sequence=['#15616D', '#E06C00', '#ACD2ED', '#C94057',
                                 '#77AF9C'],
        markers=True,
    )

    fig = get_layout(fig)
    fig.update_xaxes(showline=True, linecolor='#D3D3D3', linewidth=0, row=1,
                     col=1, mirror=True)
    fig.update_yaxes(showline=True, linecolor='white', linewidth=0, row=1,
                     col=1, mirror=True, gridcolor='#D3D3D3')

    random_x = [
        shr_latest.promoters_pct,
        shr_latest.fii_pct,
        shr_latest.dii_pct,
        shr_latest.government_pct,
        shr_latest.public_pct,
    ]

    names = ["Promoters %", "FIIs %", "DIIs %", "Government %", "Public %"]

    fig_pie = go.Figure(data=[go.Pie(
        values=random_x, labels=names,
        title="Investors",
        hole=.3,
    )])
    fig_pie.update_traces(
        marker=dict(colors=['#15616D', '#C94057', '#E06C00', '#ACD2ED', '#77AF9C'])
    )
    fig_pie = get_layout(fig_pie)

    return fig, fig_pie
