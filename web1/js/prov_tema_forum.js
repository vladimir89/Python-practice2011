function prov(){
	obj_form_forum_tema = document.forms.Prov;
	obj_name_tema = obj_form_forum_tema.tema_cont;
	if (obj_name_tema.value == ""){
		alert("Введите название темы!");
		return;
	}
	obj_form_forum_tema.submit();
}