async function saveChanges(button) {
    const card = button.closest(".password-card");
    const id = card.getAttribute("data-id");
    const cells = card.querySelectorAll("td");

    const data = {
        filters: { id: parseInt(id) },
        updates: {
            user_name: cells[0].innerText.trim(),
            email: cells[1].innerText.trim(),
            password: cells[2].innerText.trim(),
            phone_number: cells[3].innerText.trim(),
            site: cells[4].innerText.trim(),
            note: cells[5].innerText.trim()
        }
    };

    console.log("Data to update:", data);

    const response = await fetch("/passwords/update_password", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result);
    alert(result.message);

    if (response.ok) {
        cells.forEach(cell => {
            cell.contentEditable = "false";
            cell.style.backgroundColor = "";
        });
        button.classList.add("hidden");
    }
}
