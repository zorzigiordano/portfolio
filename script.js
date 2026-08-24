document.addEventListener('DOMContentLoaded', () => {
    const banners = document.querySelectorAll('.cs-banner');

    function onScroll() {
        // Applichiamo l'effetto via JS solo su schermi piccoli dove il CSS fallisce
        if (window.innerWidth <= 768) {
            banners.forEach(banner => {
                const rect = banner.getBoundingClientRect();
                
                // Se il banner è visibile nello schermo
                if (rect.top < window.innerHeight && rect.bottom > 0) {
                    // Calcola la percentuale di scroll del banner rispetto allo schermo
                    const scrollPercent = (window.innerHeight - rect.top) / (window.innerHeight + rect.height);
                    
                    // Spostiamo la posizione dello sfondo dal 20% all'80% per un effetto parallasse morbido
                    const yPos = 20 + (scrollPercent * 60); 
                    banner.style.backgroundPosition = `center ${yPos}%`;
                }
            });
        } else {
            // Su desktop puliamo lo stile inline per lasciar fare al CSS (background-attachment: fixed)
            banners.forEach(banner => {
                banner.style.backgroundPosition = '';
            });
        }
    }

    // Richiediamo l'aggiornamento solo quando il browser è pronto a renderizzare il frame (ottimizzazione performance)
    window.addEventListener('scroll', () => {
        window.requestAnimationFrame(onScroll);
    });
    
    // Resize event per aggiustamenti se si gira il telefono
    window.addEventListener('resize', () => {
        window.requestAnimationFrame(onScroll);
    });

    // Avvio iniziale
    onScroll();
});
