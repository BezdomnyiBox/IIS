import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import CountryCard from "./CountryCard";
import structures from "../../data";
const cardData = [structures[3], structures[6], structures[9], structures[7]];

function Content() {
  return (
    <Container maxWidth="xl">
      <Grid container spacing={{ xs: 3, md: 6 }}>
        {cardData.map((item, index) => (
          <Grid key={index} size={{ xs: 12, md: 6 }}>
            <CountryCard country={ item } index={ index } cardNumber={index + 1}/>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}
export default Content;
