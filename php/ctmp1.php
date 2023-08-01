<?php

function linear_search(int $x, $array)
{
    $i = 1;

    while ($i <= count($array) && $x != $array[$i]) {
        
        $i++;
    }

    if($i <= count($array))
    {
        $location = $i;
    }

    else
    {
        $location = 0;
    }

    return $location;
}

$array = [1, 2, 3, 4, 5];
$x = 3;

$location = linear_search($x,  $array);

echo "The location of $x is $location";


?>