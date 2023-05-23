sendButton.addEventListener("click", () => {
    questionInput = document.getElementById('questionInput').value;
    document.getElementById('questionInput').value="";
    document.querySelector(".right2").style.display = "block";
    document.querySelector(".right1").style.display = "none";

    question1.innerHTML = questionInput
    question2.innerHTML = questionInput

    // Get the answer and populate it


})