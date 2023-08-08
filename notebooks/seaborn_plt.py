# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data= tips,
    x = "total bill", y = "tip", col = "time",
    hue =  "smoker", style = "smoker", size = "size"
)