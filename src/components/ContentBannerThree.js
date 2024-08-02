import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box,Typography, useMediaQuery } from '@mui/material'
import SeekerSvgIconBanner from './icons/SeekerSVGIconBanner';

const ContentBannerThree = () => {
    const isScreenSizeUnder900px = useMediaQuery('(max-width: 900px)');

    return (
        <Box pt={8}>
            <Grid 
                container 
                spacing={2} 
                sx={{
                    background: 'linear-gradient(180deg, #5A8991 0%, #4187C9 100%)',
                }}
            >
                <Grid md={0} lg={1} xl={3} display={isScreenSizeUnder900px ? 'none' : 'flex'}></Grid>
                <Grid xs={12} sm={12} md={8} lg={8} xl={5} display={isScreenSizeUnder900px ? 'flex' : {}} sx={isScreenSizeUnder900px ? { justifyContent: 'center' } : {}}>
                    <Typography
                        sx={{
                           color: '#fff',
                           fontSize: 'clamp(1.8rem, 5vw, 3rem )',
                           fontFamily: 'Lato',
                           fontWeight: 800,
                           wordWrap: 'break-word',
                           paddingTop: '77px',
                           paddingBottom: '77px',
                        }}
                    >
                        From Seekers to Finders!
                    </Typography>
                </Grid>
                <Grid md={1} lg={3} xl={4} display={isScreenSizeUnder900px ? 'none' : 'flex'}>
                    <SeekerSvgIconBanner 
                        sx={{
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            fontSize: 'clamp(14rem, 4vw, 1.6rem )'
                        }}
                    />
                </Grid>
            </Grid>
        </Box>
    )
}

export default ContentBannerThree