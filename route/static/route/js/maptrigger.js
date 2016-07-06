
$(function() {
    $("#from_filter").change(function() {
        var val = $('option:selected', this).val();
        $.get( "/route/getdestination/",'from_filter='+ val, function(data) {
            var to_filter = data.to_filter;
            if (to_filter != null){
                $("#to_filter").replaceWith('<select id="to_filter"></select>');
                $('#to_filter').append("<option value=" + to_filter + ">" + to_filter + "</option>");
            }
        });
    });
});