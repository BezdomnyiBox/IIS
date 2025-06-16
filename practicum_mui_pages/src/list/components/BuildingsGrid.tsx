import buildings from "../table";
import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from "@mui/x-data-grid/locales";
import Container from "@mui/material/Container";

function BuildingsGrid() {
  const rows: GridRowsProp = buildings;
  const columns: GridColDef[] = [
    { field: "Название", headerName: "Название", flex: 1 },
    { field: "Тип", flex: 0.5 },
    { field: "Страна", flex: 0.5 },
    { field: "Город", flex: 0.5 },
    { field: "Год" },
    { field: "Высота" },
  ];

  return (
    <Container maxWidth="lg" sx={{ height: "700px", mt: "20px" }}>
      <DataGrid
        localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
        showToolbar={true}
        rows={rows}
        columns={columns}
      />
    </Container>
  );
}

export default BuildingsGrid;


// Самостоятельное задание. Отберите сооружения Тип, которых содержит слово
// «мачта», отсортируйте их по убыванию Высоты, скройте столбцы Город, Год и
// импортируйте эти данные в CSV формате. В загруженном файле React App.csv должны
// содержаться следующие данные:
// Название,Тип,Страна,Высота
// Варшавская радиомачта,Антенная мачта,Польша,646.38
// Телерадиомачта KVLY-TV,Радиомачта,США,629
// Киевская телебашня,Решётчатая мачта,Украина,385
// Виннцкая телемачта,Радиомачта,Украина,354

// Результат в csv файле /list/components/React App.csv