import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import { styled } from "@mui/material/styles";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import Drawer from "@mui/material/Drawer";
import MenuItem from "@mui/material/MenuItem";
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import { Link } from "react-router-dom";

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "space-between",
  flexShrink: 0,
  borderRadius: `calc(${theme.shape.borderRadius}px + 8px)`,
  border: "1px solid",
  borderColor: theme.palette.divider,
  padding: "8px 12px",
  backgroundColor: "white",
}));

interface NavBarProps {
  activePage?: string;
}

function NavBar({ activePage = "1" }: NavBarProps) {
  const [open, setOpen] = React.useState(false);

  const toggleDrawer = (newOpen: boolean) => () => {
    setOpen(newOpen);
  };

  return (
    <AppBar
      position="static"
      sx={{
        boxShadow: 0,
        bgcolor: "transparent",
        mt: "28px",
      }}
    >
      <Container maxWidth="xl">
        <StyledToolbar>
          <Typography variant="h6" fontWeight={"bold"} sx={{ color: "#5d8aa8" }}>
            Мировой экспорт товаров и услуг
          </Typography>

          <Box sx={{ display: { xs: "none", md: "flex" } }}>
            <Link to="/">
              <Button
                variant={activePage === "1" ? "contained" : "text"}
                color="info"
                size="medium"
              >
                Главная
              </Button>
            </Link>
            <Link to="/list">
              <Button
                variant={activePage === "2" ? "contained" : "text"}
                color="info"
                size="medium"
              >
                Список стран
              </Button>
            </Link>

            <Link to="/diagrams">
              <Button
                variant={activePage === "3" ? "contained" : "text"}
                color="info"
                size="medium"
              >
                Диаграммы
              </Button>
            </Link>
          </Box>
          <Box sx={{ display: { xs: "flex", md: "none" } }}>
            <IconButton aria-label="Menu button" onClick={toggleDrawer(true)}>
              <MenuIcon />
            </IconButton>
          </Box>

          <Drawer anchor="top" open={open} onClose={toggleDrawer(false)}>
            <Box>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "flex-end",
                }}
              >
                <IconButton onClick={toggleDrawer(false)}>
                  <CloseRoundedIcon />
                </IconButton>
              </Box>
              <Link to="/">
                <MenuItem
                  color="info"
                  sx={{
                    bgcolor: activePage === "1" ? "info.light" : "transparent",
                    color: activePage === "1" ? "info.contrastText" : "inherit",
                    transition: "all 0.3s ease",
                    "&:hover": {
                      bgcolor: "info.light",
                      color: "info.contrastText",
                      transition: "all 0.3s ease",
                    },
                  }}
                >
                  Главная
                </MenuItem>
              </Link>
              <Link to="/list">
                <MenuItem
                  color="info"
                  sx={{
                    bgcolor: activePage === "2" ? "info.light" : "transparent",
                    color: activePage === "2" ? "info.contrastText" : "inherit",
                    transition: "all 0.3s ease",
                    "&:hover": {
                      bgcolor: "info.light",
                      color: "info.contrastText",
                      transition: "all 0.3s ease",
                    },
                  }}
                >
                  Список стран
                </MenuItem>
              </Link>

              <Link to="/diagrams">
                <MenuItem
                  color="info"
                  sx={{
                    bgcolor: activePage === "3" ? "info.light" : "transparent",
                    color: activePage === "3" ? "info.contrastText" : "inherit",
                    transition: "all 0.3s ease",
                    "&:hover": {
                      bgcolor: "info.light",
                      color: "info.contrastText",
                      transition: "all 0.3s ease",
                    },
                  }}
                >
                  Диаграммы
                </MenuItem>
              </Link>
            </Box>
          </Drawer>
        </StyledToolbar>
      </Container>
    </AppBar>
  );
}
export default NavBar;
