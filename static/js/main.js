// Initialize HTMX
document.addEventListener('DOMContentLoaded', function() {
    // Handle tab switching
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', function() {
            const tabName = this.dataset.tab;
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            
            htmx.ajax('GET', `/admin/${tabName}/`, {
                target: '#main-content',
                swap: 'innerHTML'
            });
        });
    });

    // Task timer functionality
    function updateTimers() {
        document.querySelectorAll('.order-timer').forEach(timer => {
            const endTime = parseInt(timer.dataset.endTime);
            const now = Math.floor(Date.now() / 1000);
            const diff = endTime - now;
            
            if(diff > 0) {
                const hours = Math.floor(diff / 3600);
                const minutes = Math.floor((diff % 3600) / 60);
                const seconds = diff % 60;
                timer.textContent = `⏳ ${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            } else {
                timer.textContent = '⏰ Time Expired!';
                timer.style.color = 'var(--accent)';
            }
        });
    }
    setInterval(updateTimers, 1000);

    // Audio notification for new orders
    const alertSound = new Audio('/static/media/alert.mp3');
    htmx.on('htmx:afterSwap', function(evt) {
        if(evt.detail.target.id === 'main-content') {
            if(evt.detail.triggeringEvent?.detail?.newOrder) {
                alertSound.play();
            }
        }
    });

    // Shift popup handling
    function checkShiftStatus() {
        htmx.ajax('GET', '/team/shift-status/', {
            target: '#main-content',
            swap: 'beforeend'
        });
    }
    checkShiftStatus();
});

// HTMX Configuration
htmx.config.defaultSwapStyle = 'outerHTML';
htmx.config.globalViewTransitions = true;
htmx.config.useTemplateFragments = true;