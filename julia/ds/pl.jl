using Plots

# Create a scatter plot
scatter(data.column1, data.column2, label="Scatter Plot")

# Create a histogram
histogram(data.column3, bins=20, label="Histogram")

# Create a box plot
boxplot(data.column4, data.column5, label="Box Plot")
