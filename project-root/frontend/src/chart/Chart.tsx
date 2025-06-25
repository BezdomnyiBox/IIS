import Navbar from "../components/Navbar";
import GroupGrid from "./components/GroupGrid";
import GroupChart from "./components/GroupChart";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import React, { useState, useEffect } from "react";

type tSelect = "Страна" | "Год" | "Регион";

export type tGroupItem = {
  id: number;
  "Группа": string | number;
  "Минимальный экспорт": number;
  "Максимальный экспорт": number;
  "Средний экспорт": number;
};

export type tGroup = tGroupItem[];

function Chart() {
  const [group, setGroup] = useState<tSelect>("Страна");
  const [groupData, setGroupData] = useState<tGroup>([]);
  
  const [countriesData, setCountriesData] = useState<tGroup>([]);
  const [yearsData, setYearsData] = useState<tGroup>([]);
  const [regionsData, setRegionsData] = useState<tGroup>([]);

  useEffect(() => {
    fetch('http://localhost:5000/structures/api/v1/exports/grouped_by_country', {
      headers: {
        'Authorization': 'Basic ' + btoa('student:dvfu')
      }
    })
      .then(res => res.json())
      .then(data => {
        setCountriesData(data.exports);
        setGroupData(data.exports);
      });

    fetch('http://localhost:5000/structures/api/v1/exports/grouped_by_year', {
      headers: {
        'Authorization': 'Basic ' + btoa('student:dvfu')
      }
    })
      .then(res => res.json())
      .then(data => setYearsData(data.exports));
    
    fetch('http://localhost:5000/structures/api/v1/exports/grouped_by_region', {
      headers: {
        'Authorization': 'Basic ' + btoa('student:dvfu')
      }
    })
      .then(res => res.json())
      .then(data => setRegionsData(data.exports));
  }, []);

  const handleChange = (event: SelectChangeEvent) => {
    const value = event.target.value as tSelect;
    setGroup(value);
    if (value === "Страна") setGroupData(countriesData);
    if (value === "Год") setGroupData(yearsData);
    if (value === "Регион") setGroupData(regionsData);
  };

  return (
    <div>
      <Navbar activePage="3" />
      <GroupChart data={groupData} />
      <Box sx={{ width: "200px", m: "auto" }}>
        <FormControl fullWidth>
          <InputLabel> Группировать по </InputLabel>
          <Select
            id="select-group"
            value={group}
            label="Группировать по"
            onChange={handleChange}
          >
            <MenuItem value="Страна"> Стране </MenuItem>
            <MenuItem value="Год"> Году </MenuItem>
            <MenuItem value="Регион"> Региону </MenuItem>
          </Select>
        </FormControl>
      </Box>
      <GroupGrid data={groupData} />
    </div>
  );
}
export default Chart;
