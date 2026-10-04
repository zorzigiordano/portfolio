import os

filepath = 'crm.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find everything inside cs-container
pattern = r'(?s)(<div class="cs-container">)(.*?)(</div>\s*<section id="contatti")'

replacement = r'''\1
        
        <!-- Image 1 -->
        <div class="cs-slide-banner fade-in-section">
            <img src="materiale/Database-normalizzato.webp" alt="Database Normalizzato" class="cs-slide-img">
            <div class="cs-slide-text">Analisi e normalizzazione del database</div>
        </div>

        <section class="cs-section fade-in-section">
            <h2 class="cs-section-title">Il contesto e la soluzione</h2>
            <p class="cs-text">
                Il punto di partenza era un basso numero di iscrizioni al corso di Full Stack Developer. La criticità principale risiedeva nella <strong>gestione frammentata dei dati</strong> (dispersi tra file Excel, piattaforme di Pubblica Amministrazione e moduli cartacei) e nella gestione completamente manuale dei candidati esclusi dagli altri percorsi.
            </p>
            <br>
            <p class="cs-text">
                Ho quindi strutturato un nuovo <strong>workflow automatizzato</strong>: un percorso strutturato per inviare e-mail mirate agli studenti esclusi, suggerendo loro l'iscrizione al corso di Full Stack Developer. Per migliorare le conversioni, ho immaginato un <em>touchpoint innovativo</em> in grado di raccogliere più adesioni e ho utilizzato Mailchimp per sviluppare il mockup della prima comunicazione ufficiale.
            </p>
        </section>

        <!-- Image 2 -->
        <div class="cs-slide-banner fade-in-section">
            <img src="materiale/Workflow_FullStack1.webp" alt="Workflow Full Stack" class="cs-slide-img">
            <div class="cs-slide-text">La struttura del nuovo workflow automatizzato</div>
        </div>

        <section class="cs-section fade-in-section">
            <h2 class="cs-section-title">[Titolo Sezione 2]</h2>
            <p class="cs-text">
                [Sostituisci questo testo con una descrizione dettagliata di questa fase del progetto. Puoi spiegare come funziona il workflow, quali sono i trigger per le e-mail o l'impatto atteso sui tassi di conversione.]
            </p>
        </section>

        <!-- Image 3 -->
        <div class="cs-slide-banner fade-in-section">
            <img src="materiale/crm1.png" alt="Mockup Mailchimp e Workflow" class="cs-slide-img">
            <div class="cs-slide-text">Mockup della prima comunicazione su Mailchimp</div>
        </div>

        <section class="cs-section fade-in-section">
            <h2 class="cs-section-title">Cosa ho imparato</h2>
            <p class="cs-text">
                [Sostituisci questo testo con le tue conclusioni sul caso studio CRM. Spiega i vantaggi dell'abbandono dei processi manuali in favore di logiche automatizzate e come questo touchpoint innovativo ha generato valore.]
            </p>
        </section>

    \3'''

new_content = re.sub(pattern, replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
