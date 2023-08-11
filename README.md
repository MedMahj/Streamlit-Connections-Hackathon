# Streamlit Connections Hackathon

### Table of Contents

1. [Introduction](#Introduction)
2. [Descriptions](#Descriptions)
3. [Requirement](#Requirement)
4. [Instructions](#instructions)
5. [Automatisation](#Automatisation)


## Introduction: <a name="Introduction"></a>

This demo app presents two different ways to create data connection using `st.experimental_connection` and showcases the functionality of each connection.
    
#### Data Sources :

- **Database** : [MongoDB Atlas](https://www.mongodb.com/atlas) used to extract Klines data from database and display **Cryptoboard**.
- **Secured API** : [OpenWeatherMap API](https://openweathermap.org/api) used to extract Weather data and display **Current Weather**.
  
    
## Descriptions: <a name = "descriptions"></a>

This app has two new connection classes built by extending the built-in `ExperimentalBaseConnection`:

1. **MongoConnection**:  This class has four methods :
> * ` _connect` : used to set up connection to MongoDB using database url.
> * `insert_csv` : used to insert klines data into collection using CSV file.
> * `find` : used to extract klines data from collecton with specific parameters (symbol, interval, limit).
> * `count_documents` : used to count number of documents in a collection.

2. **OpenWeatherConnection** : This class has two methods :
> * ` _connect` : used to set up connection to OpenWeatherMap using API Key.
> * `get` : used to extract weather data with specific parameters (city, units).


## Requirement: <a name = "Requirement"></a>

> we will need an installation of Python 3, plus the following libraries:

- streamlit
- streamlit-extras
- pandas
- plotly
- pymongo 
- dnspython

## Instructions: <a name = "Instructions"></a>

To execute the app follow the instructions below:

1. Create new file `.streamlit/secrets.toml` and add inside the connection string to your Atlas cluster and OpenWeather API Key like below:
```
[connections.mongo]
database = "mongodb+srv://<username>:<password>@<cluster-name>/test?retryWrites=true&w=majority"

[connections.openweather]
api_key = "<API_KEY_OPENWEATHER>"
```

2. Run streamlit in the project's root directory : 
```bash
streamlit run 🏠_Home.py
```
3. Go to http://localhost:8501 to visualize the app

> You can find the app deployed on Streamlit Cloud 😉 : [Connection App.](https://connections-app.streamlit.app/)
    
