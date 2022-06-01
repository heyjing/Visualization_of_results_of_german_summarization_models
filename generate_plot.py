"""
This python generates plotly figures for pandas dataframe.
"""

import pandas as pd
import plotly.express as px


def generate_plotly_figure_from_csv_data(data, rouge_value):
    colors = {"background": "#111111", "text": "#7FDBFF"}

    total_data = (
        list(data[f"rouge{rouge_value}-precision"])
        + list(data[f"rouge{rouge_value}-recall"])
        + list(data[f"rouge{rouge_value}-fmeasure"])
    )

    metrics = (
        ["precision"] * len(data) + ["recall"] * len(data) + ["f_value"] * len(data)
    )

    models_name = list(data["Models"]) * 3
    datasets_name = list(data["Datasets"]) * 3

    df = pd.DataFrame(
        {
            "Metrics": metrics,
            "Data": total_data,
            "Models": models_name,
            "datasets": datasets_name,
        }
    )
    fig = px.line(df, x="Metrics", y="Data", color="Models", line_dash="datasets")
    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig
