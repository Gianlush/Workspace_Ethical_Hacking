<?php
/*
Plugin Name: Dummy
*/

class Evil {
  public function __wakeup() : void {
    die("Arbitrary deserialization");
  }
}

function display_hello_world() {
    echo "Hello World";
}

add_action('wp_footer', 'display_hello_world');