document.addEventListener("DOMContentLoaded", loadSubjects);

function loadSubjects() {
    fetch("/api/subjects")
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("subjects");
        container.innerHTML = "";

        data.forEach(sub => {
            const total = sub.present + sub.absent;
            const card = document.createElement("div");
            card.className = "subject-card";

            card.innerHTML = `
                <div>
                    <b>${sub.name}</b><br>
                    Present: ${sub.present} | Total: ${total}
                </div>

                <div>
                    <button class="btn" onclick="editSubject(${sub.id})">Edit</button>
                    <button class="btn btn-secondary" onclick="deleteSubject(${sub.id})">Delete</button>
                </div>
            `;

            container.appendChild(card);
        });
    });
}

function editSubject(id){
    window.location.href = "/edit/" + id;
}

function deleteSubject(id){
    fetch("/api/subjects/" + id, {method:"DELETE"})
    .then(()=> loadSubjects());
}
