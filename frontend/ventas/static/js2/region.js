//alert(888)
var url_reg = url_url + "/ventas/restfull/region/"
function regionLeer(){
    //alert("1==>"+url_reg)
    //var pathUrl= url_reg +  document.getElementById('txIdRegion').value
    var pathUrl= url_reg +  $("#txIdRegion").val()
    //alert("2==>"+pathUrl)
    $.ajax({
        type: "GET",      // GET, PUT, POST, DELETE
        async: false,      // Sincrónico
        url:pathUrl  ,  // Observe que agrego el rut
        cache: false,
        dataType: "json",  
        error: function (dataHarrys) {
            console.log("Eeror",dataHarrys)
        },
        success: function (dataHarrys) {
            console.log("Success",dataHarrys)
            document.getElementById('txCodigo').value = dataHarrys.codigo
            document.getElementById('txNombre').value = dataHarrys.nombre
        }
    })
}

function regionAgregar(){
        //alert("1==>"+url_reg)
    //var pathUrl= url_reg +  document.getElementById('txIdRegion').value
    var pathUrl= url_reg
    var dataRegion = ""
    dataRegion += "{"
    dataRegion += ' "codigo":"' + document.getElementById('txCodigo').value + '"';
    dataRegion += ',"nombre":"' + document.getElementById('txNombre').value+ '"';
    dataRegion += ',"idRegion":"' + document.getElementById('txIdRegion').value+ '"';
    dataRegion += "}"
    $.ajax({
        type: "POST",      // GET, PUT, POST, DELETE
        async: false,      // Sincrónico
        data:dataRegion,
        url:pathUrl  ,  // Observe que agrego el rut
        cache: false,
        dataType: "json",  
        error: function (dataHarrys) {
            console.log("Eeror",dataHarrys)
        },
        success: function (dataHarrys) {
            console.log("Success",dataHarrys)
            alert(dataHarrys)
        }
    })
}
function regionActualizar(){
    //alert("1==>"+url_reg)
//var pathUrl= url_reg +  document.getElementById('txIdRegion').value
var pathUrl= url_reg  +  $("#txIdRegion").val()
var dataRegion = ""
dataRegion += "{"
dataRegion += ' "codigo":"' + document.getElementById('txCodigo').value + '"';
dataRegion += ',"nombre":"' + document.getElementById('txNombre').value+ '"';
dataRegion += ',"idRegion":"' + document.getElementById('txIdRegion').value+ '"';
dataRegion += "}"
$.ajax({
    type: "PUT",      // GET, PUT, POST, DELETE
    async: false,      // Sincrónico
    data:dataRegion,
    url:pathUrl  ,  // Observe que agrego el rut
    cache: false,
    dataType: "json",  
    error: function (dataHarrys) {
        console.log("Eeror",dataHarrys)
    },
    success: function (dataHarrys) {
        console.log("Success",dataHarrys)
        alert(dataHarrys)
    }
})
}

function regionEliminar(){
    //alert("1==>"+url_reg)
    //var pathUrl= url_reg +  document.getElementById('txIdRegion').value
    var pathUrl= url_reg +  $("#txIdRegion").val()
    //alert("2==>"+pathUrl)
    $.ajax({
        type: "DELETE",      // GET, PUT, POST, DELETE
        async: false,      // Sincrónico
        url:pathUrl  ,  // Observe que agrego el rut
        cache: false,
        dataType: "json",  
        error: function (dataHarrys) {
            console.log("Eeror",dataHarrys)
        },
        success: function (dataHarrys) {
            console.log("Success",dataHarrys)
            alert(dataHarrys)
        }
    })
}