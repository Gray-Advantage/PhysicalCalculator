window.addEventListener("beforeunload", e => {
    navigator.sendBeacon("/close");
});
