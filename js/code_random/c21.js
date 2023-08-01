function generateRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  console.log(generateRandomNumber(1, 10)); // Output: Random number between 1 and 10
  