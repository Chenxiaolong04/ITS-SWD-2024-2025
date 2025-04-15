<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Carta sasso forbice</h1>
    <a href="?simbolo=pietra">Pietra</a>
    <a href="?simbolo=forbice">Forbice</a>
    <a href="?simbolo=carta">Carta</a>
<?php
    $sceltaUmano="";
    if(isset($_GET["simbolo"])){
        $sceltaUmano=$_GET["simbolo"];
    }
?>
    <h2>La scelta di umano è: <?=$sceltaUmano?></h2>
<?php
    $sceltaMacchina="";
    $scelte=["pietra","forbice","carta"];
    $casuale=array_rand($scelte);
    $sceltaMacchina=$scelte[$casuale]
?>
    <h2>La scelta della macchina è: <?=$sceltaMacchina?></h2>
<?php
    function valuta($sceltaUmano,$sceltaMacchina){
        if($sceltaUmano==$sceltaMacchina){
            return "Pareggio";
        }else{
            switch($sceltaUmano){
                case "pietra":
                    if($sceltaMacchina=="forbice")
                        return "Vince umano";
                    else 
                        return "Vince macchina";
                case "forbice":
                    if($sceltaMacchina=="carta")
                        return "Vince umano";
                    else 
                        return "Vince macchina";
                case "carta":
                    if($sceltaMacchina=="pietra")
                        return "Vince umano";
                    else 
                        return "Vince macchina";
            }
                
        }
            
    }
    $result=valuta($sceltaUmano,$sceltaMacchina)
?>
    <h2>Il risultato è: <?=$result?></h2>

</body>
</html>