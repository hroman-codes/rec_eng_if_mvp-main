import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import { Box, Typography } from '@mui/material'
import Link from '@mui/material/Link';
import SeekerSvgIcon from './icons/SeekerSvgIcon';
import LinkedInSVGIcon from './icons/LinkedInSVGIcon';
// import TwitterSVGIcon from './icons/TwitterSVGIcon';
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
                sm={4}
                md={3}
                lg={3} 
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
                    The Seeker
                </Typography>
            </Grid> 
            <Grid 
                xs={6}
                sm={3}
                md={3}
                lg={2} 
                display={'flex'} 
                justifyContent={'center'}
            >
                <Typography
                    component={'h5'}
                    variant='h5'
                    fontFamily={'Lato'}
                    fontWeight={700}
                    sx={{
                        wordWrap: 'break-word'
                    }}
                >
                    Careers
                    <Typography 
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Job Openings
                    </Typography>
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        About us
                    </Typography>
                </Typography>
            </Grid> 
            <Grid 
                xs={6}
                sm={3}
                md={3} 
                lg={2} 
                display={'flex'} 
                justifyContent={'center'}
            >
                <Typography
                    component={'h5'}
                    variant='h5'
                    fontFamily={'Lato'}
                    fontWeight={700}
                    sx={{
                        wordWrap: 'break-word'
                    }}
                >
                    Services
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Pricing
                    </Typography>
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Progress
                    </Typography>
                </Typography>
            </Grid> 
            <Grid
                xs={6}
                sm={3}
                md={3}
                lg={2}
                display={'flex'} 
                justifyContent={'center'}
            >
                <Typography
                    component={'h5'}
                    variant='h5'
                    fontFamily={'Lato'}
                    fontWeight={700}
                    sx={{
                        wordWrap: 'break-word'
                    }}
                >
                    About
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Company
                    </Typography>
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Getters
                    </Typography>
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Support
                    </Typography>
                </Typography>
            </Grid> 
            <Grid
                xs={6}
                sm={6}
                md={6}
                lg={3} 
                display={'flex'} 
                justifyContent={'center'}
            >
                <Typography
                    component={'h5'}
                    variant='h5'
                    fontFamily={'Lato'}
                    fontWeight={700}
                    sx={{
                        wordWrap: 'break-word'
                    }}
                >
                    Stil not convinced? Schedule <br /> a call with us
                    <Typography
                        pt={1}
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        Please contact us if you want more <br /> information or subscribe to our pages.
                    </Typography>
                </Typography>
            </Grid> 

            
            <Grid 
                xs={12} 
                sm={6}
                md={6}
                lg={3} 
                display={'flex'} 
                justifyContent={'center'}
            >
                <Typography
                    component={'h5'}
                    variant='h5'
                    fontFamily={'Lato'}
                    fontWeight={700}
                    sx={{
                        wordWrap: 'break-word'
                    }}
                >
                    Contact us:
                    <Typography
                        component={'p'}
                        variant='p'
                        fontFamily={'Lato'}
                        fontWeight={400}
                        fontSize={'16px'}
                        sx={{
                            wordWrap: 'break-word'
                        }}
                    >
                        community@theseeker.ai
                    </Typography>
                </Typography>               
            </Grid>

            <Grid 
                lgOffset={6}
                xs={12}
                sm={6}
                md={12} 
                lg={3}
                display={'flex'} 
                justifyContent={'center'}
            >
                <Box variant='div' component={'div'} padding={1}>
                    <Link href="https://www.linkedin.com/company/theseeker/"><LinkedInSVGIcon sx={{fontSize: '2.5rem'}}/></Link>
                </Box>
                {/* <Box variant='div' component={'div'} padding={1}>
                    <TwitterSVGIcon sx={{fontSize: '2.5rem'}}/>
                </Box> */}
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