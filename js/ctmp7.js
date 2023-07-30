function evaluateLogicalExpression(p1, p2) {
    const part1 = (!p1 && !!p2 && !p2);
    const part2 = (!!p1 && !p2 && !p2);
    const part3 = (!!p1 && !!p2 && p2);
    return part1 || part2 || part3;
  }
  
  // Example values for p1 and p2
  const p1 = true;
  const p2 = false;
  
  // Evaluate the logical expression
  const result = evaluateLogicalExpression(p1, p2);
  
  console.log(`Result: ${result}`);
  