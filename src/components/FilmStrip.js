import React from 'react'
import seekerFilmStrip from './images/seekerFilmStrip.png'
import { Box, Paper } from '@mui/material'
import Grid from '@mui/material/Unstable_Grid2';

const FilmStrip = () => {
  return (
    <Box>
        <Grid container spacing={2} sx={{ marginLeft: 0, marginRight: 0 }}>
            <Grid xs={12} sx={{ padding: 0 }}>
                <Paper sx={{boxShadow: 'none', width: '100%', margin: 0 }}>
                    <div
                      style={{
                        backgroundImage: `url(${seekerFilmStrip})`,
                        height: 'auto',
                        display: 'block',
                        backgroundRepeat: 'repeat',
                        width: '100%',
                        minHeight: '415px',
                      }}
                    />
                </Paper>
            </Grid>
        </Grid>
    </Box>
  )
}

export default FilmStrip
