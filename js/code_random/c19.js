function findSecondLargestElement(arr) {
    let largest = arr[0];
    let secondLargest = arr[0];
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] > largest) {
        secondLargest = largest;
        largest = arr[i];
      } else if (arr[i] > secondLargest && arr[i] < largest) {
        secondLargest = arr[i];
      }
    }
    return secondLargest;
  }
  
  console.log(findSecondLargestElement([5, 2, 8, 1, 9])); // Output: 8
  