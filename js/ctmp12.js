// HashTable class
class HashTable {
  constructor() {
    this.table = {};
  }

  // Function to generate a hash code for a given key
  hashCode(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      const char = key.charCodeAt(i);
      hash = (hash << 5) - hash + char;
    }
    return hash;
  }

  // Function to add a key-value pair to the hash table
  put(key, value) {
    const hashKey = this.hashCode(key);
    this.table[hashKey] = value;
  }

  // Function to get the value associated with a given key
  get(key) {
    const hashKey = this.hashCode(key);
    return this.table[hashKey];
  }

  // Function to check if a key exists in the hash table
  containsKey(key) {
    const hashKey = this.hashCode(key);
    return this.table.hasOwnProperty(hashKey);
  }

  // Function to remove a key-value pair from the hash table
  remove(key) {
    const hashKey = this.hashCode(key);
    delete this.table[hashKey];
  }

  // Function to get all keys in the hash table
  getKeys() {
    return Object.keys(this.table);
  }

  // Function to get all values in the hash table
  getValues() {
    return Object.values(this.table);
  }

  // Function to get the size (number of key-value pairs) of the hash table
  size() {
    return Object.keys(this.table).length;
  }
}

// Example usage:
const myHashTable = new HashTable();

// Adding key-value pairs to the hash table
myHashTable.put("name", "John");
myHashTable.put("age", 30);
myHashTable.put("city", "New York");

// Getting values based on keys
console.log("Name:", myHashTable.get("name"));
console.log("Age:", myHashTable.get("age"));
console.log("City:", myHashTable.get("city"));

// Checking if a key exists
console.log("Contains 'name'?", myHashTable.containsKey("name")); // true
console.log("Contains 'gender'?", myHashTable.containsKey("gender")); // false

// Removing a key-value pair
myHashTable.remove("age");

// Getting all keys and values
console.log("All Keys:", myHashTable.getKeys());
console.log("All Values:", myHashTable.getValues());

// Size of the hash table
console.log("Size:", myHashTable.size());
