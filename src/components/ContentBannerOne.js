import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box, Typography } from '@mui/material'

const ContentBannerOne = () => {
  return (
    <Box>
      <Grid container spacing={2}>
        <Grid xs={12} textAlign={'center'}>
          <Typography
            paddingTop={2}
            sx={{
              color: '#1B1A1A',
              fontFamily: 'Lato',
              fontWeight: 700,
              lineHeight: 'normal',
              fontSize: 'clamp(1.5rem, 4vw, 1.25rem )',
              wordWrap: 'break-word'
            }}
          >
            Don't go alone! 
          </Typography>
          <Typography 
            paddingLeft={0}
            paddingRight={0}
            paddingTop={0.5}
            paddingBottom={2}
            sx={{
              color: '#1B1A1A',
              fontFamily: 'Lato',
              fontWeight: 500,
              lineHeight: 'normal',
              fontSize: 'clamp(1rem, 4vw, 1.25rem )'
            }}
          >
            Your journey to find the right job deserves the right crew and the right compass.
          </Typography>
        </Grid>
      </Grid>
    </Box>
  )
}



export default ContentBannerOne
