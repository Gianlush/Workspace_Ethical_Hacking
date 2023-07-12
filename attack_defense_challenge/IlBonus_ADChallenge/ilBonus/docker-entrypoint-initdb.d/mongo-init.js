const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
const flag_characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
const categories = ["Computer", "Tablet", "Smartphone", "Bicicletta", "Monopattino"];
const descriptions = [
    "Voucher per un potente computer da gaming.",
    "Voucher per un tablet adatto alla produttività.",
    "Voucher per uno smartphone con fotocamera di alta qualità.",
    "Voucher per una bicicletta da corsa.",
    "Voucher per un monopattino elettrico pieghevole."
  ];

function generateString(length) {
    let result = '';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}

function generateFlag() {
    let result = '';
    const charactersLength = flag_characters.length;
    for ( let i = 0; i < 31; i++ ) {
        result += flag_characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result.concat('=');
}

db.createCollection('users')
db.createCollection('vouchers')

for (let i = 0; i < 5; i++) {
    let username = generateString(15).concat(String.fromCharCode(65+i));
    let email = username.concat("@ilbonus.com");
    let password = generateString(16);
    let flag_user = generateFlag();

    let flag_voucher = generateFlag();
    const random_cat = Math.floor(Math.random() * categories.length);

    insertResult = db.vouchers.insertOne(
        {
            categoria: categories[random_cat],
            descrizione: descriptions[random_cat],
            negozio: '',
            indirizzo: '',
            infos: flag_voucher,
            utente: email,
        }
    );

    voucherid = insertResult.insertedId;

    db.users.insertOne(
        {
            email: email,
            password: password,
            nome: '',
            indirizzo: '',
            telefono: '',
            infos: flag_user,
            admin_user: true,
            vouchers: [voucherid]
        }
    )
}