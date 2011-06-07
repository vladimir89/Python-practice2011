  $(document).ready(function () {
 
  if ($('#button3').click(function () {
      if($('#the_menu4').css('display')=='block'){
          	$('#the_menu4').hide('fast');
	}
	       
          $('#the_menu3').slideToggle('medium');
          
       
                 
       }));
	
	   
  $('#layer_open_button3').mouseleave(function () { 
      $('#the_menu3').hide('fast');
      });
      
  $('#layer_open_button4').mouseleave(function () { 
      $('#the_menu4').hide('fast');
      });     
  
     
       
  if ($('#button4').click(function () {
      if($('#the_menu3').css('display')=='block'){
          $('#the_menu3').hide('fast');
		  
      }
	 
    $('#the_menu4').slideToggle('medium');
  }));
  
  
  
   
       
       
       
       
       });
        
 
  
  
 
  
  
 