let counter = 0; // Declaring and initializing a variable by let keyword.

function count() {
    counter++;
    document.querySelector("h1").innerHTML = counter;
    if (counter % 10 == 0) alert(`Counter is now ${counter}`); // Close similar to Python(extra: backtic and a dollar sign) or we can do exactly similar like Java - alert('Counter is now ' + counter)
}
