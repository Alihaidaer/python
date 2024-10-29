### -barplots ( for categorical veriable creat bar plot)
import seaborn as sns
import matplotlib.pyplot as plt

titanic=sns.load_dataset("titanic")
sns.set_theme(style="ticks",color_codes=True)
sns.catplot(x="sex" , y="survived" , hue="class" , kind="bar", data=titanic)
plt.show()


# -scatterplot  (  for continus veriable  creat )
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
titanic=sns.load_dataset("titanic")
g=sns.FacetGrid(titanic, row="sex" , hue="alone")
g=(g.map(plt.scatter,"age","fare").add_legend())
plt.show()


## -countplots
import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="ticks", color_codes=True)
titanic= sns.load_dataset("titanic")
p1=sns.countplot(x='sex', data=titanic, hue='class')
p1.sns.set_title("plot for couting")
plt.show()