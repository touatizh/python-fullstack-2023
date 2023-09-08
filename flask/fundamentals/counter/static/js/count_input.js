/**
 * This script listens for the 'Enter' key to be pressed while the user is focused on a specific input element.
 * When the 'Enter' key is detected, it retrieves the count value from the current-count's text content,
 * increments it by the value entered in the input field, and updates both the current count on the page and a session variable
 * on the server with the new count.
**/

// Get the input element and the current count paragraph element from the DOM
const input = document.getElementById("increment");
const paragraph = document.getElementsByTagName("p")[0];

// Split the text content of the paragraph into two words: count value + suffix
let countPhrase = paragraph.textContent.split(" ");

// Add an event listener to detect when the 'Enter' key is pressed in the input field
input.addEventListener("keyup", (p) => {
    // If the 'Enter' key is detected
    if (p.key === 'Enter') {

        let count = parseInt(countPhrase[0]);
        let increment = parseInt(input.value);
        
        // If the increment value is a valid number
        if (!isNaN(increment)) {

            count += increment;
            
            // Update the current count with the new count
            countPhrase[0] = count;
            
            // Update the text content of the paragraph with the modified phrase
            paragraph.textContent = countPhrase.join(" ");
            
            // Send a POST request to the server with the new count as JSON data
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ count: count }),
            })
            .then(response => console.log(response.statusText))
            .catch(error => console.error('Error:', error));
        }
    }
});
