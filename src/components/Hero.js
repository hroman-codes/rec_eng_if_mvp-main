import React from 'react';
import Grid from '@mui/material/Unstable_Grid2';
import CircleSvg from './icons/CircleSvg';
import { useMediaQuery, Box, Typography, Button } from '@mui/material';
import myImage from './images/Hero.png'

import NavBar from './NavBar';

function Hero() {

  const isScreenSizeUnder900px = useMediaQuery('(max-width: 900px)')

  const handleRegisterClick = async () => {
    window.location.href = '/seeker/register/'
  }

  return (
    <Box
      sx={{
        color: '#1B1A1A',         
        paddingTop: '20px',
        paddingBottom: '20px',
        paddingLeft: '0px',
        paddingRight: '0px',
        textAlign: 'center',
        backgroundBlendMode: 'darken',
        backgroundImage: `url(${myImage})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover', 
        margin: 0,
      }}
    >
      <Grid 
        container 
        spacing={2}
        sx={{
          paddingLeft: 0,
          paddingRight: 0
        }}
      >
        <NavBar />
        <Grid xs={2} display={isScreenSizeUnder900px ? 'none' : 'flex'} alignItems="right" justifyContent="right">
          <CircleSvg
            sx={{
              fontSize: '8rem',
            }}
          />
        </Grid>
        <Grid xs={8} display="flex" justifyContent="center" alignItems="center" flexGrow={1} flexShrink={1} flexBasis={'content'}>
          <Typography 
              variant="h3" 
              sx={{
                  fontFamily: 'Lato',
                  fontStyle: 'normal',
                  fontWeight: 700,
                  lineHeight: 'normal',
                  fontSize: 'clamp(2rem, 10vw, 4rem )'
              }}
            >
              Filter through your <br/> LinkedIn connections via tags
            </Typography>
        </Grid>
        <Grid xs={2} display={isScreenSizeUnder900px ? 'none' : 'flex'} alignItems="left" justifyContent="left">
          <CircleSvg
            sx={{
              fontSize: '9rem',
            }}
          />
        </Grid>
      </Grid>

      <Grid container spacing={2}>
        <Grid xs={2} display={isScreenSizeUnder900px ? 'none' : 'flex'} alignItems="left" justifyContent="left">
          <CircleSvg
            sx={{
              fontSize: '4rem',
            }}
          />
        </Grid>
        <Grid xs={isScreenSizeUnder900px ? 12 : 8} display="flex" justifyContent="center" alignItems="center">
          <Typography 
                variant="body1" 
                paragraph
                sx={{
                    fontFamily: 'Lato',
                    fontStyle: 'normal',
                    fontWeight: 400,
                    lineHeight: 'normal',
                    fontSize: 'clamp(0.75rem, 4vw, 1.25rem )'
                }}
              >
                Upload your LinkedIn connections and filter
                  
                <br/> via tags to connect faster 
            </Typography>
        </Grid>
        <Grid xs={2} display={isScreenSizeUnder900px ? 'none' : 'flex'} alignItems="center" justifyContent="center">
          <CircleSvg
            sx={{
              fontSize: '6rem',
            }}
          />
        </Grid>
      </Grid>
    </Box>
  );
}

export default Hero;
