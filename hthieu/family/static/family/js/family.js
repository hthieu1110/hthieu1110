$(function() {
    $('form.delete .btnDelete').bind('click', function() {
        if (confirm('Are you sure for delete?')) {
            $(this).parent('form.delete').submit();
        }
    })
});