// document.addEventListener("DOMContentLoaded", function () {
//     const employeeForm = document.getElementById("employeeForm");
//     const employeeList = document.getElementById("employeeList");

//     employeeForm.addEventListener("submit", function (e) {
//         e.preventDefault();
//         const name = document.getElementById("name").value;
//         const position = document.getElementById("position").value;
//         const salary = document.getElementById("salary").value;

//         if (name && position && salary) {
//             const listItem = document.createElement("li");
//             listItem.innerHTML =  ` 
//                 <span>${name}</span>
//                 <span>${position}</span>
//                 <span>$${salary}</span>
//             `;
//             employeeList.appendChild(listItem);

//             // Clear input fields
//             document.getElementById("name").value = "";
//             document.getElementById("position").value = "";
//             document.getElementById("salary").value = "";
//         }
//     });
// });

 <script>
        // Get form and table elements
        const form = document.getElementById('employeeForm');
        const employeeTable = document.getElementById('employeeTable').getElementsByTagName('tbody')[0];

        // Add an event listener to the form for submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent page reload

            // Get values from the form
            const name = document.getElementById('name').value;
            const age = document.getElementById('age').value;
            const position = document.getElementById('position').value;
            const salary = document.getElementById('salary').value;

            // Create a new row
            const newRow = employeeTable.insertRow();

            // Insert cells and populate with employee data
            const cell1 = newRow.insertCell(0);
            const cell2 = newRow.insertCell(1);
            const cell3 = newRow.insertCell(2);
            const cell4 = newRow.insertCell(3);

            cell1.textContent = name;
            cell2.textContent = age;
            cell3.textContent = position;
            cell4.textContent = salary;

            // Clear the form inputs
            form.reset();
        });
    </script>