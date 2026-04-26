const takeTestBtn = document.getElementById('takeTestBtn')
const testModal = document.getElementById('testModal')
takeTestBtn.addEventListener('click', () => {
    testModal.style.display = 'block'
})

const closeTestModal = document.getElementsByClassName('closeTest')
for (let i = 0; i < closeTestModal.length; i++) {
    closeTestModal[i].addEventListener('click', () => {
        testModal.style.display = 'none'
    })
}


const questions = [
    { q: "Are you over 18 years old?", a1: "Yes", a2: "No", score: 1 },
    { q: "Are you under 65 years old?", a1: "Yes", a2: "No", score: 1 },
    { q: "Do you weigh at least 50 kg?", a1: "Yes", a2: "No", score: 1 },
    { q: "Are you healthy at the moment?", a1: "Yes", a2: "No", score: 1 },
    { q: "Have you engaged in \"risky\" sexual activity in the last 12 months?", a1: "No", a2: "Yes", score: 1 },
    { q: "Have you been pregnant in the last six months?", a1: "No", a2: "Yes", score: 1 },
];

let currentStep = 0;
let totalScore = 0;

const container = document.getElementById('quiz-container');

function renderQuestion() {
    if (currentStep < questions.length) {
        const item = questions[currentStep];
        container.innerHTML = `
        
            <p>${item.q}</p>
        <div class="d-flex justify-content-evenly">
            <button onclick="nextStep(${item.score})" class="btn btn-outline-dark">${item.a1}</button>
            <button onclick="nextStep(0)" class="btn btn-outline-dark">${item.a2}</button>
        </div>
        `;
    } else {
        showResult();
    }
}

function nextStep(points) {
    totalScore += points;
    currentStep++;
    renderQuestion();
}

function showResult() {
    let message = totalScore >= 6 ? "You are suitable for donation!" : "You are <b>not</b> suitable for donation.";
    container.innerHTML = `<h4>Result: ${totalScore} point(s)</h4><p>${message}</p>
    <small>Refresh the page to retake the test</small>`;

}

// Запуск
renderQuestion();
