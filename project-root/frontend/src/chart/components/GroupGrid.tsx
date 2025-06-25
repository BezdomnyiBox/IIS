import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from "@mui/x-data-grid/locales";
import Container from "@mui/material/Container";


type tGroup = {
  id: number;
  Группа: string | number;
  "Минимальный экспорт": number;
  "Максимальный экспорт": number;
  "Средний экспорт": number;
}[];

type GroupProps = {
  data: tGroup;
};

function GroupGrid({ data }: GroupProps) {
  const rows: GridRowsProp = data;

  const columns: GridColDef[] = [
    { field: "Группа", flex: 0.5 },
    { field: "Минимальный экспорт", flex: 0.5 },
    { field: "Максимальный экспорт", flex: 0.5 },
    { field: "Средний экспорт" },
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

export default GroupGrid;
