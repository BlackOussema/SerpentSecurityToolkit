// This file contains JavaScript code for client-side functionality. 

document.addEventListener('DOMContentLoaded', function() {
    // Example function to handle form submission
    const form = document.getElementById('exampleForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            // Handle form submission logic here
            console.log('Form submitted!');
        });
    }

    // Example function to fetch data from the server
    function fetchData() {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                console.log('Data fetched:', data);
                // Update the UI with the fetched data
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Call fetchData on page load
    fetchData();
});