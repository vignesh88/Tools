function onload_password_generate() {
    var e = "&U_case=ON&L_case=ON&S_chars=OFF&Num_value=ON&slider_range=12&lazy_words=";
    return $.ajax({
        type: "GET",
        url: "/password_generator.html",
        data: e,
        success: function (e) {
            var t = e.password;
            document.getElementById("password").innerHTML = t
        }
    }), !1
}

function password_generate() {
    var e = document.getElementById("myRange").value,
        lazy_words = document.getElementById("lazy_words_text").value;
    if (document.getElementById("U_case").checked) var t = "ON";
    else t = "OFF";
    if (document.getElementById("L_case").checked) var a = "ON";
    else a = "OFF";
    if (document.getElementById("S_chars").checked) var n = "ON";
    else n = "OFF";
    if (document.getElementById("Num_value").checked) var c = "ON";
    else c = "OFF";
    var d = "&U_case=" + t + "&L_case=" + a + "&S_chars=" + n + "&Num_value=" + c + "&slider_range=" + e + "&lazy_words=" + lazy_words;
    return $.ajax({
        type: "GET",
        url: "/password_generator.html",
        data: d,
        success: function (e) {
            var t = e.password;
            if (lazy_words) {
                var word_a = e.word_list,
                    x;
                 
                word_a.length = 4, document.getElementById("lazy_words_suggestion").innerHTML = word_a + "...", (x = document.getElementById("lazy_words_suggestion_p")).style.display = "block"
            } else {
                var x;
                (x = document.getElementById("lazy_words_suggestion_p")).style.display = "none"
            }
            document.getElementById("password").innerHTML = t
        }
    }), !1
}


function disableOnlyCheckbox() {
    let e = [uppercaseEl, lowercaseEl, numberEl, symbolEl].filter(e => e.checked);
    e.forEach(t => {
        1 == e.length ? t.disabled = !0 : t.disabled = !1
    })
}
const uppercaseEl = document.getElementById("U_case"),
    lowercaseEl = document.getElementById("L_case"),
    numberEl = document.getElementById("Num_value"),
    symbolEl = document.getElementById("S_chars");

function check_key(e) {
    32 == e.keyCode && alert("Only singe word is supported!"), 13 == e.keyCode && password_generate()
} [uppercaseEl, lowercaseEl, numberEl, symbolEl].forEach(e => {
    e.addEventListener("click", () => {
        disableOnlyCheckbox()
    })
}), $(document).ready((function () {
    $("#slow_loading").hide(), $("#slow_loading").delay(100).fadeIn(1000)

})), document.getElementById("lazy_words_text").parentNode.addEventListener("keydown", check_key, !1), superplaceholder({
    el: document.getElementById("lazy_words_text"),
    sentences: ["Type word e.g. 'Water'", "Generate password by word!!!" ],
    options: {
        letterDelay: 300,
        sentenceDelay: 3e3,
        autoStart: !0,
        loop: !0,
        shuffle: !1,
        showCursor: !0,
        cursor: "|",
        onFocusAction: superplaceholder.Actions.STOP
    }
});
var slider = document.getElementById("myRange"),
    output = document.getElementById("myRange-display");
output.innerHTML = slider.value, slider.oninput = function () {
    output.innerHTML = this.value
}, onload_password_generate();