'''
Before running any of the examples in this notebook, you need to import the bqviz library, sample data, ipywidgets, 
and some libraries we will use to generate random data.
'''

import bqviz as bqv
from bqviz.sample_data import *
from ipywidgets import *
import random


#Displaying Multiple Figures in the Same Cell

# Create two bqviz plot objects
left_plot = bqv.QSpreadPlot(df3[:20], num_ticks=6)
right_plot = bqv.QSpreadPlot(df3[20:40], num_ticks=6)

# Create an HBox container to show the plots aligned horizontally
HBox([left_plot.show(), right_plot.show()])



# Create two bqviz plot objects and apply Bloomberg styles
top_plot = bqv.LinePlot(multidf, fig_style='narrow').set_style()
bottom_plot = bqv.LinePlot(df3, fig_style='narrow').set_style()

# Create a VBox container to show the plots aligned vertically
VBox([top_plot.show(), bottom_plot.show()])



#Updating Plots with New Data

# Create a bqviz LinePlot object and apply Bloomberg styles
line1 = bqv.LinePlot(multidf).set_style()

# Display the plot
line1.show()

# Create a dataframe of random data
random_df = pd.DataFrame(np.random.randn(100,4), 
                         index=multidf.index, 
                         columns=multidf.columns).apply(np.cumsum)

# Push the new dataframe to the above plot
line1.push(random_df)



#Compound Plots

# Create a bqviz ComparisonPlot object
compare_plot = bqv.ComparisonPlot(compare, legend='outside', num_ticks=8)

# Display the plot
compare_plot.show()

# Create a dataframe of random data
random_df = pd.DataFrame(np.random.randn(100,2), index=compare.index, 
                         columns=compare.columns).apply(np.cumsum)

# Push the new dataframe to the above plot.
compare_plot.push(random_df)



#Grid Plots

# Create a bqviz GridPlot object
grid = bqv.GridPlot(multidf, cols=2)

# Display the plot
grid.show()

# Create a dataframe of random data
random_df = pd.DataFrame(np.random.randn(100,4), 
                         index=multidf.index, 
                         columns=multidf.columns).apply(np.cumsum)

# Push the new dataframe to the above plot.
grid.push(random_df)



#Interactive App Example

def random_security():
    return ''.join([chr(np.random.randint(97, 97+26)) for i in range(4)]).upper()

random_fields = {'Sector 1': [random_security() for i in range(5)],
                 'Sector 2': [random_security() for i in range(7)],
                 'Sector 3': [random_security() for i in range(9)],}

def random_query(field1, field2):
    return pd.DataFrame(abs(np.random.randn(len(random_fields[field1]), len(field2))), 
                        index=random_fields[field1], columns=field2)
  

class BasicApp():
    def __init__(self):
        # Create a bqviz BarPlot and set some options
        self.plot = bqv.BarPlot(legend='outside')
        
        # Create some ipywidgets widgets to get user input
        self.button = Button(description='Submit')
        self.sec_menu = Dropdown(options=['Sector 1', 'Sector 2', 'Sector 3'], 
                                 description='Sectors')
        self.met_menu = SelectMultiple(options=['Metric 1', 'Metric 2', 'Metric 3'], 
                                       description='Metrics',
                                       value=['Metric 1'])
        
        # Use .on_click to attach a callback function to self.button
        self.button.on_click(self.query_db)
    
    def query_db(self, evt):       
        # Access the values of the widgets, use them to construct a query,
        # then save the returned dataframe to new_data
        new_data = random_query(self.sec_menu.value, self.met_menu.value)
        
        # Push the new data to the BarPlot object
        self.plot.push(new_data)
    
    def show(self):
        # Create an ipywidgets container to hold the widgets
        controls = widgets.HBox([self.button, self.sec_menu, self.met_menu])
        
        # Return a container to display the HBox of widgets and BarPlot
        return widgets.VBox([controls, self.plot.show()])
      
      
# Select an option from the "Sectors" dropdown, and one or more options from the
# "metrics" menu, then press "Submit" to generate and display some random data
BasicApp().show()      




#Using bqviz Interactive Objects

#Data Selection

# Create a bqviz InteractiveLinePlot object
int_line = bqv.InteractiveLinePlot(multidf, legend='outside', hide_controls=True)

# Display the plot
int_line.show()


#InteractiveScatterPlot

# Create some random data
random_df = pd.DataFrame(np.random.randn(26,2), 
                         index=[chr(i).upper() for i in range(97, 97+26)], 
                         columns=["Metric 1", 'Metric 2'])

# Create a bqviz InteractiveScatterPlot object
int_scatter = bqv.InteractiveScatterPlot(random_df,
                                         hide_controls=True, 
                                         reg_line=False, 
                                         indexes=True)
int_scatter.y = "Metric 2"

# Display the plot
int_scatter.show()

'''Data in the selected range is accessible from the selected_data attribute. Select a range on the figure above,
then uncomment and run the cell below to return a dataframe of the points in the selected range.'''
int_scatter.selected_data



#Plot Linking
# Create two bqviz objects
int_line_main = bqv.InteractiveLinePlot(multidf, legend='outside', 
                                        hide_controls=True, 
                                        title="Main plot")
line_subplot = bqv.LinePlot(legend=None, title="Subplot")

# Link line plot to interactive line plot
int_line_main.links = [line_subplot]

# Display bqviz objects in ipywidgets containers
VBox([int_line_main.show(), line_subplot.show()])



#Data Transformation

# Define a function that receives and returns a dataframe
def min_mean_max(df):
    return pd.DataFrame([df.min(), df.mean(), df.max()], 
                        index=['Min', 'Mean', 'Max']).dropna(axis=1).transpose()

# Create two bqviz objects
int_line_3 = bqv.InteractiveLinePlot(multidf, hide_controls=True, legend='outside')
bar_plot = bqv.BarPlot(legend='outside')

# Link bar plot on min_mean_max function to interactive plot
# Format: list of [plot, function] objects
int_line_3.links = [[bar_plot, min_mean_max]]

# Dislay bqviz objects in ipywidgets containers
VBox([int_line_3.show(), bar_plot.show()])




#Linking Multiple Plots and Functions

# Create some random data
random_scatter = pd.DataFrame(np.random.randn(20,4))
random_scatter.columns = ['Metric 1', 'Metric 2', 'Metric 3', 'Metric 4']
random_scatter['Category'] = [random.choice(['A', 'B', 'C']) for i in range(20)]

# Create bqviz objects and set some options
link_scatter = bqv.InteractiveScatterPlot(random_scatter, color_field='Category')
link_bar = bqv.BarPlot(padding=.2, title="Min/Mean/Max", legend='outside',
                       fig_style='narrow')
link_bar2 = bqv.BarPlot(legend=None, title='Category counts', tick_format='.0d', 
                        fig_style='narrow')

# Define transformation functions
def min_mean_max(df):
    return pd.DataFrame([df.min(), df.mean(), df.max()], 
                        index=['Min', 'Mean', 'Max']).dropna(axis=1).transpose()

def get_category_counts(df):
    return pd.DataFrame(df['Category'].value_counts())

# Link plots and functions
# Format: list of [plot, function] objects
link_scatter.links = [[link_bar, min_mean_max], [link_bar2, get_category_counts]]

# DIsplay plots in ipywidgets container
VBox([link_scatter.show(), HBox([link_bar2.show(), link_bar.show()])])
