//normal function
//remember exemple 1
function EvenOrOdd(a) {
  if (a % 2 == 0) {
    return `even`;
  } else {
    return ` odd`;
  }
}
console.log(EvenOrOdd(95));

//as an arrow function

const EvenOrOdd2 = (a) => a % 2 === 0 ? `Even` : `Odd`;

console.log(EvenOrOdd2(5))
