<?php       
inclue('form.html');
    $username = $_POST['user'];  
    $password = $_POST['pass'];  

     if(username='shankar' and password='1234'){
echo"<h1><center>Login successful</center></h1>";
}
else{
  echo "<h1> Login failed. Invalid username or password.</h1>";  
        }     
?>  