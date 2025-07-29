'use client';
import { AppBar, Toolbar, Typography, Button, IconButton, Box } from '@mui/material';
import Link from 'next/link';

export default function Navbar() {
  return (
    <AppBar position="static" className="bg-blue-500">
      <Toolbar className="flex justify-between">
        <Box className="flex items-center space-x-2">
          <Typography variant="h6" component="div">
            LifeTrack AI
          </Typography>
        </Box>
        <Box className="space-x-4">
          <Link href="/"><Button color="inherit">Home</Button></Link>
          <Link href="/tasks"><Button color="inherit">Tasks</Button></Link>
          <Link href="/insights"><Button color="inherit">Insights</Button></Link>
          <Link href="/login"><Button color="inherit">Login</Button></Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
}
