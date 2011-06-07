function insrtSmal(obj){
	obj_form_mes_tema = document.forms.Prov_mess;
	obj_mess = obj_form_mes_tema.coment;
	if (obj_mess.value == ""){
		alert("Введите сообщение!");
		return;
	}else{
		obj.focus();
		if (typeof(obj.selectionStart)=="number"){
			var start = obj.selectionStart;
			var end = obj.selectionEnd;
			obj.value = obj.value.substr(0, start) + obj.value.substring(start,end).small() + obj.value.substr(end);
		}
		else{
			var str = document.selection.createRange().text;
			if (str!=''){ 
				var newStr =str.small();
				document.selection.createRange().text=newStr;
			}
		}
	}
return true;
}