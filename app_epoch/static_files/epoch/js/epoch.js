function process_epoch() {
    var epoch_to_convert = document.getElementById("enter_epoch").value;
    /*var epoch_input_tz = document.getElementById('epoch_angular_epoch_tz').value; */
    var epoch_input_tz = document.getElementById('dropdown_selector_epoch').value;
    var dataString = '&time_to_convert=' + 'date_input' + '&epoch_to_convert=' + epoch_to_convert + '&tz_to_convert=' + epoch_input_tz;
    $.ajax({
        type: "GET",
        url: "/epoch.html",
        data: dataString,
        success: function (response) {
            var data = response;
            //var myTable = document.getElementById('myTable');
            document.getElementById("output_epoch_1").innerHTML = data.vara0;
            /* disabling table
            if ($(window).width() > 900) {
                for (var i = 1; i < 337; i++) {
                    var dyn_set = 'vara' + i;
                    myTable.rows[i].cells[1].innerHTML = data[dyn_set];
                }
            }
            */
        }
    });
    return false;
}

function onload_epoch() {
    var timezone = moment.tz.names();
    //alert(timezone);
    var tz_default = moment.tz.guess();
    $('select').append('<option value="' + tz_default + '">' + tz_default + '</option>');
    
    for (var i = 0; i < timezone.length; i++) {
        //alert(timezone[i]);
        $('select').append('<option value="' + timezone[i] + '">' + timezone[i] + '</option>');
    }
    $('select').selectpicker();

    var date_now = new Date();
    var time_now = date_now.getTime();
    var epoch_now = Math.round(time_now / 1000)
    document.getElementById("enter_epoch").defaultValue = epoch_now;
    document.getElementById("output_epoch_1").innerHTML = date_now;
    /*  Disabling ajax
    var epoch_to_convert = epoch_now;
    var epoch_input_tz = document.getElementById('dropdown_selector_epoch').value;
    var dataString = '&time_to_convert=' + 'date_input' + '&epoch_to_convert=' + epoch_to_convert + '&tz_to_convert=' + epoch_input_tz;
    $.ajax({
        type: "POST",
        url: "/epoch.html",
        data: dataString,
        success: function (response) {
            var data = response;
            var myTable = document.getElementById('myTable');
            if ($(window).width() > 900) {
                var myTable = document.getElementById('myTable');
                for (var i = 1; i < 337; i++) {
                    var dyn_set = 'vara' + i;
                    myTable.rows[i].cells[1].innerHTML = data[dyn_set];
                }
            }
        }
    });
    return false;
*/
    

}


function process_date() {
    var date_input = document.getElementById('datetimepicker1').value;
    var date_input_tz = document.getElementById("dropdown_selector_date").value;
    var dataString = '&time_to_convert=' + date_input + '&epoch_to_convert=' + 'datetoepoch' + '&tz_to_convert=' + date_input_tz;
    $.ajax({
        type: "GET",
        url: "/epoch.html",
        data: dataString,
        success: function (response) {
            var data = response;
            //var myTable = document.getElementById('myTable');
            document.getElementById('output_date_1').innerHTML = response.vara0;
            /* Disabling table
            if ($(window).width() > 900) {
                for (var i = 1; i < 337; i++) {
                    var dyn_set = 'vara' + i;
                    myTable.rows[i].cells[1].innerHTML = data[dyn_set];
                }
            } */
        }
    });
    return false;
}




$(document).ready(function () {
    $('#datetimepicker1').datetimepicker({
        defaultDate: new Date(),
        format: 'ddd,MMM DD,YYYY, hh:mm:ss A',
        sideBySide: true,
    });
    var date_input = document.getElementById('datetimepicker1').value;
    var date_input_epoch = moment(date_input, ["ddd,MMM DD,YYYY, hh:mm:ss A"]).unix();
    document.getElementById('output_date_1').innerHTML = date_input_epoch;
    $("#slow_loading").hide(), $("#slow_loading").delay(100).fadeIn(1000),

    $('#datetimepicker1').on('dp.change', function () {
        var date_input = document.getElementById('datetimepicker1').value;
        /*var date_input_tz = document.getElementById('epoch_angular_date_tz').value; */
        var date_input_tz = document.getElementById('dropdown_selector_date').value;
        var dataString = '&time_to_convert=' + date_input + '&epoch_to_convert=' + 'datetoepoch' + '&tz_to_convert=' + date_input_tz;
        $.ajax({
            type: "GET",
            url: "/epoch.html",
            data: dataString,
            success: function (response) {
                var data = response;
                document.getElementById('output_date_1').innerHTML = response.vara0;
                /* disable for table
                var myTable = document.getElementById('myTable');
                for (var i = 1; i < 337; i++) {
                    var dyn_set = 'vara' + i;
                    myTable.rows[i].cells[1].innerHTML = data[dyn_set];
                } */
            }
        });
        return false;
    });
});

