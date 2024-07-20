import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data for population in 2022
data = {
    'Country Name': ['China', 'India', 'United States', 'Indonesia', 'Pakistan'],
    'Country Code': ['CHN', 'IND', 'USA', 'IDN', 'PAK'],
    '2022': [1444216107, 1393409038, 333616947, 276361783, 241550953],
    'Men': [725000000, 700000000, 165000000, 140000000, 120000000],
    'Women': [719216107, 693409038, 168616947, 136361783, 121550953]
}
df = pd.DataFrame(data)

# Static Bar Chart for Top Countries by Population in 2022
fig = px.bar(df.sort_values(by='2022', ascending=False).head(10), 
             x='Country Name', 
             y='2022',
             text='2022',  # Display population on hover
             labels={'2022': 'Population in 2022'},
             title='Top Countries by Population in 2022')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')  # Format population display
fig.update_xaxes(title='Country')
fig.update_layout(xaxis_tickangle=-45)
fig.show()

# Static Pie Chart for Gender Distribution (assuming sample data)
labels = ['Men', 'Women']
sizes = [df['Men'].sum(), df['Women'].sum()]
fig = px.pie(names=labels, values=sizes, title='Gender Distribution', color_discrete_sequence=['blue', 'pink'])
fig.show()

# Interactive World Map for Population in 2022
fig = px.choropleth(df, 
                    locations='Country Code', 
                    color='2022',
                    hover_name='Country Name',
                    color_continuous_scale='Viridis',
                    title='World Population in 2022')
fig.show()


