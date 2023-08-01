function median(nums) {
  // Sort the array in ascending order
  const sortedList = nums.slice().sort((a, b) => a - b);
  const length = sortedList.length;
  const midIndex = Math.floor(length / 2);

  // Check if the array has odd or even length
  if (length % 2 === 0) {
    // For even length, take the average of the middle two elements
    return (sortedList[midIndex] + sortedList[midIndex - 1]) / 2;
  } else {
    // For odd length, return the middle element
    return sortedList[midIndex];
  }
}

function main() {
  // Check if the user provided arguments
  if (process.argv.length <= 2) {
    console.log("Usage: node median.js <num1> <num2> <num3> ...");
    return;
  }

  // Parse command-line arguments to integers
  const nums = process.argv.slice(2).map(Number);

  // Check if all arguments are valid numbers
  if (nums.some(isNaN)) {
    console.log("Invalid input. Please provide only numeric values.");
    return;
  }

  const result = median(nums);
  console.log(`Median: ${result}`);
}

if (require.main === module) {
  main();
}
