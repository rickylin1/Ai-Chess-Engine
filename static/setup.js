document.addEventListener('DOMContentLoaded', function() {
    var modeSelect = document.getElementById('mode');
    var difficultyDiv = document.getElementById('difficulty-div');

    modeSelect.addEventListener('change', function() {
        if (modeSelect.value === '2') {
            difficultyDiv.style.display = 'block';
        } else {
            difficultyDiv.style.display = 'none';
        }
    });

    var form = document.getElementById('game-setup-form');


    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission behavior
        const formData = new FormData(this)
        var mode = document.getElementById('mode').value;

        if (mode === '1') {
            fetch('/play_2_players', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    return response.text()
                } else {
                    throw new Error('Failed to make a POST request');
                }
            })
            .then(url => {
                window.location.href = url; // Redirect to the URL obtained from the response
            })
            .catch(error => console.error(error));
        }else if (mode === '2') {
            fetch('/play_ai', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                    console.log(response.json())
                } else {
                    throw new Error('Failed to make a POST request');
                }
            })
            .then(data => {
                window.location.href = data.mode; // Redirect to the URL obtained from the response
                console.log('mode is ' + data.mode)
                console.log(data.difficulty)
            })
            .catch(error => console.error(error));
        }
    });
});
