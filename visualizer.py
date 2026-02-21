import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('wall_scan_data.csv')

# Create a scatter plot (replace x and y with your CSV column names)
fig = px.scatter(df, x='column_x', y='column_y', title='My CSV Plot')

# Save the plot as an HTML file
fig.write_html('plot.html')
print("Plot saved as plot.html")
