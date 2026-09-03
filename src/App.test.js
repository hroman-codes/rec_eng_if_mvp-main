import { render, screen } from '@testing-library/react';
import App from './App';

test('homepage leads to real Django authentication', () => {
  render(<App />);
  expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Your network.The right people.');
  expect(screen.getByRole('link', { name: 'Sign in' })).toHaveAttribute('href', '/seeker/login/');
  expect(screen.getByRole('link', { name: 'Get started' })).toHaveAttribute('href', '/seeker/register/');
  expect(screen.getByRole('link', { name: 'Create account' })).toHaveAttribute('href', '/seeker/register/');
});

test('explains the actual CSV and role-tag workflow', () => {
  render(<App />);
  expect(screen.getByRole('region', { name: 'How it works' })).toBeInTheDocument();
  expect(screen.getByRole('heading', { name: '1. Upload your CSV' })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: 'See how it works' })).toHaveAttribute('href', '#how-it-works');
});
