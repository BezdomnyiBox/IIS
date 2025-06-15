import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { styled } from "@mui/material";

interface ComponentProps {
  index: number
  cardNumber: number
  building: {
    img: string;
    title: string;
    description: string[];
  };
}

const StyledTypography = styled(Typography)(({ theme }) => ({
    color: theme.palette.text.secondary,
    textAlign: 'justify',
    '& p': {
      marginBottom: theme.spacing(2),
    },
    '& p:last-child': {
      marginBottom: 0,
    },
  }));

function BuildCard({ building, index, cardNumber }: ComponentProps) {
  const isEven = cardNumber % 2 === 0;

  return (
    <Card sx={{ 
      display: "flex", 
      flexDirection: { xs: "column", md: isEven ? "row-reverse" : "row" },
      mb: 4,
      height: "100%"
    }}>
      <CardMedia 
        component="img" 
        alt={building.title} 
        image={building.img}
        sx={{ 
          width: { xs: "100%", md: "50%" },
          height: { xs: 240, md: "auto" }
        }}
      />
      <Box sx={{ 
        display: "flex", 
        flexDirection: "column",
        flex: 1
      }}>
        <CardContent>
          <Typography gutterBottom variant="h5">
            {building.title}
          </Typography>
          {building.description.map((item, ind) => (
            <StyledTypography key={ind} variant="body2">
              {item}
            </StyledTypography>
          ))}
        </CardContent>
        <CardActions sx={{ 
          justifyContent: isEven ? "flex-start" : "flex-end",
          px: 2,
          pb: 2
        }}>
          <Button size="small" variant="contained" color="info">Подробнее</Button>
        </CardActions>
      </Box>
    </Card>
  );
}
export default BuildCard;
