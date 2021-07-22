let counter = 0;

function count() {
    counter++;
    document.querySelector("h1").innerHTML = counter;
    if (counter % 10 == 0) alert(`Counter is now ${counter}`);
}

// Add event listener to the entire document.
// DOMContentLoaded: perform action when entire web page is fully loaded.
// document.addEventListener() accepts two arguments, one is event and two is the name of the function to be executed. Can put anonymous function also.
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count; // Access and assign event-handler/command, not calling function that's why we didn't put the set of parenthesis.
});