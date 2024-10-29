import plotly.express as px
df=px.data.gapminder()
fig=px.scatter(df,x="gdpPercap" ,
                y = "lifeExp" , animation_frame="year"
                , animation_group="country",   facet_col="continent",
                  size="pop" , color="continent", log_x=True ,
                    size_max=45 , range_x =[100,100000] , range_y=[25,90])
fig.show()