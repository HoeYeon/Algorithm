function solution(arrangement) {
  let answer = 0;
  const stack = [];
  for (let i = 0; i < arrangement.length - 1; i++) {
    if (arrangement[i] === "(") {
      if (arrangement[i + 1] === ")") {
        answer += stack.length;
        i++;
      } else {
        stack.push("(");
        answer++;
      }
    } else {
      stack.pop();
    }
  }
  return answer;
}
