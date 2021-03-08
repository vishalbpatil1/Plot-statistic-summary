# Plot-statistic-summary
This code useful for analyst  to visualize univariate data statistics. 
first you have to add plot_code  file on your own python default dir.

#### import libraries
```python
import numpy as np
import scipy.stats as ss
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plot_code import plot_summary,plot_histogram
```

#### load data
```python
df= pd.read_csv(r"F:\\data\\diamonds.csv") 
```
#### plot summary table
```python
plot_summary(data=df,col_name='x')
```

![summar_plot](https://github.com/vishalbpatil1/Plot-statistic-summary/blob/main/newplot%50(5).png)


### plot histogram 
```python
plot_histogram(df=df,col_name='x')
```
![summar_plot](https://github.com/vishalbpatil1/Plot-statistic-summary/blob/main/newplot%50(4).png)
