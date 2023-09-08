/**
 * This script adds event listeners to the "+2" and "reset" buttons.
 * Clicking the "+2" button redirects the user to the "/plus_two" route,
 * Clicking the "reset" button redirects to the "/destroy_session" route.
**/

// Get the "+2" button using its class name and add a click event listener to it.
// When clicked, the user will be redirected to the "/plus_two" route to increase the counter by two.
const plus_two = document.getElementsByClassName("btn-warning");
plus_two[0].addEventListener( "click", () => {
    location.href = "http://127.0.0.1:5000/plus_two";
}, false);

// Get the "reset" button using its class name and add a click event listener to it.
// When clicked, the user will be redirected to the "/destroy_session" route to reset the session counter.
const reset = document.getElementsByClassName("btn-danger");
reset[0].addEventListener( "click", () => {
    location.href = "http://127.0.0.1:5000/destroy_session";
}, false);
