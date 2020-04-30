function solution(priorities, location) {
  let answer = 0;
  const printQueue = Array(priorities.length);
  const idx = [...Array(priorities.length).keys()];
  let i = 0;
  while (priorities.length !== 0) {
    const doc = priorities[0];
    const index = idx[0];
    if (doc < Math.max(...priorities)) {
      priorities.push(doc);
      idx.push(index);
    } else {
      printQueue[idx[0]] = i;
      i++;
    }
    priorities.shift();
    idx.shift();
  }

  return printQueue[location] + 1;
}
