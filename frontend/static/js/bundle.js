// Import necessary dependencies and modules
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Assuming App.js is your main component
import './index.css'; // Assuming you have a main CSS file for styling

// Render the main component (App) into the root element of your HTML
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
