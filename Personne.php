<?php


class Personne
{
private string $nom;
private string $prenom;
private string $naissance;

function __construct(string $nom, string $prenom,$naissance){
    $this->nom=$nom;
    $this->prenom=$prenom;
    $this->naissance=$naissance;
}

function afficher(){
    echo "Je suis $prenom $nom et je suis né le $naissance.";
}
}