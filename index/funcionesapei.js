async function getProductos(){
    let response = await fetch("https://api.escuelajs.co/api/v1/products/?categoryId=2");
    let items = await response.json();
    

    let productos = document.querySelector("#productos");

    for(let item of items){
        let producto = document.createElement("div");
        producto.classList.add("producto");
        
        let url = item.images[0].replaceAll("[","").replaceAll("]","").replaceAll("\"","")

        let imagen = document.createElement("div");
        imagen.classList.add("imagen")        
        imagen.style.backgroundImage = "url(" + url + ")";
        producto.appendChild(imagen);

        let nombre = document.createElement("div");
        nombre.classList.add("nombre")        
        nombre.innerHTML = item.title;
        producto.appendChild(nombre);
        
        let precio = document.createElement("div");
        precio.classList.add("precio")        
        precio.innerHTML = item.price;
        producto.appendChild(precio);





        productos.appendChild(producto);
        }
}