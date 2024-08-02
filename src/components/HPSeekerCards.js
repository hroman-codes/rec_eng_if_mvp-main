import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import LightningSVGAvatar from './icons/LightningSVGAvatar';
import UpwardIconSVG from './icons/UpwardIconSVG';
import MaginifyGlassSVG from './icons/MaginifyGlassSVG';
import CheckSVGIcon from './icons/CheckSVGIcon'
import { Card, CardContent, CardHeader, Typography } from '@mui/material'

const HPSeekerCards = () => {
  return (
    <Grid
      container
      spacing={2}
    >
      <Grid xs={12} sm={6} md={3}>
        <Card 
          sx={{
            borderRadius: '12px',
            border: '4px #4187C9 solid',
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.4);'
          }}
        >
          <CardHeader
            sx={{
              paddingBottom: '3rem'
            }}
            avatar={              
                <LightningSVGAvatar sx={{ fontSize: '3rem'}}/>
            }
          />
            <CardContent>
              <Typography 
                sx={{ 
                  fontFamily: 'Lato',
                  fontWeight: 600,
                  fontStyle: 'normal',
                  fontSize: '1.87rem',
                  color: '#4187C9',
                  textDecoration: 'none',
                }} 
                color='#4187C9;' 
                variant='h5' 
                component="div" 
                paddingBottom={2}
              >
                Start Fast
              </Typography>
              <Typography variant='body2'>
                Our app helps you quickly  
                articulate your value
                proposition, identify target companies, and organize your
                materials.
              </Typography>
            </CardContent>
        </Card>
      </Grid>

      <Grid xs={12} sm={6} md={3}>
        <Card
          sx={{
            borderRadius: '12px',
            border: '4px #4187C9 solid',
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.4);'
          }}
        >
          <CardHeader
            sx={{
              paddingBottom: '3rem'
            }}
            avatar={              
                <UpwardIconSVG sx={{ fontSize: '3rem'}}/>
            }
          />
            <CardContent>
              <Typography 
                sx={{ 
                  fontFamily: 'Lato',
                  fontWeight: 600,
                  fontStyle: 'normal',
                  fontSize: '1.87rem',
                  color: '#4187C9',
                  textDecoration: 'none',
                }} 
                color='#4187C9;' 
                variant='h5' 
                component="div" 
                paddingBottom={2}
              >
                Track your <br /> Progress
              </Typography>
              <Typography variant='body2'>
                The Seeker lets you see how
                your job search progresses each
                week and identify 
                things holding you back.
              </Typography>
            </CardContent>
        </Card>
      </Grid>

      <Grid xs={12} sm={6} md={3}>
        <Card
          sx={{
            borderRadius: '12px',
            border: '4px #4187C9 solid',
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.4);'
          }}
        >
          <CardHeader
            sx={{
              paddingBottom: '3rem'
            }}
            avatar={              
                <MaginifyGlassSVG sx={{ fontSize: '3rem'}}/>
            }
          />
            <CardContent>
              <Typography 
                sx={{ 
                  fontFamily: 'Lato',
                  fontWeight: 600,
                  fontStyle: 'normal',
                  fontSize: '1.87rem',
                  color: '#4187C9',
                  textDecoration: 'none',
                }} 
                color='#4187C9;' 
                variant='h5' 
                component="div" 
                paddingBottom={2}
              >
                Generate <br /> Referrals
              </Typography>
              <Typography variant='body2'>
                Our community and proven
                techniques get you introduced to your target
                companies faster.
              </Typography>
            </CardContent>
        </Card>
      </Grid>

      <Grid xs={12} sm={6} md={3}>
        <Card
          sx={{
            borderRadius: '12px',
            border: '4px #4187C9 solid',
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.4);'
          }}
        >
          <CardHeader
            sx={{
              paddingBottom: '3rem'
            }}
            avatar={              
                <CheckSVGIcon sx={{ fontSize: '3rem'}}/>
            }
          />
            <CardContent>
              <Typography 
                sx={{ 
                  fontFamily: 'Lato',
                  fontWeight: 600,
                  fontStyle: 'normal',
                  fontSize: '1.87rem',
                  color: '#4187C9',
                  textDecoration: 'none',
                }} 
                color='#4187C9;' 
                variant='h5' 
                component="div" 
                paddingBottom={2}
              >
                Stay <br /> accountable
              </Typography>
              <Typography variant='body2'>
                We match you with a weekly
                peer group to keep you
                connected and accountable.
              </Typography>
            </CardContent>
        </Card>
      </Grid>
    </Grid>
  )
}

export default HPSeekerCards
