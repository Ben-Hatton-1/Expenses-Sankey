import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.colors
from categories import get_categories

# Load the data
df = pd.read_excel("/path/to/your/excel/file.xlsx")

# Filter data for the year 2022
df_2022 = df[df['Date'].dt.year == 2022]

# Apply the get_categories function to get the main categories
df_2022['Main Category'] = df_2022['Category'].apply(lambda x: get_categories(x)[0])

# Group by main category and calculate total amount spent
category_totals = df_2022.groupby('Main Category')['Amount'].sum().reset_index()

# Create a list of labels and values for the Sankey diagram
labels = category_totals['Main Category'].tolist()
values = category_totals['Amount'].tolist()

# Create a list of colors for the categories
colors = plt.get_cmap('tab20').colors
colors = [matplotlib.colors.rgb2hex(color) for color in colors]
colors = colors * (len(labels) // len(colors) + 1)  # repeat colors if not enough

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = colors[:len(labels)]  # use as many colors as needed
    ),
    link = dict(
      source = [0] * len(labels), # all flows originate from the first node (total amount)
      target = list(range(1, len(labels) + 1)), # each flow goes to a different category
      value = values, # the value of each flow is the total amount spent in the category
      color = colors[:len(labels)]  # use as many colors as needed
  )
)])

fig.update_layout(title_text="Mint Transactions Sankey Diagram for 2022", font_size=10)
fig.write_html("mint_transactions_sankey_2022.html")
