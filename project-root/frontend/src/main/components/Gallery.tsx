import structures from "../../data";
import ImageList from "@mui/material/ImageList";
import ImageListItem from "@mui/material/ImageListItem";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import ImageListItemBar from "@mui/material/ImageListItemBar";
import { useNavigate, Link } from "react-router-dom";

const imgData = structures;

function Gallery() {
  
  return (
    <Container maxWidth="lg">
      <Box sx={{ height: 585, overflowY: "scroll", m: "20px auto" }}>
        <ImageList
          variant="masonry"
          sx={{
            columnCount: {
              xs: "1 !important",
              sm: "2 !important",
              md: "3 !important",
              lg: "4 !important",
            },
          }}
          gap={8}
        >
          {imgData.map((item, index) => (
            <Link key={index} to={"/country/" + index}>
              <ImageListItem
                key={item.img}
                sx={{ cursor: "pointer" }}
              >
                <img
                  srcSet={item.img}
                  src={item.img}
                  alt={item.title}
                  loading="lazy"
                  style={{ cursor: "pointer" }}
                />
                <ImageListItemBar position="bottom" title={item.title} />
              </ImageListItem>
            </Link>
          ))}
        </ImageList>
      </Box>
    </Container>
  );
}
export default Gallery;
