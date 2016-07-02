$(function() {
    $("#from_filter").change(function() {
        
        document.getElementById('to_filter').innerHTML = '' +
            '<select name="to_filter" id="to_filter">' +
                '<option value="PKR"> Pokhara </option>' +
                '<option value="BHW"> Bhairahawa </option>' +
            '</select>';
    });
});