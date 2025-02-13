import streamlit as st
import requests  # OpenWeather API key

API_KEY = 'c597e2868c9c438fa2e0c24ade2a1ecc'  # Your OpenWeather API key

# Function to get weather data
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

# Streamlit app starts here
def run_weather_app():
    # Custom CSS for styling
    st.markdown("""
        <style>
            body {
                background-color: #ffff;
                font-family: 'Arial', sans-serif;
            }
            .title {
                font-size: 36px;
                font-weight: bold;
                color: #4a90e2;
                text-align: center;
                margin-top: 20px;
            }
            .input-box {
                margin: 20px auto;
                width: 60%;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #4a90e2;
                font-size: 16px;
            }
            .result {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: 30px auto;
                color: #333;
            }
            .result h3 {
                color: #4a90e2;
            }
            .result p {
                font-size: 18px;
                margin: 5px 0;
            }
            .btn {
                background-color: #4a90e2;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .btn:hover {
                background-color: #357ab7;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="title">Weather Forecast</div>', unsafe_allow_html=True)
    
    # Input for city name
    city = st.text_input('Enter a city name:', '', key="city", help="Enter the name of a city to get weather details.")
    
    # Button to get weather
    if st.button('Get Weather', key="get_weather", help="Click to get the weather forecast"):
        if city.strip():  # Ensure that the input is not empty
            try:
                # Getting the weather report
                data = get_weather(city)
                
                # Checking if the response is successful
                if data.get('cod') != 200:
                    st.error(data.get('message'))
                else:
                    # Displaying results in a styled box
                    st.markdown(f"""
                        <div class="result">
                            <h3>{data['name']}, {data['sys']['country']}</h3>
                            <p><strong>Temperature:</strong> {data['main']['temp']}°C</p>
                            <p><strong>Weather:</strong> {data['weather'][0]['description'].capitalize()}</p>
                            <p><strong>Humidity:</strong> {data['main']['humidity']}%</p>
                            <p><strong>Wind Speed:</strong> {data['wind']['speed']} m/s</p>
                        </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error occurred: {e}")
        else:
            st.warning("Please enter a city name.")

# This is the main app function call
if __name__ == '__main__':
    run_weather_app()
