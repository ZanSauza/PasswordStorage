function toggleDetails(button) {
    const details = button.closest('.password-card').querySelector('.password-details');
    const editButton = button.previousElementSibling;

    details.classList.toggle('hidden');
    if (details.classList.contains('hidden')) {
        button.textContent = 'Показать';
        editButton.classList.add('hidden');
    } else {
        button.textContent = 'Скрыть';
        editButton.classList.remove('hidden');
    }
}

function copyToClipboard(inputId) {
    const input = document.getElementById(inputId);
    if (!input) return;

    input.select();
    input.setSelectionRange(0, 99999);

    try {
        const success = document.execCommand('copy');
        if (success) {
            showCopyToast("скопировано");
        } else {
            console.error("Не удалось скопировать");
        }
    } catch (err) {
        console.error("Ошибка копирования:", err);
    }

    window.getSelection().removeAllRanges();
}


function showCopyToast(message) {
    const toast = document.getElementById("copy-toast");
    toast.textContent = message;
    toast.classList.add("show");
    setTimeout(() => {
        toast.classList.remove("show");
    }, 2000);
}
