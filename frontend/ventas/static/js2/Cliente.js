var url_api= 'http://localhost:9010/ventas/backend'    
    //var lo_path = 'persona/'
    var lo_path = 'cliente/'

    function clienteLeer(){
        alert("leyendooo")
        var pathUrl= url_api + lo_path +  document.getElementById('txRut').value
        $.ajax({
            
            type: "GET",      // GET, PUT, POST, DELETE
            async: false,      // Sincrónico
            url:pathUrl  ,  // Observe que agrego el rut
            cache: false,
            dataType: "json"
            , error: function (data) {
                console.log('Tenemos problemas Houston ' +JSON.stringify(data));
            }
            ,success: function (data) {
                json = data;
                if (!json.OK){
                    alert(json.msg)
                    return
                }
                document.getElementById('txNombres').value = json.registro.nombre
            }
        })
    
    }



    function ClienteeLeer(){
        
        // No Tiene parametros
        //*********** Ejecuto Ajax Sincrónico
        var pathUrl= url_api + lo_path +  document.getElementById('txRut').value
        $.ajax({
            type: "GET",      // GET, PUT, POST, DELETE
            async: false,      // Sincrónico
            url:pathUrl  ,  // Observe que agrego el rut
            cache: false,
            //contentType: "application/json; charset=utf-8",
            // crossDomain:true,  // Si no se coloca da error, diferentes host
            // headers: { // Bloqueado por CORS
            //         'Access-Control-Allow-Origin': '*',
            //         'Accept': 'application/json',
            //         'Content-Type': 'application/json;charset=UTF-8',
            //         'Access-Control-Allow-Methods': '*',
            //         'Access-Control-Allow-Headers': 'Access-Control-Allow-Headers, Content-Type, Authorization',
            //         },            
            //format: "json",

            dataType: "json",             // Formato de envio
            beforeSend: function (data){
                // Método de ejecuta antes de enviar
                console.log('... cargando...');
            }
            , error: function (data) {
                alert("Error " + data)
                //si hay un error mostramos un mensaje
                console.log('Tenemos problemas Houston ' +JSON.stringify(data));
                // No es Totalmente cierto, ya que puede ser error
                document.getElementById('txDv').value = "9"
                document.getElementById('txNombres').value = ""
                document.getElementById('txPaterno').value = ""
                document.getElementById('txMaterno').value = ""
                document.getElementById('txEMail').value = ""
                document.getElementById('cbComuna').value = 1
                habilitaLeer()
            },
            success: function (data) {
                //alert("Success" + data)
                json = data;
                // Si no es Ok envia Mensaje
                if (!json.OK){
                    alert(json.msg)
                    return
                }
                document.getElementById('txDv').value = json.registro.dv
                document.getElementById('txNombres').value = json.registro.nombre
                document.getElementById('txPaterno').value = json.registro.papellido
                document.getElementById('txMaterno').value = json.registro.sapellido
                document.getElementById('txEMail').value = json.registro.email
                document.getElementById('cbComuna').value = json.registro.comuna
                document.getElementById('cbGenero').value = json.registro.genero
                habilitaLeer()
            }
        });
    }