<?php
require_once('Personne.php');

$perso=new Personne('Jacques','Jean','12 juin 2013');
$perso->afficher();


echo 'test</br>et oui';

//function pourcentageAvis(string $typeAvis,int $nbAvisFav,int $nbAvisDefav){
//    $nbtotal=$nbAvisFav+$nbAvisDefav;
//    if($nbtotal==0){
//        throw new \mysql_xdevapi\Exception("Division par 0!");
//    }
//    if(typeAvis=='favorable'){
//        $nb=$nbAvisFav/$nbtotal*100;
//        echo "le pourcentage d'avis favorable est de $nb%.";
//    }
//    if(typeAvis=='defavorable'){
//        $nb=$nbAvisDefav/$nbtotal*100;
//        echo "le pourcentage d'avis defavorable est de $nb%.";
//    }
//}
//try {
//    pourcentageAvis('favorable', 20, 20);
//}
//catch (Exception $e){
//    echo $e->getMessage();
//}


