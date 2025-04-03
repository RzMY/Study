const numbers = new Array(1, 2, 3, 4, 5);

console.log(numbers);

const fruits = ["apples", "oranges", "pears", 10, true];
console.log(fruits);
console.log(fruits[1]);
fruits[3] = "grapes";
fruits.push("mango"); // 添加到最后
fruits.unshift("strawberries"); // 添加到最前面
fruits.pop(); // 删除最后一个
console.log(Array.isArray(fruits));
console.log(fruits.indexOf("oranges"))