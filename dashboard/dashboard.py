import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


df = pd.read_csv("./dashboard/all_data.csv")

st.title("Dashboard Air Quality Index")
st.write("### Data from 2013-2017")
st.dataframe(df.head())


st.write("### Corelation Matrix")
corr = df.drop(columns=["wd", "station"]).corr()
fig = px.imshow(corr, text_auto=True)
st.plotly_chart(fig)


st.write("### Jumlah station terbanyak pada dataset?")
station = df["station"].value_counts()
st.bar_chart(station)

st.write("### Trends | PM2.5, PM10, TEMP, O3, DEWP")
cities = ("Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
          "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan",
          "Wanliu", "Wanshouxigong")


def trends(df: pd.DataFrame, option: str, period: str = "year"):
    data = df[df["station"] == option]
    pivot = data.groupby(period)[['PM2.5', 'PM10', "TEMP", "O3", "DEWP"]].mean().reset_index()
    st.line_chart(pivot, x=period, y=["PM2.5", "PM10", "TEMP", "O3", "DEWP"])

option = st.selectbox("Select Station", cities, key="For Trends")
year, month, day = st.tabs(["Year", "Month", "Day"])
with year:
    trends(df, option)
with month:
    trends(df, option, "month")
with day:
    trends(df, option, "day")


# DISPLOT each Column
st.write("### Distribution Plot")
option = st.selectbox("Select Station", cities, key="For Displot", index=None, placeholder="Select Station")
column = st.selectbox("Select Column", df.drop(columns=["wd", "station"]).columns, index=None, placeholder="Select Column")
bins = st.slider("Adjust bins", 5, 50, 5)

if option and column:
    hist_data = df[df["station"] == option][column].sample(500)
    fig = ff.create_distplot([hist_data], [column], bin_size=bins)
    st.plotly_chart(fig)
