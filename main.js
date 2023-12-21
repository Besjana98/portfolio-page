document.addEventListener("DOMContentLoaded", function() {
    // Funktion, um eine Willkommensnachricht anzuzeigen
    function showWelcomeMessage() {
        alert("Willkommen auf Besjana Latifi's Portfolio-Seite!");
    }

    // Button-Event-Listener hinzufügen
    var welcomeButton = document.getElementById("welcomeButton");
    if (welcomeButton) {
        welcomeButton.addEventListener("click", showWelcomeMessage);
    }
});
