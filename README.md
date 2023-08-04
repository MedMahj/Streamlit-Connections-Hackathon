# Streamlit-Connections-Hackathon


### How it works 

This demo app presents two different ways to create data connection using `st.experimental_connection` and showcases the functionality of each connection.
    
#### Data Sources :

- **Database** : [MongoDB Atlas](https://www.mongodb.com/atlas) used to extract Klines data from database and display **Cryptoboard**.
- **Secured API** : [OpenWeatherMap API](https://openweathermap.org/api) used to extract Weather data and display **Current Weather**.
  
    
### What's included

This app has two new connection classes built by extending the built-in `ExperimentalBaseConnection`:

1. **MongoConnection**:  This class has four methods :
> * ` _connect` : used to set up connection to MongoDB using database url.
> * `insert_csv` : used to insert klines data into collection using CSV file.
> * `find` : used to extract klines data from collecton with specific parameters (symbol, interval, limit).
> * `count_documents` : used to count number of documents in a collection.

2. **OpenWeatherConnection** : This class has two methods :
> * ` _connect` : used to set up connection to OpenWeatherMap using API Key.
> * `get` : used to extract weather data with specific parameters (city, units).

  
    
