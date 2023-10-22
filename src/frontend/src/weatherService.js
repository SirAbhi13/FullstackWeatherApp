

const base_url = "http://127.0.0.1:8000/api/weather/";

const getFormattedWeatherData = async (city) => {
  const endpoint = base_url + `${city}`;
  console.log(endpoint);
  try{
    const data = await fetch(endpoint)
    .then((res) => res.json())
    .then((data) => data).catch((err) =>{console.log(err)})
    // err.message

  
  const {
    temperature,
    feels_like_temp,
    humidity,
    wind_speed,
    cloud_cover,
    visibility,
    weather_desc,
    icon,
    forecast_data,
    location
  } = data;

  return ({
    weather_desc,
    icon,
    temperature,
    feels_like_temp,
    humidity,
    wind_speed,
    cloud_cover,
    visibility,
    location,
    forecast_data,
});
  }
  catch(err){
    console.log(err)
  }
};

export { getFormattedWeatherData };
