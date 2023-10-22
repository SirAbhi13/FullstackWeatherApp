import hotBg from "./assets/hot.jpg";
import coldBg from "./assets/cold.jpg";
import Descriptions from "./components/Descriptions";
import { useEffect, useState } from "react";
import { getFormattedWeatherData } from "./weatherService";
import { Toaster, toast } from "react-hot-toast";
import Chart from "./components/charts";
function App() {

  const [city, setCity] = useState("New Delhi");
  const [weather, setWeather] = useState(null);
  const [units, setUnits] = useState("metric");
  const [bg, setBg] = useState(hotBg);
  const [chart, setCharts] = useState([])

  useEffect(() => {
    try{
    const fetchWeatherData = async () => {
      const data = await getFormattedWeatherData(city, units);
      if( data.temperature ===undefined){
        toast.error('Invalid City.')
      }
      else{
      setWeather(data);
      setCharts(data.forecast_data);
      }
      // dynamic bg
      const threshold = units === "metric" ? 20 : 60;
      if (data.temperature <= threshold) setBg(coldBg);
      else setBg(hotBg);
    };

    fetchWeatherData();
  }
  catch(err){
    toast.error('Invalid City.')
  }
  }, [units, city]);
  const handleUnitsClick = (e) => {
    const button = e.currentTarget;
    const currentUnit = button.innerText.slice(1);
  
  };

  const enterKeyPressed = (e) => {
    if (e.keyCode === 13) {
      setCity(e.currentTarget.value);
      e.currentTarget.blur();
    }
  };

  return (
    <div className="app" style={{ backgroundImage: `url(${bg})` }}>
      <Toaster position="top-center"/>
      <div className="overlay">
        {weather && (
          <div className="container">
            <div className="section section__inputs">
              <input
                onKeyDown={enterKeyPressed}
                type="text"
                name="city"
                placeholder="Enter City..."
              />
            </div>

            <div className="section section__temperature">
              <div className="icon">
                <h3>{`${weather.location}`}</h3>
                <img src={`https://openweathermap.org/img/wn/${weather.icon}@2x.png`} alt="weatherIcon" />
                <h3>{weather.weather_desc}</h3>
              </div>
              <div className="temperature">
                <h1>{`${weather.temperature.toFixed()} °${
                  units === "metric" ? "C" : "F"
                }`}</h1>
              </div>
            </div>
            {
              chart.length>0&&<Chart data={chart}/>
            }
            
            {/* bottom description */}
            <Descriptions weather={weather} units={units} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;