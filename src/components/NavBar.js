import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import SeekerSvgIcon from './icons/SeekerSvgIcon';

const pages = ['Login'];

function NavBar() {
  const [anchorElNav, setAnchorElNav] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  return (
    <AppBar position="static" sx={{backgroundColor: 'rgba(0, 0, 0, 0)'}} elevation={0}>
      <Container maxWidth='lg'>
        <Toolbar disableGutters>

          {/* Desktop display  */}
          <SeekerSvgIcon 
            fontSize='large'
            sx={{
              fill: '#4187C9'
            }}
          />
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="#app-bar-with-responsive-menu"
            sx={{
              ml: 1,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'Lato',
              fontWeight: 600,
              fontStyle: 'normal',
              fontSize: '25px',
              color: '#4187C9',
              textDecoration: 'none',
            }}
          >
            Linktag
          </Typography>

          {/* Mobile display of menu  */}
          <Box 
            sx={{ 
              flex: 1, 
              display: { xs: 'flex', md: 'none'}, 
              justifyContent: 'flex-end',
            }}>

            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              {/* Hamburger Icon  */}
              <MenuIcon 
                sx={{ 
                  color: '#4187C9',
                  }}
              />
            </IconButton>

            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' }
              }}
            >
              {pages.map((page) => (
                <MenuItem 
                  key={page} 
                  onClick={handleCloseNavMenu}
                >
                  <a
                    href={page === 'Login' ? '/seeker/login/' : page === 'Sign Up' ? '/seeker/register/' : '#'}
                    style={{ textDecoration: 'none', color: '#4187C9' }}
                  >
                    <Typography 
                      textAlign="center"
                      sx={{
                        color: '#4187C9',
                      }}
                    >
                      {page}
                    </Typography>
                  </a>
                </MenuItem>
              ))}

              <MenuItem onClick={handleCloseNavMenu}>
                  <Typography 
                    textAlign="center"
                    sx={{
                      color: '#4187C9'
                    }}
                  >
                    Apply to our FREE community
                  </Typography>
                </MenuItem>
            </Menu>
          </Box>

          {/* Desktop view div that holds list items in navbar */}    
          <Box 
            sx={{ 
              flex: '30 1 content',
              display: { xs: 'none', md: 'flex' }, 
              justifyContent: 'flex-end' 
            }}
          >
            {pages.map((page) => (
              <Button
                key={page}
                onClick={handleCloseNavMenu}
                href={page === 'Login' ? '/seeker/login/' : undefined || page === 'Sign Up' ? '/seeker/register/' : undefined}
                target="_blank"
                sx={
                    { 
                      my: 2, 
                      color: '#1B1A1A;', 
                      display: 'block',
                      fontSize: '15px',
                      fontFamily: 'Lato',
                      fontWeight: 700,
                      fontStyle: 'normal',
                      lineHeight: 'normal',
                      textTransform: 'none'
                    }
                  }
              >
                {page}
              </Button>
            ))}
          </Box>

          <Box
            sx={{ 
              flex: '1 0 content', 
              display: { xs: 'none', md: 'flex'}, 
              justifyContent: 'flex-end'
            }}
          >

          <a 
            href='/seeker/register/' 
            style={{ textDecoration: 'none' }}
            target="_blank"
            rel="noreferrer"
          >
            <Button 
              variant='contained'
              size='small'
              sx={{
                    borderRadius: '20px',
                    paddingTop: '7px',
                    paddingBottom: '7px',
                    paddingLeft: '12px',
                    paddingRight: '12px'
                  }}
              >
                <Typography
                  sx={{
                      color: '#E1D231',
                      fontSize: '13px',
                      fontFamily: 'Lato',
                      fontWeight: 900,
                      fontStyle: 'normal',
                      lineHeight: 'normal',
                      textTransform: 'none'
                    }}
                >
                  Register
                </Typography>
            </Button>
          </a>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default NavBar;
