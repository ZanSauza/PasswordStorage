function toggleDetails(button) {
    const card = button.closest(".password-card");
    const details = card.querySelector(".password-details");
    details.classList.toggle("hidden");
}

function enableEdit(button) {
    const card = button.closest(".password-card");
    const table = card.querySelector("table");
    const cells = table.querySelectorAll("td");

    cells.forEach(cell => {
        cell.contentEditable = "true";
        cell.style.backgroundColor = "#fff2b2";
    });

    const saveBtn = card.querySelector(".save-btn");
    saveBtn.classList.remove("hidden");
}

