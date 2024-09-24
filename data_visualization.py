from statistics import correlation

import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import pairplot


def generate_seaborn_plot():
    df = sns.load_dataset("iris")

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="sepal_length", y="sepal_width", hue='species', data=df)

    plt.savefig('static/img/seaborn_plot.png')
    plt.close()

    #heatmap

    df_numeric=df.select_dtypes(include='number')
    plt.figure(figsize=(10, 6))
    correlation_matrix= df_numeric.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.savefig('static/img/seaborn_heatmap.png')
    plt.close()

#box plot

    plt.figure(figsize=(10, 6))
    sns.boxplot(x="species", y="sepal_length", data=df)
    plt.savefig('static/img/seaborn_boxplot.png')
    plt.close()

#pairplot
    sns.pairplot(df, hue='species')
    plt.savefig('static/img/seaborn_pairplot.png')
    plt.close()