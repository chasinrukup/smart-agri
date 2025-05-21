import React, { PropsWithChildren } from 'react';
import { AppBar, Toolbar, Typography, Container } from '@mui/material';

const DashboardLayout: React.FC<PropsWithChildren> = ({ children }) => {
  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div">
            Smart Agriculture Dashboard
          </Typography>
        </Toolbar>
      </AppBar>
      <Container sx={{ marginTop: 4 }}>{children}</Container>
    </>
  );
};

export default DashboardLayout; 