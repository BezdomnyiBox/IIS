import { BarChart } from "@mui/x-charts/BarChart";
import { LineChart } from "@mui/x-charts/LineChart";
import Container from "@mui/material/Container";
import { tGroup } from "../groupdata";
import * as React from "react";
import { axisClasses } from "@mui/x-charts/ChartsAxis";
import SettingChart from "./SettingChart";

type GroupProps = {
  data: tGroup;
};

function GroupChart({ data }: GroupProps) {
  const [series, setSeries] = React.useState({
    "Максимальная высота": true,
    "Средняя высота": false,
    "Минимальная высота": false,
  });
  const [isBar, setIsBar] = React.useState(true);

  let seriesY = Object.entries(series)
    .filter((item) => item[1] == true)
    .map((item) => {
      return { dataKey: item[0], label: item[0] };
    });

  const chartSetting = {
    yAxis: [
      {
        label: "Высота(м)",
      },
    ],
    height: 500,
    sx: {
      [`.${axisClasses.left} .${axisClasses.label}`]: {
        transform: "translate(-10px, 0)",
      },
    },
  };

  const showBarLabels = seriesY.length === 1;

  return (
    <Container maxWidth="lg">
      {isBar ? (
        <BarChart
          dataset={data}
          xAxis={[{ scaleType: "band", dataKey: "Группа" }]}
          series={seriesY}
          slotProps={{
            legend: {
              position: { vertical: "bottom", horizontal: "center" },
            },
          }}
          {...chartSetting}
          barLabel={showBarLabels ? "value" : undefined}
        />
      ) : (
        <LineChart
          dataset={data}
          xAxis={[{ scaleType: "band", dataKey: "Группа" }]}
          series={seriesY}
          slotProps={{
            legend: {
              position: { vertical: "bottom", horizontal: "center" },
            },
          }}
          {...chartSetting}
        />
      )}
      <SettingChart
        series={series}
        setSeries={setSeries}
        isBar={isBar}
        setIsBar={setIsBar}
      />
    </Container>
  );
}
export default GroupChart;
