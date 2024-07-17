ventana = new Ventana();

function Ventana(){
	var datosxx="";
    this.showHTML = function (objContainer,stPagina){
           $.ajax({
                  type: "GET",
                  url: stPagina ,
                  async: false,
                  cache: false,
                  //headers: "stHeader",
                  success: function (response) {
                        //alert("success" + response);
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
                  	      alert (msg)
                            datosxx = "Error " + msg
                            //wndMsgAlert("Error" + msg);
                            //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
                            datosxx=null;
                  }
            });
        document.getElementById(objContainer).innerHTML = datosxx;
    }
    this.getPostData = function (stPagina,stData){
           $.ajax({
                  type: "POST",
                  url: stPagina ,
                  async: false,
                  cache: false,
                  data : stData,
                  //headers: "stHeader",
                  //contentType: "application/json; charset=utf-8",
                  dataType : 'json',
                  success: function (response) {
                        //alert("success" + response);
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
                          alert (msg)
                            datosxx = "Error " + msg
                            //wndMsgAlert("Error" + msg);
                            //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
                            datosxx=null;
                  }
            });
        //document.getElementById(objContainer).innerHTML = datosxx;
        return datosxx;
    }
    this.getPostHtml = function (objContainer,stPagina,stData){
           $.ajax({
                  type: "POST",
                  url: stPagina ,
                  async: false,
                  cache: false,
                  data : stData,
                  //headers: "stHeader",
                  success: function (response) {
                        //alert("success" + response);
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
                          alert (msg)
                            datosxx = "Error " + msg
                            //wndMsgAlert("Error" + msg);
                            //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
                            datosxx=null;
                  }
            });
        document.getElementById(objContainer).innerHTML = datosxx;
    }    


    this.getDataCb = function (stPagina,cbCombo){
        $.ajax({
            type: "GET",      // GET, PUT, POST, DELETE
            async: false,      // Sincrónico
            url:stPagina  ,  // Observe que agrego el rut
            cache: false,
            dataType: "json",             // Formato de envio
            beforeSend: function (data){
                // Método de ejecuta antes de enviar
                console.log('... cargando...');
            }
            , error: function (data) {
                alert("Error " + data)
                //si hay un error mostramos un mensaje
                console.log('Tenemos problemas Houston ' +JSON.stringify(data));
            },
            success: function (data) {
                //alert("Success" + data)
                console.log("ventana",data)

                json = data;
                var opt = document.createElement('option');
                opt.value = -1;
                opt.innerHTML = "Seleccione";
                cbCombo.appendChild(opt);
        
                for(var x=0;x<data.registro.length;x++){
                       //alert(data[x].rut + ":" + data[x].nombre+ ":" + data[x].papellido) 
                        var opt = document.createElement('option');
                        opt.value = json.registro[x].idComuna;
                        opt.innerHTML = json.registro[x].nombre;
                        cbCombo.appendChild(opt);
                }
                //alert("carga comuna")
            }
        });
        
    }

}




