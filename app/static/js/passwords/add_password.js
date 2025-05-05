async function addPassword(button) {
    const modal = document.querySelector("[data-modal-window='modal_window2']");
    modal.style.display = "block";


    const form = document.getElementById('add-password-form');
    form.onsubmit = null;

    form.onsubmit = async function (e) {
        e.preventDefault();

        const adDatedData =
            {
                site_name: document.getElementById('add_modal_site_name').value,
                user_name: document.getElementById('add_modal_user_name').value,
                password: document.getElementById('add_modal_password').value,
                email: document.getElementById('add_modal_email').value,
                phone_number: document.getElementById('add_modal_phone').value,
                site: document.getElementById('add_modal_site').value,
                note: document.getElementById('add_modal_note').value

        };
        console.log("Data to update:", adDatedData);

        try {
            const response = await fetch("/passwords/add_password/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(adDatedData)
            });

            const result = await response.json();
            console.log("Server response:", result);

            if (response.ok) {
                modal.style.display = "none";
                location.reload();
                localStorage.setItem("toastMessage", "Пароль Добавлен");

            } else {
                 modal.style.display = "none";
                location.reload();
                localStorage.setItem("toastMessage", "Пароль не был добавлен");
            }
        } catch (err) {
            console.error("Ошибка запроса:", err);
            alert("Ошибка сети");
        }
    };

    modal.querySelector(".close_modal_window").onclick = () => modal.style.display = "none";
}