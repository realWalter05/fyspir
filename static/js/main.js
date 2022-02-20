function SetToLS(name, data) {
    localStorage.setItem(name, data);
}

function FillInputsFromLs() {
    // Setting fullscreen of pudorys by local storage
    if (localStorage.getItem("showFullscreen") !== null) {
        if (localStorage.getItem("showFullscreen") === "true") {
            document.getElementById("fullscreenEnabler").click();
        }
    }

    // Setting reservation visibility by local storage
    if (localStorage.getItem("showReservations") !== null) {
        if (localStorage.getItem("showReservations") === "false") {
            document.getElementById("checkResEnabler").click();
        }
    }

    // Setting skipped imgs visibility by local storage
    if (localStorage.getItem("eng") !== null) {
        if (localStorage.getItem("eng") === "true") {
            document.getElementById("eng").click();
        }
    }


}
