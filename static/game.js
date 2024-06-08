  // JavaScript for handling form submission and updating the chessboard
  document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and display the chessboard SVG
    function updateBoard() {
        fetch('/board')
        .then(response => response.text())
        .then(svg => {
            document.getElementById('board').innerHTML = svg;
        });
    }

    // Update the board when the page loads
    updateBoard();

    function resetBoard() {
        fetch('/reset_game')
    }

    // Handle form submission to make moves
    document.getElementById('move-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        const formData = new FormData(this);
        formData.append('mode', mode); // Append mode to the form data
        fetch('/move', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(message => {
            alert(message); // Display a message indicating if the move was successful
            const pattern = /Game over! The winner is \w+/;
            if (pattern.test(message)) {
            // Reset the board here
                resetBoard();
            }

            updateBoard(); // Update the board after making the move
        });

        document.getElementById('move-form').reset();

    
    });
});



// Add JavaScript logic here to initialize and play the game based on the mode
if (mode === '2_player') {
    // Initialize game for two players
    console.log('2 player IS BOBBBY')
    console.log(difficulty)
} else if (mode === 'ai') {
    // Initialize game against AI
    console.log('AI IS BOBBY')
    console.log(difficulty)
    
}