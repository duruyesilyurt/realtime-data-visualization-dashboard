import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
st.title("Real-Time Data Visualization Dashboard")
placeholder = st.empty()

while True:
    try:
        data = pd.read_csv("sensor_data.csv")
        # take the first column automatically
        column_name = data.columns[0]
        fig, ax = plt.subplots()
        ax.plot(data.index, data[column_name], marker="o")

        ax.set_xlabel("Time")
        ax.set_ylabel(column_name.capitalize())
        ax.set_title("Live Sensor Data")

        placeholder.pyplot(fig)
        time.sleep(1)
    except FileNotFoundError:
        st.warning("Waiting for sensor data...")
        time.sleep(1)
