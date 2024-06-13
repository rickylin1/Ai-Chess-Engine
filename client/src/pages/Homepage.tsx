import React from "react";
import Hero from "../components/Hero.tsx";
import ChessBoard from "../components/ChessBoard.tsx";

import chessImage from '../assets/Deepblue.jpeg'

const Homepage = () => {
  return (
    <>
        <Hero subtitle="Ready for chess??" />
        <div>
          <img className = "mx-auto" src={chessImage} alt="Chess" style={{ maxWidth: "100%" }} />
        </div>
    </>
  );
};

export default Homepage;
