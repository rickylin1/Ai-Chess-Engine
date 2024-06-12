import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import {Route, createBrowserRouter, createRoutesFromElements, RouterProvider} from 'react-router-dom'
import NavBar from './components/Navbar.tsx';
import Hero from './components/Hero.tsx';
import Homepage from './pages/Homepage.tsx';

function App() {

  //this is a useeffect hook to get deepblue API
  // const [data, setData] = useState({});

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const response = await fetch('/deepblue');
  //       if (!response.ok) {
  //         console.log('test')
  //         throw new Error('Network response was not ok');
  //       }
  //       const jsonData = await response.json();
  //       console.log(jsonData);
  //       setData(jsonData);
  //     } catch (error) {
  //       console.error('WOW an error', error);
  //     }
  //   };

  //   fetchData();
  // }, []);
  const router = createBrowserRouter(
    createRoutesFromElements(
    <Route index element = {<Homepage></Homepage>}> 
    </Route>
   
  )
  )

  return (
    <>
      <RouterProvider router = {router}></RouterProvider>
    </>
  );
}

export default App;
