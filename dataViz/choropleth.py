import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import cufflinks as cf
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
init_notebook_mode(connected=True)
cf.go_offline()

from plotly import graph_objs as go

df=pd.read_csv("epa_air_quality_annual_summary.csv")

#Data pre-processing and clean up

df['pollutant_standard'].fillna('UNKNOWN',inplace=True)
df['parameter_name'].fillna('UNKNOWN',inplace=True)
df['city_name'].fillna('UNKNOWN',inplace=True)
df['county_name'].fillna('UNKNOWN',inplace=True)
df= df[df['parameter_name'] != 'Elapsed Sample Time']
df= df[df['parameter_name'] != 'Ambient Max Temperature']
df= df[df['parameter_name'] != 'Average Ambient Pressure']
df= df[df['parameter_name'] != 'Wind Direction - Scalar']
df= df[df['parameter_name'] != 'Relative Humidity']
df= df[df['parameter_name'] != 'Sample Volume']
df= df1[df1['parameter_name'] != 'Particle Number Total COunt']
df= df[df['parameter_name'] != df.parameter_name.str.contains('Sample',na=False) ]

#Outliers where the percentile data was above 10k
df[ df['seventy_five_percentile'] == df['seventy_five_percentile'].max() ] #1 record
df[ (df['seventy_five_percentile'] >= 10000.0) &  (df['seventy_five_percentile'] <= 20000.0 )] # 78 records

#  1980s - Hydro carbon California state only

df1.groupby(['state_name','year','parameter_name']).agg({'seventy_five_percentile':'count'})
df[ (df['seventy_five_percentile'] >= 5000.0) &  (df['seventy_five_percentile'] <= 10000.0 )] # 47 records
df1= df[ (df['seventy_five_percentile'] <= 90.0) & (df['seventy_five_percentile'] >= 0.6) ]

## normalize datasets
from sklearn import preprocessing

# Create x, where x the 'scores' column's values as floats
x = df1[['seventy_five_percentile']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
df_normalized = pd.DataFrame(x_scaled)

df1['seventy_five_percentile']= df_normalized

import cufflinks as cf
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
init_notebook_mode(connected=True)
cf.go_offline()

from plotly import graph_objs as go

# Load data frame and tidy it.

state_codes = {
    'District of Columbia' : 'DC','Mississippi': 'MS', 'Oklahoma': 'OK',
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR',
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA',
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ',
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT',
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT',
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV',
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND',
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY',
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH',
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD',
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA',
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX',
    'Nevada': 'NV', 'Maine': 'ME'}

data=dict(type='choropleth',
         locations=list(state_codes.values()),
         # plotly does not take state names rather codes, can use fif codes with county
         locationmode='USA-states',
         colorscale='Portland',
         text="Pollutant: " + df1['parameter_name'] + '<br>' + "Year: " + df1['year'].apply(str) + \
               '<br>' + "units_of_measure: " + df1['units_of_measure'].apply(str) ,
         z = df1['seventy_five_percentile'],
         colorbar={'title':'Pollutant Concentration Index'})

layout = dict(geo={'scope':'usa'})

choromap = go.Figure(data=[data], layout=layout)

iplot(choromap)
plot(choromap, filename='graph.html')
