import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box, Button, Typography, useMediaQuery } from '@mui/material'
import SubscribeIconSVG from './icons/SubscribeIconSVG'
import SlackSVGIcon from './icons/SlackSVGIcon'

const FooterBanner = () => {
  const isScreenSizeUnder600px = useMediaQuery('(max-width: 600px)')

  return (
    <Box
      pt={8}
      display={'flex'}
      justifyContent={'center'}
    >
        <Grid 
          container 
          spacing={5}
          sx={{
            background: '#4187C9; border-radius: 20px'
          }}
          width={'100%'}
          height={'100%'}
        >
          <Grid xs={12} pb={0}>
            <Typography
              color={'white'}
              fontSize={'clamp(1.5rem, 2vw, 2.5rem )'}
              fontFamily={'Lato'}
              fontWeight={800}
              wordWrap={'break-word'}
              component={'h1'}
              display={'flex'}
              justifyContent={'center'}
            >
              Let's get this party started<br />
            </Typography>
          </Grid>
          <Grid xs={12} pt={0} pb={0}>
            <Typography
                color={'white'}
                fontSize={'clamp(1rem, 2vw, 1.3rem )'}
                fontFamily={'Lato'}
                wordWrap={'break-word'}
                component={'p'}
                display={'flex'}
                justifyContent={'center'}
              >
                Start this amazing journey! See the alternative we have for you!
              </Typography>
          </Grid>
          <Grid 
            xs={12}
            sm={6}
            display={'flex'}
            justifyContent={ isScreenSizeUnder600px ? 'center' : 'end'}
            pb={isScreenSizeUnder600px ? '0' : '20'}
          >
            <Button 
              variant="outlined" 
              href='https://forms.gle/6uqB2VFhLFejBrP1A'
              startIcon={
                isScreenSizeUnder600px ? 
                <SubscribeIconSVG sx={{fontSize: '3rem !important' }}/> 
                :
                <SubscribeIconSVG sx={{fontSize: '2rem !important' }}/>
              }
              size='large'
              sx={{
                background: '#FFEE3C; border-radius: 20px',
                color: '#4187C9',
                textTransform: 'none',
                padding: '5px 15px',
                '&:hover': {
                  background: '#FFEE3C'
                }
              }}
            >
              <Typography
                color={'#4187C9'}
                fontSize={'clamp(1rem, 2vw, 1rem )'}
                fontFamily={'Lato'}
                wordWrap={'break-word'}
                component={'p'}
                fontWeight={800}
              >
                Start Subscribing
              </Typography>
            </Button>
          </Grid>
          <Grid 
            xs={12} 
            sm={6}
            display={'flex'}
            justifyContent={ isScreenSizeUnder600px ? 'center' : 'none'}
          >
            <Button 
              variant="outlined" 
              href='https://www.theseeker.ai/slack-community'
              startIcon={<SlackSVGIcon sx={{fontSize: '2rem !important' }}/>}
              sx={{
                background: '#fff; border-radius: 20px',
                textTransform: 'none',
                color: '#4187C9',
                padding: '5px 15px',
                '&:hover': {
                  background: '#fff'
                }
              }}
            >
              <Typography
                color={'#4187C9'}
                fontSize={'clamp(1rem, 2vw, 1rem )'}
                fontFamily={'Lato'}
                wordWrap={'break-word'}
                component={'p'}
                fontWeight={800}
                textAlign={'start'}
              >
                Join our FREE Slack <br /> Community
              </Typography>
            </Button>
          </Grid>
        </Grid>
    </Box>
  )
}

export default FooterBanner