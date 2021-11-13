function compareTriplets(a, b) {
  let alice = 0;
  let bob = 0;
  if (a.length == b.length) {
    //constraints
    for (let i = 0; i < a.length; i++) {
      if (a[i] < 1 || b[i] < 1 || a[i] > 100 || b[i] > 100) {
        return;
      }
    }

    //compare
    for (let i = 0; i < a.length; i++) {
      if (a[i] > b[i]) alice++;
      else if (a[i] < b[i]) bob++;
    }
  }
  return [alice, bob];
}

//test
console.log(compareTriplets([1, 2, 3], [1, 2, 3]));
