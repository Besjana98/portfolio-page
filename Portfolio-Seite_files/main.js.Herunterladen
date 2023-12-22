document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");
    var successMessage = document.getElementById("form-message-success");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Verhindert die tatsächliche Übermittlung des Formulars

        // Zeigen Sie die Erfolgsmeldung an und setzen Sie das Formular zurück
        successMessage.style.display = "block";
        form.reset();
    });
});
