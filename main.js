const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Body Parser Middleware, um Formulardaten zu verarbeiten
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/send-form', (req, res) => {
    // Hier würden Sie normalerweise die Daten in einer Datenbank speichern
    // oder eine E-Mail senden. Im Beispiel loggen wir die Daten einfach auf der Konsole.
    console.log('Name: ' + req.body.name);
    console.log('Email: ' + req.body.email);
    console.log('Message: ' + req.body.message);
    
    // Sie könnten dann eine Antwort an den Client zurücksenden
    // Zum Beispiel eine Bestätigungsseite oder eine Nachricht
    res.send('Formular wurde empfangen!');
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server läuft auf Port ${PORT}`);
});
