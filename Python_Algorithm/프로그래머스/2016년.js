function solution(a, b) {
  const info = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
  };
  const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  console.log(info);
  const idx = 5;
  let start = 1;
  let days = 0;
  while (a !== start) {
    days += info[start];
    start++;
  }
  days += b;
  days %= 7;
  const ans = day[(idx + days - 1) % 7];
  return ans;
}
