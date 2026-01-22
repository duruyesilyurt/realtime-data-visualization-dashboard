# Real-Time Data Visualization Dashboard

This project demonstrates a real-time data visualization system built using Python.
Sensor data is logged to a CSV file and visualized through a Streamlit dashboard.

## Features
- Real-time sensor data logging to CSV
- Live data updates and visualization
- Dynamic plots using matplotlib
- Interactive dashboard built with Streamlit

## Files
- `sensor_logger.py` – generates and logs sensor data to a CSV file
- `sensor_data.csv` – sample sensor data
- `app.py` – Streamlit dashboard for real-time visualization
- `requirements.txt` – project dependencies

## Technologies
- Python
- Streamlit
- pandas
- matplotlib

## How to Run
```bash
pip install -r requirements.txt
python sensor_logger.py
streamlit run app.py

