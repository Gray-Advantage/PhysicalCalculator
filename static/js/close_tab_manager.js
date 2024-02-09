const form = document.getElementById("form");
let isPost = false;

window.addEventListener("beforeunload", () => {
    if (!isPost) {
        navigator.sendBeacon("/close");
    }
});

form.addEventListener("submit", () => {
    isPost = true;
})
