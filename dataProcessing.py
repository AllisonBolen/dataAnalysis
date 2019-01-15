# data processing
import pandas as pd
import numpy as np
import os.path
from bokeh.plotting import figure, output_file, show, save

def main():
    # do we have preprocessed data already
    while(os.path.isfile("modifiedData.csv") is False):
        # processing
        pre_pro()
    # load data to pandas
    analysis()

def analysis():
    m_data = pd.read_csv("modifiedData.csv")
    # visualize
    print(m_data.head())
    vis(m_data)

    # Linear regression:
    regress(m_data)

    # save data to pandas


def pre_pro():
    '''
    remove or replace nan values

    In the original downloads file there are 8 null values out of 24*31, it makes sense to delete those values because they are so few as to not affect the overall data set

    source: https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-certain-columns-is-nan
    '''
    # load unmodified data
    data = pd.read_csv("./downloads.csv")
    print(data.head())

    null_values = data.columns[data.isnull().any()]
    sum = data[null_values].isnull().sum()
    #print("Count of nulls:\n" + str(sum))

    # create new data set out of he original containing only the valid rows
    # modif_data = data[pd.notnull(data['downloaded'])]
    modif_data = data.dropna()
    # reassign index
    modif_data.reset_index(drop=True, inplace=True)
    print(modif_data.head())
    saveModif(modif_data)
    return 1


def saveModif(modif_data):
    modif_data.to_csv("modifiedData.csv", index=False)
    return 1


def vis(data):

    hour = data['hour'].tolist()
    downloaded = data['downloaded'].tolist()

    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    if 'prediction' in data.columns:
<<<<<<< HEAD
=======
        print("THISS IS THE PRED LINE")
>>>>>>> 8c2ad8cf2fb082627789e2319fa89b2313d6a60e
        pred = data['prediction'].tolist()
        p.line(hour, pred, line_width=2, line_color='red')

    # add a circle renderer with a size, color, and alpha
    p.circle(hour, downloaded, size=5, color="navy", alpha=0.5)

    p.xaxis.axis_label = "Hour of Month"
    p.xaxis.axis_label_text_color = "#aa6666"
    p.xaxis.axis_label_standoff = 30

<<<<<<< HEAD
    p.yaxis.axis_label = "Number of Books Downloaded"
=======
    p.yaxis.axis_label = "Number of books downloaded"
>>>>>>> 8c2ad8cf2fb082627789e2319fa89b2313d6a60e
    p.yaxis.axis_label_text_font_style = "italic"

    # show the results
    save(p)
    return 1


def regress(data):
    x_sum, y_sum, products_sum, sum_x_squares, sum_y_squares = preclaculations(data)
    number_of_values = len(data.index)
    # slope
    a = number_of_values * products_sum
    b = x_sum * y_sum
    c = number_of_values * sum_x_squares

    a_sub_b = a - b
<<<<<<< HEAD
    c_sub_sum_x_squares = c - x_sum**2
=======
    c_sub_sum_x_squares = c - sum_x_squares
>>>>>>> 8c2ad8cf2fb082627789e2319fa89b2313d6a60e

    slope = a_sub_b / c_sub_sum_x_squares
    print("slope: " + str(slope))

    # intercept
    e = slope * x_sum
    f = y_sum - e
    intercept = f / number_of_values
    print("intercept: " + str(intercept))

    # y = mx + b
    data['prediction'] = data.hour*slope + intercept
<<<<<<< HEAD

=======
    
>>>>>>> 8c2ad8cf2fb082627789e2319fa89b2313d6a60e
    print(data.head())

    vis(data)
    return 1

def preclaculations(data):
    # sum of all the x values
    x_sum = data['hour'].sum()
    print("The sum of the hour values: " + str(x_sum))
    # sum of all the y vals
    y_sum = data['downloaded'].sum()
    print("The sum of the downloaded values: " + str(y_sum))
    # sum of the products of x and y pair
    products = data.hour * data.downloaded
    products_sum = products.sum()
    print("The sum of the products of the xy pairs values: " + str(products_sum))
    # sum of the squares of every X value
    x_squares = data.hour**2
    sum_x_squares = x_squares.sum()
    print("The sum of the squares for every hour value: " + str(sum_x_squares))
    # sum of the squares of every y value
    y_squares = data.downloaded**2
    sum_y_squares = y_squares.sum()
    print("The sum of the squares for every downloaded value: " + str(sum_y_squares))

    return x_sum, y_sum, products_sum, sum_x_squares, sum_y_squares

if __name__ == "__main__": main()
