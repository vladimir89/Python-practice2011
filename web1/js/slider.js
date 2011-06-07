 $(document).ready(function () {
 
  if ($('#button1').click(function () {
      if($('#the_menu2').css('display')=='block'){
          	$('#the_menu2').hide('fast');
	}
	  
      
          $('#the_menu1').slideToggle('medium');
          
       
                 
       }));
	
	   
  $('#layer_open_button1').mouseleave(function () { 
      $('#the_menu1').hide('fast');
      });
      
  $('#layer_open_button2').mouseleave(function () { 
      $('#the_menu2').hide('fast');
      });  
  
  
     
       
  if ($('#button2').click(function () {
      if($('#the_menu1').css('display')=='block'){
          {
			$('#the_menu1').hide('fast');
			
			
		  }
	  
      }
	 
    $('#the_menu2').slideToggle('medium');
  }));
  
  
  
   
       
       
       
       
       });
        
 
  
  
 