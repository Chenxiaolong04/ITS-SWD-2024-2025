<?php
$saluto = "hello world";
$a = 6;

if ($a == 5) {
    $saluto = "Hello PHP";
} elseif ($a < 5) {
    $saluto = "Abbasso python";
} else {
    $saluto = "Viva java";
}
for($i=0;$i<10;$i++){
    echo "<h1>" . $saluto . "</h1>\n";
}
?>
