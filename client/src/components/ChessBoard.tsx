import React, { useEffect, useState } from "react";
import './Winner.css'

const Chessboard = () => {
  const [svgContent, setSvgContent] = useState("");
  const [moveInput, setMoveInput] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/board");
        if (!response.ok) {
          console.log("test");
          throw new Error("Network response was not ok");
        }
        const board = await response.text();
        const svgcontent = board.replace(
          "<svg",
          '<svg style="background-color: black;"'
        );
        console.log(board);
        setSvgContent(board);
      } catch (error) {
        console.error("WOW an error", error);
      }
    };

    fetchData();
  }, []);

  const handleInputChange = (event) => {
    setMoveInput(event.target.value);
  };

  const handleReset = async(event) =>{
    try{
      const response = await fetch("/reset_game")
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const boardResponse = await fetch("/board");
      if (!boardResponse.ok) {
        throw new Error("Failed to fetch updated board");
      }
      const board = await boardResponse.text();
      const svgContentWithStyle = board.replace(
        "<svg",
        '<svg style="background-color: black;"'
      );

      // Update the SVG content state with the new board SVG
      setSvgContent(svgContentWithStyle);

     
    }
    catch (error) {
      console.error("Error submitting move:", error);
    }
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("/play_2_players", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ move: moveInput }), // Send move input as JSON
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // Optionally handle response data here if needed
      const responseData = await response.json();
      const winner = responseData['winner']
      console.log("Response:", responseData);

      const boardResponse = await fetch("/board");
      if (!boardResponse.ok) {
        throw new Error("Failed to fetch updated board");
      }
      const board = await boardResponse.text();
      const svgContentWithStyle = board.replace(
        "<svg",
        '<svg style="background-color: black;"'
      );

      // Update the SVG content state with the new board SVG
      setSvgContent(svgContentWithStyle);

      // Reset the input after successful submission
      setMoveInput("");
    } catch (error) {
      console.error("Error submitting move:", error);
    }
  };


  return (
    <>
      <div className="mx-auto text-center">
        <button onClick = {handleReset} className="bg-red-500 text-white py-2 px-4 rounded-md hover:bg-red-700 focus:outline-none focus:ring focus:border-red-700 mr-4">
          Reset
        </button>
        <div
          className="mx-auto size-5/12"
          dangerouslySetInnerHTML={{ __html: svgContent }}
        />
        <div className="mt-5 mx-auto">
          <div className="flex justify-end"></div>
          <form
            onSubmit={handleSubmit}
            className="mx-auto max-w-xs bg-blue-200 p-4 rounded-lg shadow-md"
          >
            <label>
              Move:
              <input
                type="text"
                className="block w-full mt-1 p-2 border border-blue-500 rounded-md focus:outline-none focus:ring focus:border-blue-700"
                value={moveInput}
                onChange={handleInputChange}
              />
            </label>
            <button
              type="submit"
              className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring focus:border-blue-700"
            >
              Confirm
            </button>
          </form>
        </div>
      </div>
    </>
  );
};

export default Chessboard;
