#Before running any of the examples in this notebook, you need to import the bqviz library and sample data.
import bqviz as bqv
from bqviz.sample_data import *


#****************Base Plot Objects*******************

# For reference, display the first few rows of our dataframe
multidf.head()

# Pass the dataframe to LinePlot and apply Bloomberg styles
ex1 = bqv.LinePlot(multidf).set_style()

# Display the plot
ex1.show()



#********************BarPlot Object********************

# For reference, display the first few rows of our dataframe
multidf2.head()

# Pass the dataframe to BarPlot
# Specify the legend outside of plot
# Slice the dataframe to include bars for the first three data rows
# Apply Bloomberg styles
ex2 = bqv.BarPlot(multidf2[:3], 
                  legend='outside', 
                  convert_dates=True, 
                  padding=.3).set_style()

# Display the plot
ex2.show()


#Create a Stacked Bar Chart

# Use the bar_type parameter to stack the bars
ex3 = bqv.BarPlot(multidf2[:3], 
            bar_type='stacked', 
            legend='outside', 
            convert_dates=True, 
            padding=.3).set_style()

# Display the plot
ex3.show()



******************#KDEPlot Object*********************

# Pass the dataframe to KDEPlot and apply Bloomberg styles
ex4 = bqv.KDEPlot(multidf).set_style()

# Show the plot
ex4.show()

# Use the bandwidth parameter to modify the KDE bandwidth
ex5 = bqv.KDEPlot(multidf, bandwidth=0.009).set_style()

# Display the plot
ex5.show()


#********************HistPlot Object****************

# Pass the dataframe to HistPlot and apply Bloomberg styles
ex6 = bqv.HistPlot(df)

ex6.show()
# Display the plot


# Use the bins parameter to increase the number of bins to 25
ex7 = bqv.HistPlot(df, bins=25)

# Display the plot
ex7.show()



#*********************Specialized Plot Objects*********************

#********************DistributionPlot**************

# Pass the dataframe to DistributionPlot and apply Bloomberg styles
ex8 = bqv.DistributionPlot(df).set_style()

# Display the plot
ex8.show()



#****************OverUnderPlot Object**************
# Pass the dataframe to OverUnderPlot and apply Bloomberg styles
ex9 = bqv.OverUnderPlot(df3).set_style()

# Display the plot
ex9.show()


#*******************Compound Plot Objects****************

#***********************ComparisonPlot Object****************

# Pass the dataframe to ComparisonPlot
ex10 = bqv.ComparisonPlot(compare)

# Display the plot
ex10.show()



#********************MultiComparisonPlot Object***************

# Pass the dataframe to MultiComparisonPlot
ex11 = bqv.MultiComparisonPlot(port1, port2)

# Display the plot
ex11.show()

# Define a list with the title values
legend_titles =['Portfolio ABC', 'Portfolio XYZ']

# Pass the list to the titles parameter
ex12 = bqv.MultiComparisonPlot(port1, port2, titles=legend_titles)

# Display the plot
ex12.show()



#*****************Grid Objects************************

#************GridPlot Object*************

# Pass the dataframe to GridPlot
ex13 = bqv.GridPlot(tear_sheet2)

# Display the plot
ex13.show()


# Use the plots parameter to specify the BarPlot object for all charts
ex14 = bqv.GridPlot(tear_sheet2, plots=bqv.BarPlot)

# Display the plot
ex14.show()

# Define a list of base plot objects
grid = [bqv.LinePlot, 
        bqv.BarPlot, 
        bqv.LinePlot, 
        bqv.BarPlot, 
        bqv.LinePlot, 
        bqv.BarPlot, 
        bqv.LinePlot]

# Pass the list to the plots parameter
ex15 = bqv.GridPlot(tear_sheet2, plots=grid)

# Display the plot
ex15.show()


# Set the number of columns to 2
# Set the relative column widths to 70/30
ex16 = bqv.GridPlot(tear_sheet2, plots=grid, cols=2, widths=['70%', '30%'])

# Display the plot
ex16.show()


#*************************MultiGridPlot Object******************

# Create a list of base plot objects with the syntax:
# (base plot object, title as string, list of column names)
plots = [
    (bqv.LinePlot, 'Plot 1', ['Min Monthly Return', 'Max Drawdown']),
    (bqv.BarPlot, 'Plot 2', ['Num Up Months', 'Num Down Months'])
]

# Pass the dataframe and the list MultiGridPlot
# Specify two columns
ex17 = bqv.MultiGridPlot(tear_sheet2, plots, cols=2)

# Display the plot
ex17.show()




#*************************Interactive Objects********************

#************************InteractiveLinePlot Object **********************

# Pass the dataframe to InteractiveLinePlot
ex18 = bqv.InteractiveLinePlot(multidf)

# Display the plot
ex18.show()


# Set the hide_controls attribute value to True
int_line = bqv.InteractiveLinePlot(multidf, hide_controls=True)

# Display the plot
int_line.show()



#***************************InteractiveScatterPlot Object**********************

# Pass the dataframe to InteractiveScatterPlot
int_scatter = bqv.InteractiveScatterPlot(multidf)

# Display the plot
int_scatter.show()


# Set the hide_controls attribute value to True
int_scatter2 = bqv.InteractiveScatterPlot(multidf, hide_controls=True)

# Display the plot
int_scatter2.show()


