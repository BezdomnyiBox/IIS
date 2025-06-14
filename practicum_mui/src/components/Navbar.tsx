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

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "space-between",
  flexShrink: 0,
  borderRadius: `calc(${theme.shape.borderRadius}px + 8px)`,
  border: "1px solid",
  borderColor: theme.palette.divider,
  padding: "8px 12px",
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
          <Typography variant="h6" sx={{ color: "#5d8aa8" }}>
            Самые высокие здания и сооружения
          </Typography>

          <Box sx={{ display: { xs: "none", md: "flex" } }}>
            <Button 
              variant={activePage === "1" ? "contained" : "text"} 
              color="info" 
              size="medium"
            >
              Главная
            </Button>
            <Button 
              variant={activePage === "2" ? "contained" : "text"} 
              color="info" 
              size="medium"
            >
              Список зданий
            </Button>
            <Button 
              variant={activePage === "3" ? "contained" : "text"} 
              color="info" 
              size="medium"
            >
              Контакты
            </Button>
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
                Список зданий
              </MenuItem>
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
                Контакты
              </MenuItem>
            </Box>
          </Drawer>
        </StyledToolbar>
      </Container>
    </AppBar>
  );
}
export default NavBar;
