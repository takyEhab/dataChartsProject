// Get the container element
var btnContainer = document.getElementById("myDIV");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("switcher-item");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("switcher-active-item");

    // If there's no active class
    if (current.length > 0) {
      current[0].className = current[0].className.replace("switcher-active-item", "");
    }

    // Add the active class to the current/clicked button
    this.className += " switcher-active-item";
  });
}
