function checkedFalse(id) {
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/ouvertime-record/checked-false/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (result) {
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#hours").text(result.hours);
        }
    });
}

function utilizouHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/ouvertime-record/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (result) {
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#hours").text(result.hours);
        }
    });
}

