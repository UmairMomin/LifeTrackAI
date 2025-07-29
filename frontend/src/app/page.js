'use client';
import { Button, Typography, Container, Box } from '@mui/material';
import Link from 'next/link';

export default function Home() {
  return (
    <Container maxWidth="md" className="mt-16 text-center">
      <Typography variant="h3" gutterBottom className="font-bold">
        Welcome to LifeTrack AI
      </Typography>
      <Typography variant="h6" className="mb-8 text-gray-700">
        Your personal AI assistant for managing tasks, tracking productivity, and gaining smart insights.
      </Typography>

      <Box className="flex justify-center gap-4">
        <Link href="/tasks">
          <Button variant="contained" color="primary" size="large">
            View Tasks
          </Button>
        </Link>
        <Link href="/insights">
          <Button variant="outlined" color="primary" size="large">
            View Insights
          </Button>
        </Link>
      </Box>
    </Container>
  );
}
