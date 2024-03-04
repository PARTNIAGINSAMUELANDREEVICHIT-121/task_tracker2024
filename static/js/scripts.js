// static/js/scripts.js

$(document).ready(function() {
    $('#id_priority').change(function() {
        var color = '';
        switch ($(this).val()) {
            case 'low':
                color = 'priority-low';
                break;
            case 'medium':
                color = 'priority-medium';
                break;
            case 'high':
                color = 'priority-high';
                break;
            default:
                color = '';
        }
        $(this).removeClass().addClass(color);
    });

    $('#id_status').change(function() {
        var color = '';
        switch ($(this).val()) {
            case 'new':
                color = 'status-new';
                break;
            case 'in-progress':
                color = 'status-in-progress';
                break;
            case 'done':
                color = 'status-done';
                break;
            case 'cancelled':
                color = 'status-cancelled';
                break;
            case 'postponed':
                color = 'status-postponed';
                break;
            default:
                color = '';
        }
        $(this).removeClass().addClass(color);
    });
});
