let answer = 0;
const dfs = (op, numbers, target) => {
  if (op.length == numbers.length) {
    let count = 0;
    for (let i in numbers) {
      count += op[i] === "+" ? numbers[i] : -numbers[i];
    }
    if (count === target) answer++;
    return;
  }
  dfs([...op, "+"], numbers, target);
  dfs([...op, "-"], numbers, target);
};
function solution(numbers, target) {
  dfs([], numbers, target);
  return answer;
}
