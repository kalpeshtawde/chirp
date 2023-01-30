import plotly.express as px
import pandas as pd

from screener.models import Ratios
from screener.plotly.common import get_layout

from screener.plotly.common import get_color_sequence


def ratios():
    res = Ratios.objects.all()

    df_eps = pd.DataFrame(
        data={
            "ROCE %": [r.roce_pct for r in res]
        },
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in res], name="Date"
        ),
    )

    fig_roce = px.line(
        df_eps,
        title="Return On Capital Employed",
        color_discrete_sequence=[get_color_sequence()[1]],
        markers=True,
    )

    fig_roce = get_layout(fig_roce)

    return fig_roce
