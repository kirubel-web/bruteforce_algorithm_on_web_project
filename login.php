<?php
  // Connect to database
  $conn = new mysqli('localhost', 'root', 'kirubel', 'website1',3306);

  // Check login credentials
  if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username']; 
    $password = $_POST['password']; 
    
    $sql = "SELECT * FROM users WHERE username = ? AND password = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $username, $password);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
       // Redirect to the dashboard
       echo "You are logged in!";
       header('Location: dashboard1.html');
       exit;

     
    } else {
      echo "Invalid username or password!"; 
    }
  }
  
?>


