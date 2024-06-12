import React from "react";
import NavBar from "../components/Navbar.tsx";
import Hero from "../components/Hero.tsx";
import ChessBoard from "../components/ChessBoard.tsx";
import Footer from "../components/Footer.tsx";

const Homepage = () => {
  return (
    <>
      <div className="flex flex-col min-h-screen">
        <Hero subtitle="Ready for chess??" />
        <ChessBoard/>
        <div className=" bg-blue-600 flex-grow"></div>{" "}
        {/* This div fills up remaining space */}
      </div>
    </>
  );
};

export default Homepage;
