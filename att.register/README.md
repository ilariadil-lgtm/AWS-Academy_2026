# atta
Progetto di gruppo del team AWS re/Start di Edgemony.

Taget
- utente che fa il ruolo di trainer
- utente che ha il ruolo di partecipante

Obiettivo:
- creare un'applicazione da linea di comando che permetta all'utente trainer di segnare assenze e presenze dei partecipanti a un corso
- permetta all'utente partecipante di vedere il proprio tasso percentuale di assenze e presenze

Problemi:
- quale database utilizzare?
    - CSV (locale)
    - Google Sheets (cloud)
        - API Google Sheets
        - potrebbe risolvere il problema di auth
        - come faccio a gestire i permessi in maniera tale che ogni partecipante possa vedere solo i suoi dati?
            - in base alla complessità implementativa, potrebbe essere utile partire con qualcosa che non richiede filtro dati per utente specifico
    - creo un db locale in un altro formato
- quale funzionalità implementare prima (mvp)?
- come stabilisco il ruolo dell'utente? 
    - non ho possibilità di mettere auth
        - potrebbe aver senso per il momento sviluppare solo uno dei due prodotti per uno specifico utente (target)