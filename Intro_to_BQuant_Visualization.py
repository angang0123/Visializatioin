'''
Introduction to BQuant Visualization 
This notebook provides an overview of the different visualization libraries and features available in the BQuant platform.
BQuant includes two Bloomberg visualization libraries that allow you to quickly create simple plots and leverage highly 
customizable visualizations in interactive applications.

Visualization Libraries
Examples
      bqviz Line Plot Example
      bqplot Line Plot Example
Related Resources


Visualization Libraries 
bqviz
bqviz is a Bloomberg wrapper for the bqplot library that helps you easily create many common plots, often with just a single line of code.

bqplot
bqplot is a complete visualization library developed and open sourced by Bloomberg. bqplot includes two APIs:

The context-based API is similar to Matplotlib's pyplot library, which provides sensible defaults for most parameters.
The object model is based on the Grammar of Graphics principles and allows you to build sophisticated visualizations out 
of component objects (figure, marks, axes and scales).
'''


# Import the BQL library
import bql
# Import the bqviz and bqplot libraries
import bqviz as bqv
from bqplot import pyplot as plt

# Instantiate an object to interface with the BQL service
bq = bql.Service()

# Define a request for the daily last price of Apple and IBM over the last year
request = "get(PX_LAST(dates=range(-1Y,-1D)) as #LAST_PRICE) for (['AAPL US Equity','IBM US Equity'])"

# Execute the request to return a response object
response = bq.execute(request)

# Convert the response object to a DataFrame 
df = response[0].df()
# Drop N/A values and reset the dataframe index
df = df.dropna().reset_index()
# Pivot the DataFrame on the columns to plot
df = df.pivot("DATE","ID","#LAST_PRICE")

# Check the DataFrame columns
df.head()

#************bqviz Line Plot Example************
# Pass the example DataFrame to the bqviz LinePlot object and apply Bloomberg styles
bqv_plot = bqv.LinePlot(df).set_style()

# Display the plot
bqv_plot.show()

#*************bqplot Line Plot Example************
# Define series objects for the price lines
aapl_price = df['AAPL US Equity']
ibm_price = df['IBM US Equity']
# Define a series object for the date index
plot_dates = df.index

# Create the figure canvas
plt.figure()
# Define the plot using the price date and price series objects
aapl_line = plt.plot(plot_dates, [aapl_price, ibm_price])

# Display the plot
plt.show()
