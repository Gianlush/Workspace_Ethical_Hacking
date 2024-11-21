const path = require('path');

const x = '../../flag.txt'

const filepath = path.join("team", x + ".png");
const sliced = filepath.slice(0, 100)
console.log('path:          team/'+x)
console.log('path joined:   '+filepath);
console.log('path sliced:   '+sliced);