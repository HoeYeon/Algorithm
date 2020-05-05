function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length != b.length) return false;
  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
function solution(name) {
  let answer = 0;
  let idx = 0;
  const result = name.split("");
  const cmp = Array(name.length).fill("A");
  let count = 0;

  while (true) {
    let [left, right] = [idx, idx];
    if (arraysEqual(cmp, result)) break;
    count += Math.min(
      Math.abs(result[idx].charCodeAt() - "A".charCodeAt()),
      Math.abs(result[idx].charCodeAt() - "Z".charCodeAt()) + 1
    );
    cmp[idx] = result[idx];
    for (let i = 0; i < result.length; i++) {
      if (
        cmp[(right + i) % result.length] !== result[(right + i) % result.length]
      ) {
        idx = (right + i) % result.length;
        count += i;
        break;
      } else if (
        cmp[(idx + result.length - i) % result.length] !==
        result[(idx + result.length - i) % result.length]
      ) {
        idx = (idx + result.length - i) % result.length;
        count += i;
        break;
      }
    }
  }
  return count;
}
