function validateGuess() {
    const guessInput = document.getElementById("guess");
    const value = parseInt(guessInput.value);

    if (isNaN(value) || value < 1 || value > 100) {
        alert("Please enter a number between 1 and 100!");
        return false;
    }
    return true;
}
