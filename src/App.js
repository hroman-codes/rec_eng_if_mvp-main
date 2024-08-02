import './App.css';
import Container from '@mui/material/Container'
import Hero from './components/Hero';
import ContentBannerOne from './components/ContentBannerOne';
import ContentBannerTwo from './components/ContentBannerTwo';
import ContentBannerThree from './components/ContentBannerThree';
import FilmStrip from './components/FilmStrip';
import HPSeekerCards from './components/HPSeekerCards';
import Testimonial from './components/Testimonial';
import FooterBanner from './components/FooterBanner';
import Footer from './components/Footer';

function App() {

  return (
    <div className="App">
      <Hero />
      <ContentBannerOne />
      <FilmStrip />
      <ContentBannerTwo />

      <Container>
        <HPSeekerCards />
      </Container>
      
      <ContentBannerThree />
      
      <Container>
        <Testimonial />
        <FooterBanner />
      </Container>
      <Container maxWidth='xl'>
        <Footer />
      </Container>
    </div>
  );
}

export default App;
