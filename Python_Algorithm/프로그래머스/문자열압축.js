function solution(s) {
  const max_len = Math.floor(s.length / 2);
  let answer = s.length;

  for (let check = 1; check <= max_len + 1; check++) {
    let count = 1;
    let result = "";
    let i = 0;
    for (i; i < s.length - check; i += check) {
      let dup = true;
      const cmp = i + check;
      for (let j = 0; j < check; j++) {
        if (s[i + j] !== s[cmp + j]) {
          dup = false;
          if (count == 1) result += s.slice(i, i + check);
          else result += count + s.slice(i, i + check);
          count = 1;
          break;
        }
      }
      if (dup) count++;
    }

    if (count == 1) result += s.slice(i, s.length);
    else result += count + s.slice(i, s.length);
    // console.log(result,i,count,result.length)
    answer = Math.min(answer, result.length);
  }
  return answer;
}
