Mint Transactions Sankey Diagram
This project generates a Sankey diagram of Mint transactions, grouped by categories, for the year prior (2022 in this case). This tool enables more customizable options.

Getting Started
Prerequisites packages:

pandas
plotly
matplotlib
openpyxl

pip install pandas plotly matplotlib openpyxl
Usage
Make sure your transaction data is in an Excel file with the following columns:

Date
Amount
Category
Update the file path in the Python script to point to your Excel file:

df = pd.read_excel("/path/to/your/excel/file.xlsx")
Run the Python script:
css

python main.py
The script will generate an HTML file named "mint_transactions_sankey_2022.html" in the same directory. Open this file in a web browser to view the Sankey diagram.
Customizing the Diagram
You can customize the Sankey diagram by modifying the following parts of the script:

Change the year by updating this line:
python
Copy code
df_2022 = df[df['Date'].dt.year == 2022]
Change the color palette by updating this line:
python
Copy code
colors = plt.get_cmap('tab20').colors
