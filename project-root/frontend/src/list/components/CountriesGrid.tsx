import React, { useEffect, useState } from "react";
import { DataGrid, GridColDef} from "@mui/x-data-grid";
import { ruRU } from "@mui/x-data-grid/locales";
import Container from "@mui/material/Container";
import CircularProgress from "@mui/material/CircularProgress";


interface Region {
  id: number;
  name: string;
}

interface SubRegion {
  id: number;
  name: string;
  region: Region;
  region_id: number;
}

interface Country {
  sub_region: SubRegion;
  sub_region_id: number;
  id: number;
  name: string;
}

interface Export {
  id: number;
  year: string;
  value: number;
  country: Country;
}

interface ExportRow {
  id: number;
  year: string;
  value: number;
  countryName: string;
  subRegionName: string;
  regionName: string;
}

const transformExport = (exp: Export): ExportRow => ({
  id: exp.id,
  year: exp.year,
  value: exp.value,
  countryName: exp.country?.name || "—",
  subRegionName: exp.country?.sub_region?.name || "—",
  regionName: exp.country?.sub_region?.region?.name || "—",
});

function CountriesGrid() {
  const [rows, setRows] = useState<ExportRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const columns: GridColDef<ExportRow>[] = [
    {
      field: "countryName",
      headerName: "Страна",
      flex: 1,
    },
    {
      field: "subRegionName",
      headerName: "Подрегион",
      flex: 1,
    },
    {
      field: "regionName",
      headerName: "Регион",
      flex: 1,
    },
    {
      field: "year",
      headerName: "Год",
      flex: 0.5,
    },
    {
      field: "value",
      headerName: "Уровень экспорта от ВВП",
      flex: 1,
    },
  ];

  useEffect(() => {
    setLoading(true);
    setError(null);

    const username = "student";
    const password = "dvfu";

    fetch("http://localhost:5000/structures/api/v1/exports", {
      headers: {
        Authorization: "Basic " + btoa(`${username}:${password}`),
      },
    })
      .then((res) => {
        if (!res.ok) {
          if (res.status === 401) {
            throw new Error("Ошибка аутентификации: неверный логин или пароль");
          }
          throw new Error("Ошибка загрузки данных");
        }
        return res.json();
      })
      .then((data) => {
        setRows(data.exports.map(transformExport));
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <Container maxWidth="lg" sx={{ height: "700px", mt: "20px" }}>
      {loading ? (
        <CircularProgress />
      ) : error ? (
        <div>Ошибка: {error}</div>
      ) : (
        <DataGrid
          localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
          showToolbar={true}
          rows={rows}
          columns={columns}
        />
      )}
    </Container>
  );
}

export default CountriesGrid;