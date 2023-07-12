<?php
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/includes/logging.inc.php';
require_once __DIR__ . '/includes/utils.inc.php';
require_once __DIR__ . '/includes/voucher_utils.inc.php';

////////////////////////////////////////////////////////////////////////////////
// GLOBALS/CONFIG

// start session on each page
session_start();
$mongoclient = new MongoDB\Client('mongodb://mongo-app');
$users = $mongoclient->ilbonus->users;
$klein = new \Klein\Klein();

////////////////////////////////////////////////////////////////////////////////
// APP

$klein->respond(array('GET'), '/', function ($req, $res, $service) {
    header("Location: /flagIds");
});

$klein->respond(array('GET'), '/flagIds', function ($req, $res, $service) {
    global $users;
    try {
        header('Content-Type: application/json; charset=utf-8');
        $json = $users->find(array('admin_user' => TRUE), array('projection' => array('_id' => 0, 'email' => 1)));
        $emails = array();
        
        foreach($json as $el)
            array_push($emails, $el['email']);
        
        $nopteam = array('localhost' => $emails);
        $result = json_encode(array('ilBonus' => $nopteam));
        echo $result;
    } catch (Exception $e) {
        header('Content-Type: text/plain; charset=utf-8');
        echo "Database in costruzione...\nAttendi qualche secondo e ricarica la pagina!";
    }
});

$klein->onHttpError(function ($code, $router) {
    echo 'Error '.$code;
});

$klein->dispatch();
