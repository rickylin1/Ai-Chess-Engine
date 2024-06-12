import React from 'react'
import {Outlet} from 'react-router-dom'
import Footer from '../components/Footer.tsx'
import NavBar from '../components/Navbar.tsx'

const MainLayout = () => {
  return (
    <>
    <NavBar></NavBar>
    <Outlet></Outlet>
    <Footer></Footer>
    </>
  )
}

export default MainLayout