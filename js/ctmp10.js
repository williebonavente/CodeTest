// Function to evaluate the analogies
function evaluateAnalogies(p, q, r) {
    const analogyA = r && !p;
    const analogyB = (!r || p) === q;
    const analogyC = (!r) === (!q);
    const analogyD = (!p && r) === q;
  
    return { analogyA, analogyB, analogyC, analogyD };
  }
  
  // Example input values for p, q, and r
  const p = true;  // User enters a valid password
  const q = true;  // Access is granted
  const r = true;  // User has paid the subscription fee
  
  // Evaluate the analogies
  const result = evaluateAnalogies(p, q, r);
  
  console.log("Analogies Evaluation:");
  console.log("a) The user has paid the subscription fee, but does not enter a valid password:", result.analogyA);
  console.log("b) Access is granted whenever the user has paid the subscription fee and enters a valid password:", result.analogyB);
  console.log("c) Access is denied if the user has not paid the subscription fee:", result.analogyC);
  console.log("d) If the user has not entered a valid password but has paid the subscription fee, then access is granted:", result.analogyD);
  