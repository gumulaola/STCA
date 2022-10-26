// js 6种基本数据类型 number string boolean null undefined symbol

let arr = [1, 2, 3];
let fn = function () {
  console.log(1);
};
let str = "hello";

console.log(typeof arr);
console.log(typeof fn);
console.log(typeof str);

console.log(Object.prototype.toString.call(arr));
console.log(Object.prototype.toString.call(fn));
