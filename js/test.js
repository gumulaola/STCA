function Student(name, age) {
  this.name = name;
  this.age = age;
}

Student.prototype.say = function () {
  console.log(this.name);
  console.log(this.age);
};

let ins = new Student("ming", 18);
// ins.say();

let proxy = new Proxy(ins, {
  get(target, p) {
    if (p in target) {
      console.log("name get.");
      return target[p];
    } else {
      throw new Error("p is not in target.");
    }
  },
});

console.log(proxy.name);
