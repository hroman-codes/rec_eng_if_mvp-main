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
                Download CSV Connections
              </Typography>
              <Typography variant='body2'>
                Go to your settings page. Click on data privacy. Click on get a copy of your data. 
                Export your connections. 
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
                Upload <br /> CSV
              </Typography>
              <Typography variant='body2'>
                Find your CSV file and upload it. Our system will automatically filter your connections.
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
                Insert <br /> Tags
              </Typography>
              <Typography variant='body2'>
                Add up to 5 tags aka positions that you would like to search from your connections.
                For example: Software Engineer, Product Manager, UX Designer, Data Scientist,
                Technical Recruiter.
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
                Look Through <br /> Recommendations
              </Typography>
              <Typography variant='body2'>
                You will be able to see your connections that match your tags. 
                Review and edit detailed information.
              </Typography>
            </CardContent>
        </Card>
      </Grid>
    </Grid>
  )
}

export default HPSeekerCards
