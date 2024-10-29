# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load data set 

kashti = sns.load_dataset("titanic")
kashti

# draw a bar plot 
sns.barplot(x="who" , y ="alone" , hue="sex" , data= kashti , order=["woman","man","child"], color="red")
plt.show()