function solution(board, moves) {
  const stack = [];
  let count = 0;
  const tmp = [...Array(board.length)].map((e) => Array());
  for (let i = board.length - 1; i >= 0; i--) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] !== 0) tmp[j].push(board[i][j]);
    }
  }
  for (let i in moves) {
    const item = tmp[moves[i] - 1].pop();
    if (item) {
      if (stack[stack.length - 1] == item) {
        stack.pop();
        count += 2;
      } else stack.push(item);
    }
  }
  return count;
}
