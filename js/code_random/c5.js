function fibonacciSequence(num) {
    const sequence = [0, 1];
    for (let i = 2; i <= num; i++) {
      const nextNum = sequence[i - 1] + sequence[i - 2];
      sequence.push(nextNum);
    }
    return sequence;
  }
  
  console.log(fibonacciSequence(10)); // Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  