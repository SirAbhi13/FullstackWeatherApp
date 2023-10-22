import { LineChart, XAxis, YAxis,CartesianGrid, Line } from "recharts";
const Chart = ({data}) => {

  return (

    <LineChart width={800} height={400} data={data}>
      <XAxis dataKey="dt_txt" tick={{ fill: "white" }} interval={0}/>
      <YAxis dataKey="temp" tick={{ fill: "white" }} />
      
      <Line
        type="monotone"
        dataKey="dt_txt"
        stroke="#0074D9"
        strokeWidth={3}
        dot={{ fill: "#0074D9", r: 6 }}
      />
      <Line
        type="monotone"
        dataKey="temp"
        stroke="#2ECC40"
        strokeWidth={3}
        dot={{ fill: "white", r: 8 }}
      />
    </LineChart>
  );
};

export default Chart
