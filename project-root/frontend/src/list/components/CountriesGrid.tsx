import exports_level from "../table";
import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from "@mui/x-data-grid/locales";
import Container from "@mui/material/Container";

function CountriesGrid() {
  const rows: GridRowsProp = exports_level;
  const columns: GridColDef[] = [
    { field: "Страна", flex: 0.5 },
    { field: "Год", flex: 0.5 },
    { field: "Уровень экспорта от ВВП", flex: 0.5 },
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

export default CountriesGrid;