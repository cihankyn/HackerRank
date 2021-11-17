// URL : https://www.hackerrank.com/challenges/mini-max-sum/problem

function miniMaxSum(arr) {
  let mini = 0,
    max = 0;
  mini = [...arr]
    .sort()
    .splice(0, 4)
    .reduce((acc, value) => acc + value, 0);
  max = [...arr]
    .sort()
    .reverse()
    .splice(0, 4)
    .reduce((acc, value) => acc + value, 0);
  console.log(mini, max);
}

// test
miniMaxSum([1, 2, 3, 4, 5]);
