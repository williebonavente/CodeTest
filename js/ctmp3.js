// Function to find the value of c ≡ a (mod m)
function findC(mod, a, constant) {
  let c = a % mod;
  while (c < 0) {
    c += mod;
  }
  c *= constant;
  c %= mod;
  return c;
}

// Given values
const a = 11;
const b = 3;
const mod = 19;

// a) c ≡ 13a (mod 19)
const c_a = findC(mod, a, 13);
console.log(`a) c ≡ ${c_a} (mod 19)`);

// b) c ≡ 8b (mod 19)
const c_b = findC(mod, b, 8);
console.log(`b) c ≡ ${c_b} (mod 19)`);

// c) c ≡ a - b (mod 19)
const c_c = findC(mod, a - b, 1);
console.log(`c) c ≡ ${c_c} (mod 19)`);

// d) c ≡ 7a + 3b (mod 19)
const c_d = findC(mod, 7 * a + 3 * b, 1);
console.log(`d) c ≡ ${c_d} (mod 19)`);

// e) c ≡ 2a^2 + 3b^2 (mod 19)
const c_e = findC(mod, 2 * a * a + 3 * b * b, 1);
console.log(`e) c ≡ ${c_e} (mod 19)`);

// f) c ≡ a^3 + 4b^3 (mod 19)
const c_f = findC(mod, Math.pow(a, 3) + 4 * Math.pow(b, 3), 1);
console.log(`f) c ≡ ${c_f} (mod 19)`);
