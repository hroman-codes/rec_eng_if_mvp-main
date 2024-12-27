import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box, Typography } from '@mui/material'
import Link from '@mui/material/Link';
import SeekerSvgIcon from './icons/SeekerSvgIcon';
import LinkedInSVGIcon from './icons/LinkedInSVGIcon';
import FacebookSVGIcon from './icons/FacebookSVGIcon';
import MailSVGIcon from './icons/MailSVGIcon';


const Footer = () => {
  return (
    <Box 
        sx={{
            background: '#1A1A1A; border-radius: 20px;',
            flexGrow: 1
        }}
        color={'#fff'}
    >
        <Grid container spacing={2} rowSpacing={5} pt={8}>
            <Grid 
                xs={12}
                sm={6}
                md={12}
                lg={6} 
                display={'flex'} 
                justifyContent={'center'}
            > 
                <SeekerSvgIcon 
                    fontSize='large'
                    sx={{
                        fill: '#fff'
                    }}
                />
                <Typography
                    variant="h6"
                    noWrap
                    sx={{
                        ml: 1,
                        fontFamily: 'Lato',
                        fontWeight: 600,
                        fontStyle: 'normal',
                        fontSize: '25px',
                        color: '#fff',
                        textDecoration: 'none'                        
                    }}
                >
                    Linktag
                </Typography>
            </Grid> 

            <Grid 
                xs={12}
                sm={6}
                md={12} 
                lg={6}
                display={'flex'} 
                justifyContent={'center'}
            >
                <Box variant='div' component={'div'} padding={1}>
                    <Link href="https://www.linkedin.com/company/theseeker/"><LinkedInSVGIcon sx={{fontSize: '2.5rem'}}/></Link>
                </Box>
                <Box variant='div' component={'div'} padding={1}> 
                    <Link href="#"><FacebookSVGIcon sx={{fontSize: '2.5rem'}}/></Link>
                </Box>
                <Box variant='div' component={'div'} padding={1}>
                    <Link href="#"><MailSVGIcon sx={{fontSize: '2.5rem'}}/></Link>
                </Box>
            </Grid>
        </Grid>
    </Box>
  )
}

export default Footer