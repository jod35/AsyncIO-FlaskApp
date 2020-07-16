const signup_form=document.querySelector('#signup-form');
const signup_btn=document.querySelector('#signup-btn');

//handle the sign up form
signup_form.addEventListener('submit',showSignUpAction);


function showSignUpAction(){
    console.log("Hello");
    signup_btn.style.backgroundColor="rgba(31, 180, 180, 0.191)";
    signup_btn.style.color="teal";
    signup_btn.value="Signing Up";
    signup_btn.style.fontWeight="bolder";

}