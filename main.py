import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio

PATH = "/Users/andresgarcia/Documents/projects/kaggle/"

# Country Daily Data
df = pd.read_csv(PATH + "input/agg_country_2021_02_26.csv", index_col="GID_0", parse_dates=True)
df = df.drop(['ISO_3', 'NAME_0', 'country_agg'], axis=1).fillna(0)
df2 = df.filter(regex='pct')

def get_data(type, date):
    if type == "Country Daily":
        try:
            df = pd.read_csv(PATH + f"input/agg_country_{date}.csv", index_col="GID_0", parse_dates=True)
            df = df.drop(['ISO_3', 'NAME_0', 'country_agg'], axis=1).fillna(0)
            df_out = df.filter(regex='pct')
            return df_out
        except:
            st.write(f"{date} file does not exits!")
            return pd.DataFrame()

    elif type == "Region Daily":
        try:
            df = pd.read_csv(PATH + f"input/agg_region_{date}.csv", index_col="GID_1", parse_dates=True)
            df = df.drop(['ISO_3', 'GID_0', 'NAME_0', 'NAME_1', 'country_agg', 'region_agg'], axis=1).fillna(0)
            df_out = df.filter(regex='pct')
            return df_out
        except:
            st.write(f"{date} file does not exits!")
            return pd.DataFrame()

    elif type == "Country Smoothed":
        pass
    else:
        pass

def data_hists(data):
    for col in data.columns:
        fig = px.histogram(df2, x=col)
        st.plotly_chart(fig, use_container_width=True)


st.title("COVID-19 World Symptoms Survey Aggregates")

st.sidebar.markdown('## UMD COVID-19 Survey Aggregates')
date = st.sidebar.date_input("Pick date:")
agg_type = st.sidebar.radio(
    "Pick Aggregates", ("Country Daily", "Region Daily", "Country Smoothed", "Region Smoothed"))

if agg_type == "Country Daily":
    st.markdown("### Country Daily")
    data = get_data(agg_type, date.strftime("%Y_%m_%d"))
    if not data.empty:
        data_hists(data)

elif agg_type == "Region Daily":
    st.markdown("### Region Daily")
    data = get_data(agg_type, date.strftime("%Y_%m_%d"))
    if not data.empty:
        data_hists(data)

elif agg_type == "Country Smoothed":
    st.markdown("### Country Smoothed is under construction...")
else:
    st.markdown("### Region Smoothed is under construction...")