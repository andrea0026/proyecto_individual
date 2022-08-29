// contador de encuesta de satisfacción 
$(function () {
    $(".like").click(function () {
        var input = $(this).find('.qty1');
        input.val(parseInt(input.val())+ 1);
    });

    $(".neutral").click(function () {
        var input = $(this).find('.qty3');
        input.val(input.val() - 1);
    });

    $(".dislike").click(function () {
        var input = $(this).find('.qty2');
        input.val(input.val() - 1);
    });
});

//-seleccionar mes en el panel de produccion
$(function() {
    $('.date-picker').datepicker( {
    changeMonth: true,
    changeYear: true,
    showButtonPanel: false,
    dateFormat: 'mm-yy',
    onClose: function(dateText, inst) { 
        $(this).datepicker('setDate', new Date(inst.selectedYear, inst.selectedMonth, 1));
    }
    });
});