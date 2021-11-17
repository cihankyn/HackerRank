// URL : https://www.hackerrank.com/challenges/staircase/problem

function staircase(n) {
  if (0 < n && n <= 100) {
    for (let i = n; i > 0; i--) {
      let string = "";
      for (let j = 1; j < n + 1; j++) {
        if (j < i) string += " ";
        else string += "#";
      }
      console.log(string);
    }
  }
}

// test
staircase(6);
