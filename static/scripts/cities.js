function toggleColour(event) {
    if (event.currentTarget.style.backgroundColor == event.currentTarget.style.borderColor) {
        event.currentTarget.style.backgroundColor = "#614c22";
    } else {
        event.currentTarget.style.backgroundColor = event.currentTarget.style.borderColor;
    }
}    

document.querySelectorAll(".city").forEach(f => {
    f.addEventListener("click", toggleColour);
})