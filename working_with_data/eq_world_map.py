import plotly.express as px
from eq_explore_data import lats, lons, mags, eq_titles, title


fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,)
fig.show()
