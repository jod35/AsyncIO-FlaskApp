const login_btn=document.querySelector('#login-btn');
const login_form=document.querySelector('#login-form');

login_form.addEventListener('submit',showLoginAction);


function showLoginAction(){
    login_btn.value="Logging In";
    login_btn.style.backgroundColor="rgba(31, 180, 180, 0.191)";
    login_btn.style.color="teal";
    
    login_btn.style.fontWeight="bolder";
}