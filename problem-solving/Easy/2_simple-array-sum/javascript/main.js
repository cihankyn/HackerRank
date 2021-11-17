// URL : https://www.hackerrank.com/challenges/simple-array-sum/problem

function simpleArraySum(ar) {
  return [...ar]
    .filter((p) => p > 0 && p <= 1000)
    .reduce((acc, x) => {
      return acc + x;
    }, 0);
}

//test
console.log(simpleArraySum([3, 4, 5, 0, -1, 4]));
