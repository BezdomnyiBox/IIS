import FormControl from "@mui/material/FormControl";
import FormLabel from "@mui/material/FormLabel";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Stack from "@mui/material/Stack";
import Divider from "@mui/material/Divider";
import RadioGroup from "@mui/material/RadioGroup";
import Radio from "@mui/material/Radio";

type tSeries = {
  "Минимальный экспорт": boolean;
  "Максимальный экспорт": boolean;
  "Средний экспорт": boolean;
};
type CheckboxProps = {
  series: tSeries;
  setSeries: React.Dispatch<React.SetStateAction<tSeries>>;
  isBar: boolean;
  setIsBar: React.Dispatch<React.SetStateAction<boolean>>;
};
function SettingChart({ series, setSeries, isBar, setIsBar }: CheckboxProps) {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSeries({
      ...series,
      [event.target.name]: event.target.checked,
    });
  };

  const handleRadioChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.value === "bar") setIsBar(true);
    if (event.target.value === "dot") setIsBar(false);
  };

  return (
    <Stack
      direction="row"
      justifyContent="center"
      divider={<Divider orientation="vertical" flexItem />}
      spacing={2}
      sx={{ m: "20px 0" }}
    >
      <FormControl>
        <FormLabel id="label-radio-group">Тип диаграммы:</FormLabel>
        <RadioGroup name="group-radio" value={isBar ? "bar" : "dot"}>
          <FormControlLabel
            value="bar"
            control={<Radio checked={isBar} onChange={handleRadioChange} />}
            label="Гистограмма"
          />
          <FormControlLabel
            value="dot"
            control={<Radio checked={!isBar} onChange={handleRadioChange} />}
            label="Линейная"
          />
        </RadioGroup>
      </FormControl>
      <FormControl>
        <FormLabel id="label-checkbox-group">На диаграмме показать:</FormLabel>
        <FormControlLabel
          control={
            <Checkbox
              checked={series["Максимальный экспорт"]}
              onChange={handleChange}
              name="Максимальный экспорт"
            />
          }
          label="Максимальный экспорт"
        />

        <FormControlLabel
          control={
            <Checkbox
              checked={series["Средний экспорт"]}
              onChange={handleChange}
              name="Средний экспорт"
            />
          }
          label="Средний экспорт"
        />
        <FormControlLabel
          control={
            <Checkbox
              checked={series["Минимальный экспорт"]}
              onChange={handleChange}
              name="Минимальный экспорт"
            />
          }
          label="Минимальный экспорт"
        />
      </FormControl>
    </Stack>
  );
}
export default SettingChart;
