function GCD(a, b) {
  return b ? GCD(b, a % b) : a;
}
function solution(w, h) {
  const gcd = GCD(w, h);
  const [w_, h_] = [w / gcd, h / gcd];
  if (w === h) return w * h - w;
  const answer = (w_ + h_ - 1) * gcd;
  return w * h - answer;
}
