// URL : https://www.hackerrank.com/challenges/plus-minus/problem

// This is works on here but not working on hackerrank.

function plusMinus(input) {
  var lines = input.toString().split("\n"),
    size = parseInt(lines.shift()),
    pos = 0,
    neg = 0,
    zero = 0;
  lines[0].split(" ").map(function (p) {
    val = parseInt(p);
    if (val < 0) neg++;
    else if (val == 0) zero++;
    else pos++;
  });
  console.log((pos / size).toFixed(6));
  console.log((neg / size).toFixed(6));
  console.log((zero / size).toFixed(6));
}
//test
inp = `10
0 100 35 0 94 40 42 87 59 0`;
plusMinus(inp);
