# Custom PowerShell object to simulate a hash table
$HashTable = New-Object PSObject -Property @{}

# Function to generate a hash code for a given key
function Get-HashCode([string] $key) {
    $hash = 0
    for ($i = 0; $i -lt $key.Length; $i++) {
        $char = [int]$key[$i]
        $hash = ($hash -shl 5) -bxor $hash + $char
    }
    return $hash
}

# Function to add a key-value pair to the hash table
function Put($key, $value) {
    $hashKey = Get-HashCode $key
    $HashTable.$hashKey = $value
}

# Function to get the value associated with a given key
function Get($key) {
    $hashKey = Get-HashCode $key
    return $HashTable.$hashKey
}

# Function to check if a key exists in the hash table
function ContainsKey($key) {
    $hashKey = Get-HashCode $key
    return $HashTable.PSObject.Properties.Name -contains $hashKey
}

# Function to remove a key-value pair from the hash table
function Remove($key) {
    $hashKey = Get-HashCode $key
    $HashTable.PSObject.Properties.Remove($hashKey)
}

# Function to get all keys in the hash table
function GetKeys() {
    return $HashTable.PSObject.Properties.Name
}

# Function to get all values in the hash table
function GetValues() {
    return $HashTable.PSObject.Properties.Value
}

# Function to get the size (number of key-value pairs) of the hash table
function Size() {
    return $HashTable.PSObject.Properties.Count
}

# Example usage:
# Adding key-value pairs to the hash table
Put "name" "John"
Put "age" 30
Put "city" "New York"

# Getting values based on keys
Write-Output "Name: $(Get 'name')"
Write-Output "Age: $(Get 'age')"
Write-Output "City: $(Get 'city')"

# Checking if a key exists
Write-Output "Contains 'name'? $(ContainsKey 'name')" # True
Write-Output "Contains 'gender'? $(ContainsKey 'gender')" # False

# Removing a key-value pair
Remove "age"

# Getting all keys and values
Write-Output "All Keys: $(GetKeys)"
Write-Output "All Values: $(GetValues)"

# Size of the hash table
Write-Output "Size: $(Size)"
