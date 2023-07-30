// Function to check if ac ≡ bc (mod mc)
function checkModularEquivalence(a, b, c, m) {
    const leftHandSide = (a * c) % (m * c);
    const rightHandSide = (b * c) % (m * c);
  
    return leftHandSide === rightHandSide;
  }
  
  // Given values
  const a = 7;
  const b = 5;
  const c = 3;
  const m = 4;
  
  // Check if ac ≡ bc (mod mc)
  const result = checkModularEquivalence(a, b, c, m);
  
  console.log(result ? "ac ≡ bc (mod mc)" : "ac is not equivalent to bc (mod mc)");
  