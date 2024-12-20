// Example song and answers data
const quizData = {
    question: "Bohemian Rhapsody",
    correctAnswer: "Queen",
    options: ["Queen", "The Beatles", "Led Zeppelin", "Pink Floyd"]
};

// Check if the selected answer is correct
function checkAnswer(button) {
    const resultMessage = document.getElementById("result-message");
    if (button.textContent === quizData.correctAnswer) {
        resultMessage.textContent = "Correct! 🎉";
        resultMessage.style.color = "green";
    } else {
        resultMessage.textContent = "Wrong! Try again.";
        resultMessage.style.color = "red";
    }
}
