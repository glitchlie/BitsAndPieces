

//document.getElementsByName("registration-submit-btn")[0].addEventListener("click", submitReistrationData());

const firstName = document.getElementsByName("reg-input-firstname")[0];
const secondName = document.getElementsByName("reg-input-middlename")[0];
const lastName = document.getElementsByName("reg-input-lastname")[0];

const email = document.getElementsByName("reg-input-email")[0];

const passwd = document.getElementsByName("reg-input-passwd")[0];
const passwdConfirm = document.getElementsByName("reg-input-passwd-confirm")[0];


function checkPwd() {
	passwd.value.length < 8 ? passwd.style.backgroundColor = "rgba(255,0,0,0.4)" : 
							  passwd.style.backgroundColor = "rgba(255,255,255,0.4)";
}

function checkPwdMatch() {
	passwd.value !== passwdConfirm.value ? passwdConfirm.style.backgroundColor = "rgba(255,0,0,0.4)" : 
										   passwdConfirm.style.backgroundColor = "rgba(255,255,255,0.4)";
}

function checkName(event) {
	console.log(event.target.value);
}

passwd.addEventListener("input", checkPwd);
passwdConfirm.addEventListener("input", checkPwdMatch);
