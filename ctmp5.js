const mergeSort = (arr) => {
  if (arr.length <= 1) {
    return arr;
  }
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  return mergeSort(mergeSort(left), mergeSort(right));
};

console.log(mergeSort([3, 5, 1, 2, 4]));