<h1>Slide Show</h1>
<?php
function inc(){
    global $counter;
    return $counter++;
}
function dec(){
    global $counter;
    return $counter--;
}
inc();
$counter = (isset($_GET['contatore'])) ? $_GET['contatore'] : 0;

echo "<h2>" .$counter."</h2>";
?>
<img src="./img/img<?=$counter?>.jpg" alt="">
<a href="?contatore=<?=$counter+1?>">Avanti</a>
<a href="?contatore=<?=$counter-1?>">Indietro</a>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut dolor nisi fuga harum error ullam eum nemo dolores eos maxime. Consequuntur, eos. Aut quaerat deleniti asperiores vitae, nemo tempora culpa!</p>
