import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(1,10,100)
b=np.sin(a)

#sin and cosine wave together
#c=np.cos(a)
#plt.plot(a,b)
#plt.plot(a,c)
#plt.show()
#adding labels
#plt.title("sin and cosine wave")
#plt.xlabel("angle")
#plt.ylabel("cos and sin wave")
#plotting a parabola

#d=np.linspace(1,10,100)
#e=d**2
#plt.plot(d,e)

#bar plot
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
speakers=[100,233,45,678]
languages=['ENGLISH','GERMAN','SPANSIH','HINDI']
ax.bar(languages,speakers)
plt.xlabel('languages')
plt.ylabel('number of speakers')
plt.show()````````````````````````````````````````````````````````````````````````````````