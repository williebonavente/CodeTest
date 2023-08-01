function countOccurrences(arr, element) {
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === element) {
        count++;
      }
    }
    return count;
  }
  
  console.log(countOccurrences([1, 2, 2, 3, 2, 4, 2], 2)); // Output: 4
  