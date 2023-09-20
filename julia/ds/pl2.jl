using Plots

# Predefined data (replace with your actual data)
column1 = rand(1:100, 50)   # Example data for column1
column2 = rand(1:100, 50)   # Example data for column2
column3 = rand(1:100, 100)  # Example data for column3
column4 = rand(1:100, 100)  # Example data for column4
column5 = rand(1:100, 100)  # Example data for column5

# Create a scatter plot
scatter(column1, column2, label="Scatter Plot")

# Create a histogram
histogram(column3, bins=20, label="Histogram")

# Create a box plot
boxplot(column4, column5, label="Box Plot")

# Display the plot
plot!()  # This command is used to display the combined plot
