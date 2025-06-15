import React from 'react';
import { Box, Container, Typography, Link, IconButton, Stack } from '@mui/material';
import { styled } from '@mui/material/styles';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

const StyledFooter = styled(Box)(({ theme }) => ({
  backgroundColor: theme.palette.primary.main,
  color: theme.palette.primary.contrastText,
  padding: theme.spacing(6, 0),
  marginTop: 'auto',
}));

const FooterLink = styled(Link)(({ theme }) => ({
  color: theme.palette.primary.contrastText,
  textDecoration: 'none',
  '&:hover': {
    textDecoration: 'underline',
  },
}));

function Footer() {
  return (
    <StyledFooter>
      <Container maxWidth="lg">
        <Box
          sx={{
            display: 'flex',
            flexDirection: { xs: 'column', md: 'row' },
            justifyContent: 'space-between',
            alignItems: { xs: 'center', md: 'flex-start' },
            gap: 4,
          }}
        >
          {/* О нас */}
          <Box sx={{ maxWidth: 300 }}>
            <Typography variant="h6" gutterBottom>
              О проекте
            </Typography>
            <Typography variant="body2">
              Исследуйте самые впечатляющие архитектурные сооружения мира. 
              Узнайте об их истории, особенностях и технологиях строительства.
            </Typography>
          </Box>

          {/* Быстрые ссылки */}
          <Box>
            <Typography variant="h6" gutterBottom>
              Быстрые ссылки
            </Typography>
            <Stack spacing={1}>
              <FooterLink href="/">Главная</FooterLink>
              <FooterLink href="/buildings">Список зданий</FooterLink>
              <FooterLink href="/contacts">Контакты</FooterLink>
            </Stack>
          </Box>

          {/* Контакты */}
          <Box>
            <Typography variant="h6" gutterBottom>
              Контакты
            </Typography>
            <Stack spacing={1}>
              <Typography variant="body2">
                Email: info@buildings.com
              </Typography>
              <Typography variant="body2">
                Телефон: +7 (999) 123-45-67
              </Typography>
            </Stack>
          </Box>

          {/* Социальные сети */}
          <Box>
            <Typography variant="h6" gutterBottom>
              Мы в соцсетях
            </Typography>
            <Stack direction="row" spacing={1}>
              <IconButton color="inherit" aria-label="Facebook">
                <FacebookIcon />
              </IconButton>
              <IconButton color="inherit" aria-label="Twitter">
                <TwitterIcon />
              </IconButton>
              <IconButton color="inherit" aria-label="Instagram">
                <InstagramIcon />
              </IconButton>
              <IconButton color="inherit" aria-label="LinkedIn">
                <LinkedInIcon />
              </IconButton>
            </Stack>
          </Box>
        </Box>

        {/* Копирайт */}
        <Box
          sx={{
            mt: 4,
            pt: 2,
            borderTop: 1,
            borderColor: 'rgba(255, 255, 255, 0.1)',
            textAlign: 'center',
          }}
        >
          <Typography variant="body2">
            © {new Date().getFullYear()} Самые высокие здания и сооружения. Все права защищены.
          </Typography>
        </Box>
      </Container>
    </StyledFooter>
  );
}

export default Footer; 