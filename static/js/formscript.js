jQuery(document).ready(function() {
    $('#add-to-cart').submit(function() {
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            dataType: 'json',
            success: function(json) {
            window.location.href = "http://www.page-2.com";
            }
        })
        return false;
    });
});