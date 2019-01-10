# data processing
import pandas as pd
import numpy as np
import os.path
from bokeh.plotting import figure, output_file, show, save

def main():
    # do we have preprocessed data already
    if os.path.isfile("modifiedData.csv"):
        # load data to pandas
        analysis()
    else:
        # processing
        pre_pro()

def analysis():
    m_data = pd.read_csv("modifiedData.csv")
    # visualize
    print(m_data.head())
    vis(m_data)

    # Linear regression:
    regress()

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
    # modif_data = data[pd.notnull(data['sold'])]
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
    sold = data['sold'].tolist()
    print(hour)
    print(sold)
    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle(hour, sold, size=5, color="navy", alpha=0.5)

    # show the results
    save(p)
    # return 1

def regress():
    return 1


if __name__ == "__main__": main()
