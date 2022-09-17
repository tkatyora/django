 let error = document.getElementsByClassName('error'),
     form = document.forms['form-id'],
     username = document.forms["form"]['username'],
     password = document.forms["form"]['password'],
     show = document.querySelector('#show'),
     time = document.querySelector('#time'),
     input = document.getElementsByClassName('input')
 ;
 
console.log(input)
for(error of error){
  error.style.display = 'none' ;
}
form.addEventListener('submit',function(e){
  e.preventDefault();
  
  validation();

})

// validation function
  function validation() {
   if(password.value == 2000 && username.value == 'admin'){
    window.location = "B:\\TNC-COMPANY-PROJECTS\\company-website\\BOOTSRAP-WEBSITE\\html.pages\\admin-dashboard.html";
   }
   else if(password.value == 2000 && username.value != 'admin')
   {
    usernameWrong();
   
   }
   else if(password.value != 2000 && username.value == 'admin')
   {
    error[1].style.display ='block';
    passwordWrong();
   }
   else{
    
    error[0].style.display ='block';
    bothWrong();
   }
   }
show.addEventListener('click', function(){
  if(input[1].type === 'password'){
    input[1].type = 'text';
    show.textContent = 'Hide'
    
  }else{
    input[1].type = 'password';
    show.textContent = 'Show'
    
  }
  
}

)



   // functions

   function usernameWrong(){
    error[2].style.display ='block';
    input[0].style.border = '2px red solid';
    input[0].style.backgroundColor = 'red'
   }
   function passwordWrong(){
    error[1].style.display ='block';
    input[1].style.border = '2px red solid';
    
   }
   function bothWrong(){
    error[2].style.display ='block';
    input[0].style.border = '2px red solid';
    input[1].style.border = '2px red solid';
    
   }
  
