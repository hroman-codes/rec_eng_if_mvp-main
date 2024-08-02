import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box, Typography } from '@mui/material'

const ContentBannerTwo = () => {
  return (
    <Box>
      <Grid container spacing={2}>
        <Grid xs={12} textAlign={'center'}>
          <Typography 
            paddingTop={5}
            paddingBottom={2}
            sx={{
              color: '#1B1A1A',
              fontFamily: 'Lato',
              fontWeight: 800,
              lineHeight: 'normal',
              fontSize: 'clamp(2rem, 4vw, 1.6rem )',
              wordWrap: 'break-word',
            }}
          >
            Use a Proven Path
          </Typography>
        </Grid>
      </Grid>
    </Box>
  )
}

export default ContentBannerTwo
