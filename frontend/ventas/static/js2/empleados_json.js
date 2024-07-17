    // Definimos la parte fija de la Url
    var url_emp= url_url + '/ventas/backend/'    


//alert(22)
function listarDuenio() {
    //alert(222)
    let pathUrl = url_emp + "region/";
    $.ajax({
      type: "GET",
      async: false,
      url: pathUrl,
      cache: false,
      dataType: "json",
      beforeSend: function (data) {
        console.log('... cargando...');
      },
      error: function (data) {
        console.log('Tenemos problemas Houston ' + JSON.stringify(data));
      },
      success: function (data) {
        //alert(data)
        if (!data.OK) {
          alert(data.msg);
          return;
        }
        console.log(data)
        // Añadir la fila de títulos
        let tbConten = `<table border='1'>
          <tr>
          <td style="width:300px"></td>
            <th>Id</th>
            <th>Código</th>
            <th>Nombre</th>
          </tr>
        `;
  
        for (let i = 0; i < data.registro.length; i++) {
          let reg = data.registro[i];
          tbConten +="<tr>";
          tbConten += "<td style='width:300px'></td>"
          tbConten += "<td id='lblId'>" + reg.idRegion + "</td>";
          tbConten += "<td id='lblCod'>" + reg.codigo +"</td>";
          tbConten += "<td id='lblNom'>" + reg.nombre+ "</td>";
          tbConten +="</tr>";
        }
        tbConten += "</table>"
        console.log("tt",tbConten)
        document.getElementById("tbRegion").innerHTML= tbConten

      }
    });
  }