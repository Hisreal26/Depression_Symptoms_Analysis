import pandas as pd
import streamlit as st
import plotly.express as px



st.markdown("## DEPRESSION SYMPTOMS IN UNITED STATE")
#create a data frame
df = pd.read_csv("Depressive_Symptoms_Across_US_Population.csv")
st.write(df)


#code for data inspection
st.markdown("#### TABLE ON DEPRESSION SYMPTOMS IN UNITED STATE FIRST 7 ROW")
chart_ = df.head(7)
st.table(chart_)


#code for data inspection
st.markdown("#### TABLE ON DEPRESSION SYMPTOMS IN UNITED STATE LAST 7 ROW")
Hisreal_ = df.tail(7)
st.table(Hisreal_)


#code for data inspection
st.markdown("##### GENERAL INFORMATION ON DEPRESSION SYMPTOMS IN UNITED STATE LAST 7 ROW")
Hisreal_ = df.describe()
st.table(Hisreal_)


#code for data inspection
st.markdown("##### GENERAL INFORMATION ON DEPRESSION SYMPTOMS IN UNITED STATE LAST 7 ROW")
Hisreal_ = df.shape
st.table(Hisreal_)


st.markdown("## UNIVARIATE VARIABLES")
#code to pick a column in a table - univariate
df = pd.read_csv("Depressive_Symptoms_Across_US_Population.csv")
Entity = df["Several days"].describe()
st.markdown("### Rate ofoccurrence")
st.write(Entity)


st.title("HISTOGRAM REPRESENTATION")
Several_days =px.histogram(df["Several days"], x = "Several days", title = "Entity")
st.plotly_chart(Several_days, use_container_width = True)

#display string type data using bar chart
st.title("BAR GRAPH REPRESENTATION")
Entity_count = df["Entity"].value_counts()
Entity_count.columns = ["Entity", "counts"]
Several_days2 =px.bar(df["Entity"], x = "Entity", title = "Several days")
st.plotly_chart(Several_days2, use_container_width = True)



st.title("PIE REPRESENTATION")
counted = df["Several days"].value_counts().reset_index()
counted.columns = ["Several days", "count"]
Several_days_ = px.pie(counted, names="Several days", values="count", title="Entity")
st.plotly_chart(Several_days_, use_container_width = True)
