const x = 10;
const y = "10";

// == 表示相等，不考虑数据类型 === 表示严格相等，包括数据类型

if (y == 10) {
    console.log('y is 10');
}
if (x === 10) {
    console.log('x is 10');
}
if (x == y) {
    console.log('x is equal to y');
}
if (x === y) {
    console.log('x is strictly equal to y');
} else {
    console.log('x is not strictly equal to y');
}

if (x === 10) {
    pass
} else if (x === 20) {
    pass
} else {
    pass
}

const z = 10;
if (x > 5 || y > 10) {
    console.log('x is more than 5 or y is more than 10');
}
if (x > 5 && y > 10) {
    console.log('x is more than 5 and y is more than 10');
}