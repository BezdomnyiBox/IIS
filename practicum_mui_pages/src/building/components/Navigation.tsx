import { Breadcrumbs, Typography, Container } from "@mui/material";
import { useParams, Link } from "react-router-dom";
import structures from "../../data";

function Navigation() {
  const { id } = useParams();
  const buildingIndex = id ? parseInt(id, 10) : 0;
  const buildingTitle = structures[buildingIndex]["title"];
  return (
    <Container maxWidth="xl" sx={{ mt: 2, mb: 2 }}>
      <Breadcrumbs
        separator="›"
        aria-label="breadcrumb"
        sx={{ fontSize: "16px" }}
      >
        <Link
          to="/"
          style={{
            textDecoration: "none",
            color: "#1976d2", // синий цвет ссылки
            fontWeight: 500,
            textTransform: "uppercase",
          }}
        >
          ГЛАВНАЯ
        </Link>
        <Typography
          color="text.primary"
          sx={{
            fontWeight: 500,
            textTransform: "none",
          }}
        >
          {buildingTitle}
        </Typography>
      </Breadcrumbs>
    </Container>
  );
}

export default Navigation;
