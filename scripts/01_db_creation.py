# %%
import geopandas as gpd
import requests

# %%
path = r'C:\VM2GEO\SIG\LIM_MUN\SC_Municipios_2021.shp'
sc = gpd.read_file(path)

sc.drop(['CD_MUN', 'SIGLA', 'AREA_KM2', 'perimetro'], axis=1, inplace=True)

# TO DO: Pegar coordenadas x e y dos centroides/point_on_surface dos municípios para iterar na API do OpenWeather.