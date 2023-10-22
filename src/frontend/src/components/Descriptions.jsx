import React from "react";
import "./descriptions.css";

import { FaArrowUp, FaArrowDown, FaWind } from "react-icons/fa";
import { BiHappy } from "react-icons/bi";
import { MdCompress, MdOutlineWaterDrop } from "react-icons/md";

const Descriptions = ({ weather, units }) => {

  const cards = [
    {
      id: 1,
      icon: <FaArrowDown />,
      title: "Cloud Cover",
      data: weather.cloud_cover,
      unit: "%",
    },
    {
      id: 2,
      icon: <FaArrowUp />,
      title: "Visibility",
      data: weather.visibility,
      unit: "m",
    },
    {
      id: 3,
      icon: <BiHappy />,
      title: "feels like",
      data: weather.feels_like_temp.toFixed(),
      unit: "°C",
    },

    {
      id: 4,
      icon: <MdOutlineWaterDrop />,
      title: "humidity",
      data: weather.humidity,
      unit: "%",
    },
    {
      id: 5,
      icon: <FaWind />,
      title: "wind speed",
      data: weather.wind_speed,
      unit: "m/s",
    },
  ];
  return (
    <div className="section section__descriptions">
      {cards.map(({ id, icon, title, data, unit }) => (
        <div key={id} className="card">
          <div className="description__card-icon">
            {icon}
            <small>{title}</small>
          </div>
          <h2>{`${data} ${unit}`}</h2>
        </div>
      ))}
    </div>
  );
};

export default Descriptions;
