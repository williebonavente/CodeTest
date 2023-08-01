// Function to simulate the combinatorial circuit
function combinatorialCircuit(p, q, r) {
    // Inverters (NOT gates)
    const notR = !r;
    const notQ = !q;
  
    // AND gates
    const pAndNotR = p && notR;
    const notQAndR = notQ && r;
  
    // OR gate
    const output = pAndNotR || notQAndR;
  
    return output;
  }
  
  // Example input values for p, q, and r
  const p = true;
  const q = false;
  const r = true;
  
  // Evaluate the combinatorial circuit
  const result = combinatorialCircuit(p, q, r);
  
  console.log(`Output: ${result}`);
  