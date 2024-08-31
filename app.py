import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the model
with open('randomforest model.pkl', 'rb') as load:
    model = pickle.load(load)

# Define prediction function
def predict(distance, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, avg_wind_speed, avg_pressure):
    prediction = model.predict([[distance, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, avg_wind_speed, avg_pressure]])
    return prediction[0]

# Main function for the Streamlit app
def main():
    st.title("Solar Power Generation Prediction")

    # Sidebar inputs
    distance = st.sidebar.number_input('Distance to Solar Noon (radians)', min_value=0.0, max_value=1.0, step=0.01)
    temperature = st.sidebar.number_input('Temperature (°C)', min_value=-50.0, max_value=100.0, step=0.1)
    wind_direction = st.sidebar.number_input('Wind Direction (degrees)', min_value=0.0, max_value=360.0, step=0.1)
    wind_speed = st.sidebar.number_input('Wind Speed (m/s)', min_value=0.0, max_value=100.0, step=0.1)
    sky_cover = st.sidebar.number_input('Sky Cover (scale 0-4)', min_value=0.0, max_value=4.0, step=0.1)
    visibility = st.sidebar.number_input('Visibility (km)', min_value=0.0, max_value=100.0, step=0.1)
    humidity = st.sidebar.number_input('Humidity (%)', min_value=0.0, max_value=100.0, step=0.1)
    avg_wind_speed = st.sidebar.number_input('Average Wind Speed (m/s)', min_value=0.0, max_value=100.0, step=0.1)
    avg_pressure = st.sidebar.number_input('Average Pressure (inHg)', min_value=25.0, max_value=32.0, step=0.01)

    # Prediction and display
    if st.button('Predict'):
        result = predict(distance, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, avg_wind_speed, avg_pressure)
        st.success(f'The predicted power generated is: {result:.2f} Joules')

        # Scatter plot
        fig, ax = plt.subplots()
        ax.scatter(temperature, wind_speed, color='blue')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Wind Speed (m/s)')
        ax.set_title('Temperature vs Wind Speed Scatter Plot')
        st.pyplot(fig)

if __name__ == '__main__':
    main()
