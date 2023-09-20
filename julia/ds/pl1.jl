# Creating a 1D array of numbers
data_array = [1, 2, 3, 4, 5]

# Creating a 2D matrix
data_matrix = [1 2 3; 4 5 6; 7 8 9]

# Creating a dictionary (associative array)
data_dict = Dict("name" => "John", "age" => 30, "city" => "New York")

# Creating a vector of random numbers
using Random
random_numbers = rand(5)  # Creates an array of 5 random numbers between 0 and 1

# Creating a DataFrame (requires the DataFrames package)
using DataFrames
data_df = DataFrame(Column1 = [1, 2, 3, 4, 5], Column2 = ["A", "B", "C", "D", "E"])
