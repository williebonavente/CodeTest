// Function to calculate the total cost of grocery shopping
function calculateTotalCost(items) {
  let totalCost = 0;

  // Iterate through each item in the items array
  for (const item of items) {
    const { price, quantity } = item;
    const itemCost = price * quantity;
    totalCost += itemCost;
  }

  return totalCost;
}

// Real-life scenario: Grocery shopping
const groceryItems = [
  { name: "Apples", price: 1.5, quantity: 3 },
  { name: "Bananas", price: 0.5, quantity: 6 },
  { name: "Milk", price: 2.0, quantity: 2 },
  { name: "Bread", price: 1.0, quantity: 1 },
];

// Calculate the total cost
const totalCost = calculateTotalCost(groceryItems);

// Output the result
console.log(`Total grocery cost: $${totalCost.toFixed(2)}`);
