import plotly.express as px
import pandas as pd

from screener.models import Results
from screener.plotly.common import get_layout


def results_bar():
    res = Results.objects.all()

    df = pd.DataFrame(
        data={
            "Sales": [r.sales for r in res],
            "Profit Before Tax": [r.profit_before_tax for r in res],
            "Net Profit": [r.net_profit for r in res],
        },
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in res], name="Date"
        ),
    )

    df_eps = pd.DataFrame(
        data={
            "EPS": [r.eps for r in res]
        },
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in res], name="Date"
        ),
    )

    fig = px.bar(
        df,
        title="Quarterly Results",
        color_discrete_sequence=['#15616D', '#FFDDAD', '#E06C00'],
        barmode='group',
    )

    fig_eps = px.area(
        df_eps,
        title="Earning Per Share",
        color_discrete_sequence=['#77AF96'],
        markers=True,
    )

    fig = get_layout(fig)
    fig_eps = get_layout(fig_eps)

    fig.update_xaxes(showline=True, linecolor='#D3D3D3', linewidth=0, row=1,
                     col=1, mirror=True)
    fig.update_yaxes(showline=True, linecolor='white', linewidth=0, row=1,
                     col=1, mirror=True, gridcolor='#D3D3D3')

    return fig, fig_eps
