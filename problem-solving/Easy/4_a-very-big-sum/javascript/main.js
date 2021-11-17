// URL : https://www.hackerrank.com/challenges/a-very-big-sum

function aVeryBigSum(ar) {
  // Write your code here
  return [...ar]
    .filter((p) => 0 <= p && p <= Math.pow(10, 10))
    .reduce((acc, total) => {
      return acc + total;
    }, 0);
}

//test
console.log(aVeryBigSum([1, 2, 3]));
