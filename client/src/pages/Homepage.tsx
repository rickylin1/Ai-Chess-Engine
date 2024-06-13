import React from "react";
import Hero from "../components/Hero.tsx";
import ChessBoard from "../components/ChessBoard.tsx";

const Homepage = () => {
  return (
    <>
      <div className="flex flex-col min-h-screen">
        <Hero subtitle="Ready for chess??" />
        <ChessBoard/>
        {/* <div className=" bg-blue-700 flex-grow"></div>{" "} */}
        {/* This div fills up remaining space */}
      </div>
    </>
  );
};

export default Homepage;
