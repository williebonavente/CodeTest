// Function to perform linear search in the dictionary
function dictionarySearch(dictionary, targetWord) {
  for (let i = 0; i < dictionary.length; i++) {
    if (dictionary[i] === targetWord) {
      return i; // Return the index where the word is found in the dictionary
    }
  }
  return -1; // Return -1 if the word is not found in the dictionary
}

// Example dictionary (an ordered list of words)
const dictionary = [
  "apple",
  "banana",
  "cherry",
  "grape",
  "orange",
  "peach",
  "pear",
  "pineapple",
  "strawberry",
];

// Word to search for in the dictionary
const targetWord = "orange";

// Perform linear search in the dictionary
const index = dictionarySearch(dictionary, targetWord);

// Output the result
if (index !== -1) {
  console.log(
    `The word "${targetWord}" is found at index ${index} in the dictionary.`
  );
} else {
  console.log(`The word "${targetWord}" is not found in the dictionary.`);
}
