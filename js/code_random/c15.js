function containsOnlyDigits(str) {
    return /^\d+$/.test(str);
  }
  
  console.log(containsOnlyDigits('123')); // Output: true
  