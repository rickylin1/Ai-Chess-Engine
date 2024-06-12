import React, { useEffect, useState } from 'react';

const Chessboard = () => {
  const [svgContent, setSvgContent] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/board');
        if (!response.ok) {
          console.log('test')
          throw new Error('Network response was not ok');
        }
        const board = await response.text()
        const svgcontent = board.replace('<svg', '<svg style="background-color: black;"')
        console.log(board);
        setSvgContent(board);
      } catch (error) {
        console.error('WOW an error', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className = "mx-auto size-5/12 " dangerouslySetInnerHTML={{ __html: svgContent }} />
  );
};

export default Chessboard;
