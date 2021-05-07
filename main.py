import folium
import pandas as pd

places = pd.read_excel('Naughty_Places.xlsx')

m = folium.Map(location=[45.216958, 3.317702], tiles='cartodbdark_matter', zoom_start=4)
ftr_grp1 = folium.FeatureGroup(name='Naughty Places')

for i in range(0, len(places)):
    html=f"""
    <h1>{places.iloc[i]['Location']}</h1>
    <p>{places.iloc[i]['Country']}<p>
    """
    iframe = folium.IFrame(html=html, width=200, height=100)
    popup = folium.Popup(iframe, max_width=200)
    folium.Marker([places.iloc[i]['Latitude'],places.iloc[i]['Longitude']],
                  popup=popup,
                  icon=folium.DivIcon(html=f"""
                                      <div><svg>
                                          <circle cx="5" cy="5" r="4" fill="#F70000" opacity="2.0"/>
                                      </svg></div>""")
                                      ).add_to(ftr_grp1)


title = '<title>Naughty Places Map</title>'
m.get_root().html.add_child(folium.Element(title))

m.add_child(ftr_grp1)
m.add_child(folium.LayerControl(position='topright', collapsed=True))
m.save('./index.html')