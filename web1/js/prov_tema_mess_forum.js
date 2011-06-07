function prov_mes_forum(){
	obj_form_mes_tema = document.forms.Prov_mess;
	obj_mess = obj_form_mes_tema.coment;
	if (obj_mess.value == ""){
		alert("Введите сообщение!");
		return;
	}
	obj_form_mes_tema.submit();
}