# Product Specifications: Attendance Register CLI

## 1. Product Overview (Vision)
**Obiettivo:** Creare un'applicazione da linea di comando versatile per la gestione delle presenze in un corso.
L'applicazione deve servire due tipologie di utenti: chi gestisce il corso (Trainer) e chi frequenta (Partecipante), offrendo funzionalità mirate per ciascun ruolo.

## 2. Target Audience (Personas)

### 2.1. Trainer (Gestore)
*   **Responsabilità:** Monitoraggio e registrazione dati.
*   **User Story:** "Come Trainer, voglio poter segnare rapidamente le presenze giornaliere per l'elenco studenti, in modo da mantenere i registri aggiornati senza perdite di tempo."
*   **User Story:** "Come Trainer, voglio poter esportare o visualizzare un riepilogo per monitorare l'andamento della classe."

### 2.2. Partecipante (Studente)
*   **Responsabilità:** Consultazione.
*   **User Story:** "Come Partecipante, voglio vedere la mia percentuale di presenza/assenza attuale per sapere se sono in linea con i requisiti del corso."

## 3. Analisi Tecnica e Decisioni (Problem Solving)

### 3.1. Strategia Database (Dati)
**Problema:** Scegliere tra CSV Locale vs Cloud (Google Sheets).
*   **Decisione (Pivot):** **Google Sheets (Cloud)**.
    *   **Motivazione:** Il Trainer può inserire i dati direttamente dall'interfaccia web di Google Sheets, che è superiore a qualsiasi CLI in termini di velocità di input.
    *   **Ruolo della CLI:** La CLI diventa principalmente un tool di **consultazione (Read-Only)** per gli studenti (e opzionalmente reportistica avanzata per il trainer).

### 3.2. Privacy e Autenticazione (Il Problema API)
**Problema:** Come gestire i permessi in modo semplice senza backend complesso?
*   *Analisi Alternative Scartate:*
    *   *Permessi Row-Level:* Non supportati da Google Sheets.
    *   *Hub & Spoke (1 file per studente):* Scartata perché ingestibile per il Trainer (dovrebbe mantenere 20+ file sincronizzati).
*   **Decisione Finale (MVP):** **Client-Side Filtering (Privacy Debole)**.
    *   **Architettura:** Singolo Spreadsheet condiviso.
    *   **Funzionamento:** La CLI scarica l'intero dataset. Il software "filtra per id" (`stats --id 123`) solo a livello di interfaccia utente.
    *   **Compromesso:** Accettiamo che un utente smanettone possa tecnicamente vedere i dati altrui. Per il contesto target (classe/team), la facilità d'uso e sviluppo vince sulla sicurezza militare.

### 3.3. User Experience (Interattiva)
*   **Menu Navigabile:** L'applicazione non sarà una semplice comando "usa e getta" (flag-based), ma un programma interattivo che rimane attivo.
*   **Loop Principale:** All'avvio, l'utente vede un menu di opzioni (es. `1. Visualizza Statistiche`, `2. Altro...`, `3. Esci`).
*   **Scalabilità:** Questa struttura permette di aggiungere facilmente nuove funzionalità nel menu futuro senza complicare i flag di lancio.

## 4. Roadmap Funzionale (MVP)

Le funzionalità sono prioritizzate per sbloccare valore il prima possibile.

### Milestone 1: Core & Google Sheets Connection
*   Setup progetto.
*   Connessione Google Sheets (Link Pubblico CSV o Service Account).
*   **Engine:** La CLI scarica i dati e li filtra in memoria (es. Pandas) scartando le righe non pertinenti all'utente loggato.

### Milestone 2: Statistiche Partecipante (Interattiva)
*   Menu interattivo: Opzione "Le mie statistiche".
*   Input ID Studente (richiesto dal menu se non fornito all'avvio).
*   Output: Report formattato in tabella (Totale lezioni / Presenze / Assenze).

### Milestone 3: Reportistica Trainer (Opzionale)
*   Se necessario, comandi per generare report aggregati che Sheets non fa automaticamente.
