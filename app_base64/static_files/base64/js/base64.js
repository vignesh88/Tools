function base64_convert() {
    var csrftoken = Cookies.get('csrftoken');
    var input_value = document.getElementById("default_input_data").value;
    if (document.getElementById('base64_decode').checked) {
        var input_type = "base64decode";
    } else if (document.getElementById('base64_encode').checked) {
        var input_type = "base64encode";
    }
    var dataString = '&input_value=' + input_value + '&input_type=' + input_type;
    $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        type: "POST",
        url: "/base64.html",
        data: dataString,
        success: function (response) {
            var data = response.final;
            document.getElementById("results").value = data;
        }
    });
    return false;
}

function base64_convert_enterkey(e) {
    if (e.keyCode == 13) {
        base64_convert();
    }
}

$(document).ready((function () {
    $("#slow_loading").hide(), $("#slow_loading").delay(100).fadeIn(1000) 
}));



