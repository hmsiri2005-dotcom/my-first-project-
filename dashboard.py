import streamlit as st
import pandas as pd

st.title("Restaurant Review Dashboard")

data = {
    "Review": [
        "The pizza was amazing, and the crust was perfectly crispy",
        "Food quality was good, though a bit pricey",
        "The biriyani was bland and undercooked",
        "Ambience is nice",
        "Paneer is expensive for the quality served"
    ],
    "Sentiment": [
        "positive",
        "okay -- high price",
        "negative -- bland / undercooked",
        "positive",
        "okay -- high price"
    ]
}

df = pd.DataFrame(data)

st.subheader("Reviews Table")
st.dataframe(df)

positive_count = sum(df['Sentiment'].str.contains("positive"))
negative_count = sum(df['Sentiment'].str.contains("negative"))
okay_count = sum(df['Sentiment'].str.contains("okay"))

st.subheader("Sentiment Summary")
st.metric("Positive Reviews", positive_count)
st.metric("Negative Reviews", negative_count)
st.metric("Okay / Neutral Reviews", okay_count)

st.subheader("Sentiment Distribution")
st.bar_chart({
    "Positive": [positive_count],
    "Negative": [negative_count],
    "Okay": [okay_count]
})