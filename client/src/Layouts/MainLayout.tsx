import React from 'react'
import {Outlet} from 'react-router-dom'
import Footer from '../components/Footer.tsx'
import NavBar from '../components/Navbar.tsx'
import '../styles/MainLayout.css'

const MainLayout = () => {
  return (
    <>
       <div className="main-layout">
      <NavBar />
      <div className="content">
        <Outlet />
      </div>
      <Footer />
    </div>
    </>
  )
}

export default MainLayout