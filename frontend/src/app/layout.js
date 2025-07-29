import './globals.css';
import Navbar from '../components/navbar';

export const metadata = {
  title: 'LifeTrack AI',
  description: 'AI-enhanced productivity tracker',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="p-4">{children}</main>
      </body>
    </html>
  );
}
