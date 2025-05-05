let btns = document.querySelectorAll("*[data-modal-btn]");

for(let i = 0; i<btns.length; i++) {
    btns[i].addEventListener('click', function () {
        let name = btns[i].getAttribute('data-modal-btn');
        let modal = document.querySelector("[data-modal-window='"+name+"']");
        modal.style.display = "block";
        let close = modal.querySelector(".close_modal_window");
        close.addEventListener('click', function () {
            modal.style.display = 'none'
        })
    })
}

window.onclick = function (e) {
    if(e.target.hasAttribute('data-modal-window')) {
        let modals = document.querySelectorAll("*[data-modal-window]")
        for(let i = 0; i<modals.length; i++) {
            modals[i].style.display = 'none'
        }
    }
}


async function editPassword(button) {

    const passwordCard = button.closest('.password-card');
    const passwordId = passwordCard.getAttribute('data-id');
    const modal = document.querySelector("[data-modal-window='modal_window1']");

    modal.style.display = "block";

    document.getElementById('modal_user_name').value = passwordCard.querySelector(`#user_name_${passwordId}`).value;
    document.getElementById('modal_password').value = passwordCard.querySelector(`#password_${passwordId}`).value;
    document.getElementById('modal_email').value = passwordCard.querySelector(`#email_${passwordId}`).value;
    document.getElementById('modal_phone').value = passwordCard.querySelector(`#phone_${passwordId}`).value;
    document.getElementById('modal_site').value = passwordCard.querySelector(`#site_${passwordId}`).value;
    document.getElementById('modal_note').value = passwordCard.querySelector(`#note_${passwordId}`).value;

    const form = document.getElementById('edit-password-form');
    form.onsubmit = null;

    form.onsubmit = async function (e) {
        e.preventDefault();

        const updatedData = {
            filters: { id: parseInt(passwordId) },
            updates: {
                user_name: document.getElementById('modal_user_name').value,
                password: document.getElementById('modal_password').value,
                email: document.getElementById('modal_email').value,
                phone_number: document.getElementById('modal_phone').value,
                site: document.getElementById('modal_site').value,
                note: document.getElementById('modal_note').value
            }
        };

        try {
            const response = await fetch("/passwords/update_password", {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(updatedData)
            });

            const result = await response.json();
            console.log("Server response:", result);

            if (response.ok) {
                modal.style.display = "none";
                location.reload();
                localStorage.setItem("toastMessage", "Пароль обновлён");

            } else {
                modal.style.display = "none";
                location.reload();
                localStorage.setItem("toastMessage", "Пароль не был обновлён");

            }
        } catch (err) {
            console.error("Ошибка запроса:", err);
            alert("Ошибка сети");
        }
    };

    modal.querySelector(".close_modal_window").onclick = () => modal.style.display = "none";
}


window.addEventListener("DOMContentLoaded", () => {
    const message = localStorage.getItem("toastMessage");
    if (message) {
        showCopyToast(message);
        localStorage.removeItem("toastMessage");
    }
});