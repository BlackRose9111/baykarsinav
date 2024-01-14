$(document).ready(function () {
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);

    var parametre1 = urlParams.get('page');

    // Check if parametre1 is not null and the element with that ID exists
    if (parametre1 && document.getElementById(parametre1)) {
        document.getElementById(parametre1).classList.add("active");
    }
});