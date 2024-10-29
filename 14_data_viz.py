 #steps involved in data visualizatiion
# step 1 import libraries 
import seaborn as sns
import matplotlib.pyplot as plt

#  step 2 set a theme
sns.set_theme(style="ticks" , color_codes =True)

# step 3 import data set  ( you can also import ur own data )
kashti= sns.load_dataset("titanic")

# tep 4-plot basic graph
p = sns.countplot(x="sex", data=kashti)
plt.show()


#count plot ki left side pt al ready count a jata han


#steps involved in data visualizatiion
# step 1 import libraries  ( )                                                      # [wirh 2 veriables ]
import seaborn as sns
import matplotlib.pyplot as plt

#  step 2 set a theme
sns.set_theme(style="ticks" , color_codes = True)

# step 3 import data set  ( you can also import ur own data )
kashti= sns.load_dataset("titanic")

# # tep 4-plot basic graph with 1 veriable  ( count )
# p = sns.countplot(x="sex", data=kashti)
# plt.show()


#count plot ki left side pt al ready count a jata han

# #step 5 plot basic graph with 2 variables (count plot )         # yaha 1 veriable extra add keya han  add key ha  hue = "class"
# p = sns.countplot(x="sex", data=kashti , hue="class")
# plt.show()

#step 6 plot basic graph with 2 variables (count plot )  with title        
p = sns.countplot(x="sex", data=kashti , hue="class")
p.set_title("plot for basic counting ")
plt.show()