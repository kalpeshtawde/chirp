import plotly.express as px
import pandas as pd

from screener.models import CashFlow
from screener.plotly.common import get_layout


def cashflow():
    shr = CashFlow.objects.all()

    df = pd.DataFrame(
        data={
            "Operating": [r.operating for r in shr],
            "Investing": [r.investing for r in shr],
            "Financing": [r.financing for r in shr],
            "Net": [r.net for r in shr],
        },
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in shr], name="Date"
        ),
    )

    fig = px.line(
        df,
        title="Cash Flow (INR Cr.)",
        color_discrete_sequence=['#15616D', '#E06C00', '#ACD2ED', '#C94057'],
        markers=True,
    )

    fig = get_layout(fig)
    fig.update_xaxes(showline=True, linecolor='#D3D3D3', linewidth=0, row=1,
                     col=1, mirror=True)
    fig.update_yaxes(showline=True, linecolor='white', linewidth=0, row=1,
                     col=1, mirror=True, gridcolor='#D3D3D3')

    return fig
