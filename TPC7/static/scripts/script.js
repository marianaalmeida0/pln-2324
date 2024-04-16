
function delete_conceito(designacao){
$.ajax({
    url:'/conceitos/'+ designacao,
    type:'DELETE',
    success: function (result) {
        console.log(result)
        window.location.href = "/conceitos"
    }
});
}

$(document).ready( function () {
    $('#myTable').DataTable(); // procura o elemento q tiver com id myTable
} );