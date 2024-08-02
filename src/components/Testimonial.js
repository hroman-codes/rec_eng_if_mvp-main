import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import {Box, Typography} from '@mui/material'
import TestimonialGabriealSVG from './icons/TestimonialGabriealSVG'

const Testimonial = () => {
  return (
    <Box pt={8}>
        <Grid 
            container 
            spacing={2}
        >
            <Grid 
                xs={12}
                sm={5}
                sx={{
                    display: 'flex',
                    justifyContent: 'center'
                }}
            
            >
                <TestimonialGabriealSVG 
                    sx={{
                        fontSize: '17rem',
                    }}
                />
            </Grid>
            <Grid 
                xs={12}
                sm={7}
                sx={{
                    display: 'flex',
                    alignItems: 'center'
                }}
            
            >
                <Typography 
                    color={'#1B1A1A'}
                    fontSize={'clamp(1rem, 2vw, 1.2rem )'}
                    fontFamily={'Lato'}
                    fontWeight={400}
                    wordWrap={'break-word'}
                    component={'p'}
                >
                    He landed a job that leverages his bi-lingual fluency, 
                    strong verbal and written communication skills, his customer empathy, and great organizational skills. 
                    But to move that process forward quickly, Gabriel had to take a leap of faith.<br />
                    <Typography 
                        color={'#1B1A1A'}
                        fontSize={'clamp(1rem, 2vw, 1.2rem )'}
                        fontFamily={'Lato'}
                        fontWeight={'bold'}
                        wordWrap={'break-word'}
                        component={'p'}
                        pt={3}
                    >
                        Gabriel Barbosa<br />
                    </Typography>
                    <Typography 
                        color={'#1B1A1A'}
                        fontSize={'clamp(1rem, 2vw, 1.2rem )'}
                        fontFamily={'Lato'}
                        fontWeight={'bold'}
                        wordWrap={'break-word'}
                        component={'p'}
                    >
                        Virtual Assistant | WorkBetterNow
                    </Typography>
                </Typography>
            </Grid>
        </Grid>
    </Box>
  )
}

export default Testimonial