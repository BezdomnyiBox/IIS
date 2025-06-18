import {
  Container,
  Typography,
  Box,
  Paper,
  useTheme,
  useMediaQuery,
} from "@mui/material";
import { useParams, Link } from "react-router-dom";
import structures from "../../data";

function Country() {
  const { id } = useParams();
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm"));
  const countryIndex = id ? parseInt(id, 10) : 0;
  const country = structures[countryIndex];

  if (!country) {
    return (
      <Container maxWidth="xl" sx={{ py: 4 }}>
        <Typography variant="h4">Страна не найдена</Typography>
      </Container>
    );
  }

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Box
        sx={{
          display: "flex",
          flexDirection: { xs: "column", md: "row" },
          gap: 4,
        }}
      >
        <Box sx={{ width: { xs: "100%", md: "50%" } }}>
          <Paper
            elevation={3}
            sx={{
              height: isMobile ? "300px" : "500px",
              overflow: "hidden",
              borderRadius: 2,
            }}
          >
            <Box
              component="img"
              src={country.img}
              alt={country.title}
              sx={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
              }}
            />
          </Paper>
        </Box>

        <Box sx={{ width: { xs: "100%", md: "50%" } }}>
          <Box
            sx={{
              height: "100%",
              display: "flex",
              flexDirection: "column",
              gap: 3,
            }}
          >
            <Typography
              variant="h3"
              component="h1"
              gutterBottom
              sx={{
                fontSize: { xs: "2rem", md: "2.5rem" },
                fontWeight: "bold",
              }}
            >
              {country.title}
            </Typography>

            {country.description.map((paragraph: string, index: number) => (
              <Typography
                key={index}
                variant="body1"
                paragraph
                sx={{
                  fontSize: { xs: "1rem", md: "1.1rem" },
                  lineHeight: 1.6,
                }}
              >
                {paragraph}
              </Typography>
            ))}
          </Box>
        </Box>
      </Box>
    </Container>
  );
}

export default Country;
