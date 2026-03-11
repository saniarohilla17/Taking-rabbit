import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt 🐰")
st.write("Talk to your business data instantly")

file = st.file_uploader("Upload your CSV file", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:

        if "highest revenue" in question.lower():

            revenue = df.groupby("Region")["Revenue"].sum()

            max_region = revenue.idxmax()
            max_value = revenue.max()

            st.success(f"{max_region} region generated highest revenue: {max_value}")

            fig, ax = plt.subplots()
            revenue.plot(kind="bar", ax=ax)

            plt.title("Revenue by Region")

            st.pyplot(fig)