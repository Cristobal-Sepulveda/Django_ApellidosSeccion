let listadoDeProductos = [];

//esta funcion agrega al carrito un producto....
const agregarAlCarrito = (nombre, precioUnitario) => {
  //obtengo los strings...
  const auxNombre = nombre.innerText;
  const auxPrecioUnitario = parseInt(
    precioUnitario.innerText.slice(1).replace(".", "")
  );

  //creo el objeto
  const productoAIngresar = {
    nombre: auxNombre,
    precioUnitario: auxPrecioUnitario,
    cantidad: 1,
    precioPorCantidad: auxPrecioUnitario,
  };

  /*El parametro del switch checkea si hay coinsidencias de nombre en el array
      listadoDeProductos */
  switch (
    listadoDeProductos.filter((producto) => producto.nombre === auxNombre)
      .length
  ) {
    /* Si el producto no esta en el carrito, lo añado*/
    case 0:
      alert("Producto añadido al carrito");
      listadoDeProductos.push(productoAIngresar);
      break;

    /* Si el producto ya esta en el carrito...*/
    case 1:
      for (const producto of listadoDeProductos) {
        if (producto.nombre === auxNombre) {
          producto.cantidad++;
          producto.precioPorCantidad += auxPrecioUnitario;
        }
      }
      alert("Producto sumado en el carrito");
      break;

    /* Para debugear(por si hay mas de un producto con el mismo nombre, dado
           que nombre es el "uuid" para la logica de codigo en los casos anteriores */
    default:
      alert("HAY ERRORES EN LA LOGICA!!");
  }
};

const obtenerElListadoDeProductosEnElCarrito = () => {
  return listadoDeProductos;
};

const irATransbank = () => {
  if (listadoDeProductos.length !== 0) {
    window.location.href =
      "https://www.webpay.cl/portalpagodirecto/pages/institucion.jsf?idEstablecimiento=86480605";
  }
};
const desapareceImagen = (document) => {
  document.getElementById("imagenCarrito").style.width = "50px";
  document.getElementById("imagenCarrito").style.height = "50px";
};

const reapareceImagen = (document) => {
  document.getElementById("imagenCarrito").style.width = "80%";
  document.getElementById("imagenCarrito").style.height = "350px";
};

const requestAAPI = async (document) => {
  try {
    let response = await fetch("https://mindicador.cl/api");
    let data = await response.json();
    document.getElementById("precioUF").innerHTML = data.uf.valor;
    return data;
  } catch (error) {
    console.log("Looks like there was a problem: ", error);
  }
};

const dibujadoraDeTablaEnCarrito = () => {
  let dibujadora = obtenerElListadoDeProductosEnElCarrito();
  if (dibujadora.length === 0) {
    return;
  }
  //limpio la tabla, así no habrá duplicidad de filas.
  $("#tablaDelCarrito").find("tbody tr").remove();

  let count = 1;
  let totalAPagar = 0;
  for (const element of dibujadora) {
    $("#tablaDelCarrito")
      .find("tbody")
      .append(
        "<tr>" +
          '<th scope="row">' +
          count +
          "</th>" +
          "<td>" +
          element.nombre +
          "</td>" +
          "<td>" +
          element.cantidad +
          "</td>" +
          "<td>" +
          element.precioUnitario +
          "</td>" +
          "<td>" +
          element.precioPorCantidad +
          "</td>" +
          "</tr>"
      );
    totalAPagar = totalAPagar + element.precioPorCantidad;
    count++;
  }

  $("#tablaDelCarrito")
    .find("tbody")
    .append(
      "<tr>" +
        '<th style="border-bottom:0px" scope="row"></th>' +
        '<td style="border-bottom:0px"></td>' +
        '<td style="border-bottom:0px"></td>' +
        '<td class="totalEnTabla" style="background-color:lightgrey;">Total:</td>' +
        '<td class="totalEnTabla" style="background-color:lightgrey;">' +
        totalAPagar +
        "</td>" +
        "</tr>"
    );
};
