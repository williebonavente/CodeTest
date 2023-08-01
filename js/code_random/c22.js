function removeDuplicates(list) {
    return [...new Set(list)];
  }
  
  console.log(removeDuplicates([1, 2, 2, 3, 3, 4, 5, 5])); // Output: [1, 2, 3, 4, 5]
  