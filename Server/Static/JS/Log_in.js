
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST","/validate",true);
    xhr.setRequestHeader("Content-Type","application/json");
    xhr.send(JSON.stringify(username+"/"+password));
    console.log(xhr);
})