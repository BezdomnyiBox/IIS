import React from "react";
import { Box } from "@mui/material";
import "./styles/App.css";
import NavBar from "./components/Navbar";
import Gallery from "./components/Gallery";
import Content from "./components/Content";
import Footer from "./components/Footer";

function App() {
  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
      }}
    >
      <NavBar />
      <Box sx={{ flex: 1 }}>
        <Gallery />
        <Content />
      </Box>
      <Footer />
    </Box>
  );
}

export default App;
