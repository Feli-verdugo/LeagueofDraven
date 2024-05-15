function validarUsuario() {
    let user = document.querySelector("#user");
    let poseeNumero = /\d/.test(user.value); 
    let contieneEspacio = /\s/.test(user.value); 
    let formatoPermitido = /^[a-zA-Z0-9._-]+$/i.test(user.value);

    if(user.value.length >= 6 && formatoPermitido && poseeNumero){
        user.classList.add("correct");
        user.classList.remove("incorrect");
        document.querySelector("#error-user").innerHTML = "&nbsp;";
    }else{
        user.classList.add("incorrect");
        user.classList.remove("correct");
        
        if (user.value.length < 6) {
            document.querySelector("#error-user").innerHTML = "Error, ingrese minimo 6 caracteres!.";
        } else if (!poseeNumero) {
            document.querySelector("#error-user").innerHTML = "Error, el usuario debe contener al menos un número.";
        } else if (!formatoPermitido) {
            document.querySelector("#error-user").innerHTML = "Error, el formato esta mal, intente con '.' o '_' para los espacios";
        } else if (!contieneEspacio) {
            document.querySelector("#error-user").innerHTML = "Error, usuario no puede tener espacios";
        } 

    } 
}




function validarNombre() {
    let user = document.querySelector("#nombre");
    let contieneNumeros = /\d/.test(nombre.value); 
    if(user.value.length <= 40 && !contieneNumeros){
        user.classList.add("correct");
        user.classList.remove("incorrect");
        document.querySelector("#error-nombre").innerHTML = "&nbsp;";
    }else{
        user.classList.add("incorrect");
        user.classList.remove("correct");
        document.querySelector("#error-nombre").innerHTML = "Error, El nombre no puede sobrepasar el maximo de digitos.";
        if (contieneNumeros) {
            document.querySelector("#error-nombre").innerHTML = "Error, El nombre no puede contener numeros."
        } 
    } 
}



function validarContrasena() {
    let password = document.querySelector("#password");
    let contieneMayuscula = /[A-Z]/.test(password.value);
    let tieneEspacio = /\s/.test(password.value);
    let contieneNumero = /\d/.test(password.value); 
    let formatoaceptado = /^[a-zA-Z0-9._-]+$/i.test(password.value);

    if (password.value.length >= 5 && contieneMayuscula && contieneNumero && formatoaceptado) { 
        password.classList.add("correct");
        password.classList.remove("incorrect");
        document.querySelector("#error-password").innerHTML = "&nbsp;";
    } else {
        password.classList.add("incorrect");
        password.classList.remove("correct");
        if (password.value.length < 5) {
            document.querySelector("#error-password").innerHTML = "Error, la contraseña debe tener al menos 5 o mas caracteres.";
        } else if (!contieneMayuscula) {
            document.querySelector("#error-password").innerHTML = "Error, la contraseña debe contener al menos una letra mayúscula.";
        } else if (!contieneNumero) {
            document.querySelector("#error-password").innerHTML = "Error, la contraseña debe contener al menos un número.";
        } else if (!tieneEspacio) {
            document.querySelector("#error-password").innerHTML = "Error, la contraseña no puede tener espacios";
        } else if (!formatoaceptado) {
            document.querySelector("#error-password").innerHTML = "Error, el formato esta mal, intente con '.' o '_' para los espacios";
        }
    }
}



function validarConfirmarContrasena() {
    let password = document.querySelector("#password");
    let confirmPassword = document.querySelector("#confirm-password");

    if (confirmPassword.value === password.value) { 
        confirmPassword.classList.add("correct");
        confirmPassword.classList.remove("incorrect");
        document.querySelector("#error-confirm-password").innerHTML = "&nbsp;";
    } else {
        confirmPassword.classList.add("incorrect");
        confirmPassword.classList.remove("correct");
        document.querySelector("#error-confirm-password").innerHTML = "Error, las contraseñas no coinciden.";
    }
}




function validarCorreo() {
    let email = document.querySelector("#gmail");
    let formatoValido = /^[a-zA-Z0-9._-]+@gmail\.(com|cl)$/i.test(email.value);

    if (formatoValido) {
        email.classList.add("correct");
        email.classList.remove("incorrect");
        document.querySelector("#error-gmail").innerHTML = "&nbsp;";
    } else {
        email.classList.add("incorrect");
        email.classList.remove("correct");
        document.querySelector("#error-gmail").innerHTML = "Error, el correo es invalido, tiene que terminar en '@gmail.com' o '@gmail.cl'.";
    }
}



