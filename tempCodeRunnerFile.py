fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
speakers=[100,233,45,678]
languages=['ENGLISH','GERMAN','SPANSIH','HINDI']
ax.bar(languages,speakers)
plt.xlabel('languages')
plt.ylabel('number of speakers')
plt.show()