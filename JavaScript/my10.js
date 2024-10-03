const x = 10;

const color = x > 10 ? 'red' : 'blue';
console.log(color);

switch (color) {
    case 'red':
        console.log('Color is red');
        break;
    case 'blue':
        console.log('Color is blue');
        break;
    default:
        console.log('Color is not red or blue');
        break;
}