document.addEventListener('DOMContentLoaded', () => {
    fetch('https://0viq2ph712.execute-api.ap-south-1.amazonaws.com/default/FetchFunction')
    .then(response => response.json())
    .then(data => {
    const tableBody = document.querySelector('#attendanceTable tbody');
    data.forEach(student => {
    const row = document.createElement('tr');
    const rollNoCell = document.createElement('td');
    const nameCell = document.createElement('td');
    const attendanceCell = document.createElement('td');
    rollNoCell.text Content = student.Name;
    nameCell.textContent = student.Rollno;
    attendanceCell.textContent = student.Count;
    row.appendChild(rollNoCell);
    row.appendChild(nameCell);
    row.appendChild(attendanceCell);
    tableBody.appendChild(row);
    });
    })
    .catch(error => {
    console.error(error);
    });
    });
