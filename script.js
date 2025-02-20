document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('https://rztqndyln3.execute-api.ap-south-1.amazonaws.com/default/FetchFunction');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Fetched Data:", data); // Debugging: Check API response in console

        const tableBody = document.querySelector('#AttendTable tbody');
        if (!tableBody) {
            console.error("Error: Table body not found! Make sure you have a <tbody> in your HTML table.");
            return;
        }

        tableBody.innerHTML = ''; // Clear existing rows before adding new ones

        data.forEach(student => {
            const row = document.createElement('tr');

            const rollNoCell = document.createElement('td');
            const nameCell = document.createElement('td');
            const attendanceCell = document.createElement('td');

            rollNoCell.textContent = student.Rollno || "N/A"; // Ensure correct key
            nameCell.textContent = student.Name || "Unknown";
            attendanceCell.textContent = student.Count || "0";

            row.appendChild(rollNoCell);
            row.appendChild(nameCell);
            row.appendChild(attendanceCell);

            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Error fetching attendance data:", error);
    }
});
