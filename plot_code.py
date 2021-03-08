import numpy as np
import scipy.stats as ss
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def plot_summary(data,col_name):
    var=data[col_name].values
    summary_df=pd.DataFrame({'min':[np.min(var)],'mean':[np.mean(var)],
              'D1' : [np.percentile(var,10)],
              'Q1' : [np.percentile(var,25)],
              'Interquartile Range ':[ss.iqr(var)],
              'median ':[np.median(var)],'Mode ':[ss.mode(var)],
              'Q3' : [np.percentile(var,75)],
              'D9' : [np.percentile(var,90)],
             'max':[np.mean(var)],'varince':[np.mean(var)],
             'Coefficent of variation ':[ss.variation(var)],
            '2nd central moment ':[ss.moment(var,moment=2)],
            '3rd central moment ':[ss.moment(var,moment=3)],
            'kurtosis ':[ss.kurtosis(var)],'skewness ':[ss.skew(var)],
            'length ':len(var)                            
             }).T
    summary_df.columns=['statistics_value']
    summary_df=round(summary_df,3)
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(['statistic','values']),
                    fill_color='royalblue',
                    align='center',
                   font=dict(color='white', size=18)),
        cells=dict(values=[summary_df.index, summary_df.values],
                   fill_color='rgb(107, 174, 214)',
                   align='left',
                   font=dict(color='black', size=14)))
    ])
    fig.update_layout(title='statistic summary of univariate data',plot_bgcolor='white',paper_bgcolor='white',font_color='black',
                     width=600, height=800,font=dict(size=18) ,title_x=0.5)
    return fig.show()


    def plot_histogram(df,col_name):
    fig = px.histogram(df, x=col_name,nbins=30)
    fig.add_annotation(x=np.percentile(df[col_name],25),y=0,
                text="Q1",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=np.percentile(df[col_name],50),y=0,
                text="Median",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=np.percentile(df[col_name],75),y=0,
                text="Q3",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=np.percentile(df[col_name],10),y=0,
                text="D1",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=np.percentile(df[col_name],90),y=0,
                text="D9",
                showarrow=True,
                arrowhead=1)
    fig.update_layout(title='Univariate data historgam',plot_bgcolor='white',paper_bgcolor='white',font_color='black',
                     width=800, height=800,font=dict(size=18) ,title_x=0.5)
    return fig.show()
