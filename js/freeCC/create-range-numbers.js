function rangeOfNumbers(startNum, endNum) {

  // push.(i)
  if (endNum < startNum) {
    return [];
  } else {
    const counting = rangeOfNumbers(startNum, endNum - 1);
    counting.push(endNum);
    return counting;
  }
};

console.log(rangeOfNumbers(5, 15))