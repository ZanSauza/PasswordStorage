function toggleDetails(button) {
        const details = button.nextElementSibling;
        if (details.classList.contains('hidden')) {
            details.classList.remove('hidden');
            button.textContent = 'Скрыть';
        } else {
            details.classList.add('hidden');
            button.textContent = 'Показать';
        }
    }