import geopandas as gp

glaciers = gp.GeoDataFrame.from_file(
    "/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Seattle/StatePlane/Street_Network_Database.shp")


glaciers.plot()


import shapely
studyarea = shapely.geometry.box(-136., 56., -130., 60.)
ax1 = glaciers[glaciers.geometry.intersects(studyarea)].plot()
ax1.set_aspect(2)
fig = plt.gcf()
fig.set_size_inches(10, 10)