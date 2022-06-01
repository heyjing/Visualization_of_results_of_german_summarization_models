import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
import generate_plot

st.set_page_config(layout="wide")
st.title("Visualization of results of existing German summarization systems")

data = pd.read_csv(
    "Results_of_existing_models_on_different_datasets.csv", index_col=False
)

gb = GridOptionsBuilder.from_dataframe(data)

# Add pagination
gb.configure_pagination(paginationAutoPageSize=True)

# Add a sidebar
gb.configure_side_bar(defaultToolPanel="filters")

# Enable multi-row selection
gb.configure_selection(
    "multiple", use_checkbox=True, groupSelectsChildren="Group checkbox select children"
)

gridOptions = gb.build()


grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode="AS_INPUT",
    update_mode="MODEL_CHANGED",
    fit_columns_on_grid_load=False,
    # Add theme color to the table
    theme="blue",
    enable_enterprise_modules=True,
    height=350,
    width="100%",
)


df = grid_response["data"]
option = st.selectbox(
    "Do you want to see the plot results about other rouge values?",
    ("rouge1", "rouge2", "rougeL"),
)

with st.spinner("Displaying results..."):
    fig = generate_plot.generate_plotly_figure_from_csv_data(df, "1")

    if option == "rouge2":
        fig = generate_plot.generate_plotly_figure_from_csv_data(df, "2")
    if option == "rougeL":
        fig = generate_plot.generate_plotly_figure_from_csv_data(df, "L")

    st.plotly_chart(fig, use_container_width=True)
