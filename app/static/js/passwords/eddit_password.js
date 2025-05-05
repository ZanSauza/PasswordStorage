function openModal(password) {
    document.getElementById("edit-id").value = password.id;
    document.getElementById("edit-username").value = password.user_name || "";
    document.getElementById("edit-email").value = password.email || "";
    document.getElementById("edit-password").value = password.password || "";
    document.getElementById("edit-phone").value = password.phone_number || "";
    document.getElementById("edit-site").value = password.site_name || "";
    document.getElementById("edit-note").value = password.note || "";

    document.getElementById("editModal").classList.remove("hidden");
}

function closeModal() {
    document.getElementById("editModal").classList.add("hidden");
}

async function submitEdit() {
    const id = parseInt(document.getElementById("edit-id").value);
    const user_name = document.getElementById("edit-username").value;
    const email = document.getElementById("edit-email").value;
    const password = document.getElementById("edit-password").value;
    const phone_number = document.getElementById("edit-phone").value;
    const site_name = document.getElementById("edit-site").value;
    const note = document.getElementById("edit-note").value;



    const payload = {
        filters: { id },
        updates: {
            user_name,
            email,
            password,
            phone_number,
            site_name,
            note
        }
    };
        console.log("Data to update:", payload);

    try {
        const response = await fetch("/passwords/update_password", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            closeModal();
            location.reload();
        }
    } catch (err) {
        alert("Ошибка при сохранении");
        console.error(err);
    }
}
