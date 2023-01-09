import dash
import plotly.express as px
import pandas as pd

from django.shortcuts import render
from screener.models import Results


def stockplot(request):
    return render(request, 'chart.html')


def results_chart(request):
    results = Results.objects.all()

    df = pd.DataFrame(
        data={"Sales in INR Crore.": [r.sales for r in results]},
        index=pd.Series(
            [r.date.strftime("%b %Y") for r in results], name="Date"
        ),
    )

    fig = px.bar(
        df,
        title="Quarterly Sales",
        color_discrete_sequence=['#15616D'],
        text_auto='50.0s',
    )

    fig.update_traces(
        textposition='outside'
    )

    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5,
        },
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    chart = fig.to_html()

    context = {'chart': chart}

    return render(request, 'chart.html', context)
