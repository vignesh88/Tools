function copyToClipboard(x,y) {
    if( document.getElementById(x).value) {
        data_2_copy = document.getElementById(x).value;
    } else {
        data_2_copy = document.getElementById(x).innerText;
    }

    var e = document.createElement("textarea");
    e.style.opacity = "0", e.style.position = "fixed", e.textContent = data_2_copy;
    var t = document.getElementsByTagName("body")[0];
    t.appendChild(e), e.select(), document.execCommand("copy"), t.removeChild(e), $(y).show(), setTimeout((function () {
        $(y).hide()
    }), 1e3)
}