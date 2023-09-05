/**
 * Waits for the DOM content to be fully loaded and then applies specified styles.
 *
 * Once the DOM is ready, this function checks if specific colors have been defined.
 * If so, it applies these colors to various elements on the page, specifically:
 * - The background color of the page's main header (`<h1>` element).
 * - The background colors of cells in a checkerboard pattern.
 */
document.addEventListener("DOMContentLoaded", () => {
    
    // Extract colors from the globally defined 'colors' object.
    var color1 = colors.color1;
    var color2 = colors.color2;

    // Select all cells with class 'even' and 'odd', and the main header.
    var even = document.querySelectorAll(".even");
    var odd = document.querySelectorAll(".odd");
    var h1 = document.querySelector("h1");

    // If both colors are defined, apply them to the selected elements.
    if(color1 && color2) {
        
        // Set the background color of the main header to 'color1' and its text color to 'color2'.
        h1.style.backgroundColor = color1;
        h1.style.color = color2;

        // Apply 'color1' as the background color to all 'even' cells.
        even.forEach(cell => {
            cell.style.backgroundColor = color1;
        });
        
        // Apply 'color2' as the background color to all 'odd' cells.
        odd.forEach(cell => {
            cell.style.backgroundColor = color2;
        });
    }
});
