function deletePassword(button) {
    const card = button.closest(".password-card");
    const id = card.getAttribute("data-id");
    if (confirm("Удалить этот пароль?")) {
        fetch(`/passwords/delete/${id}`, {
            method: "DELETE"
        }).then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert("Ошибка при удалении");
            }
        }).catch(err => {
            console.error("Ошибка удаления:", err);
        });
    }
}