#make uk lists
uk_countries =[57.11,3.13,1.91,5.45]
uk_names =["England","Wales","Northern Ireland","Scotland"]
#make cn lists
cn_countries =[65.77,41.88,45.28,61.27,85.15]
cn_names =["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]


# Sort uk_countries and uk_names together
uk_combined = sorted(zip(uk_countries, uk_names))
uk_countries, uk_names = zip(*uk_combined)

# Convert back to lists
uk_countries = list(uk_countries)
uk_names = list(uk_names)

print(uk_countries)
print(uk_names)

# Sort cn_countries and cn_names together
cn_combined = sorted(zip(cn_countries, cn_names))
cn_countries, cn_names = zip(*cn_combined)

# Convert back to lists
cn_countries = list(cn_countries)
cn_names = list(cn_names)

print(cn_countries)
print(cn_names)



#draw the pie chart
import matplotlib.pyplot as plt
#draw the pie chart for uk
labels=uk_names
sizes=uk_countries
#prevent the names of the countries from overlapping
explode=(0.3,0.1,0,0)
plt.pie(sizes,labels=labels,autopct='%2.2f%%',shadow=False,startangle=90,explode=explode)
#make the pie chart a circle
plt.axis('equal')
plt.show()


#draw the pie chart for cn
labels=cn_names
sizes=cn_countries  
plt.pie(sizes,labels=labels,autopct='%2.2f%%',shadow=False,startangle=90)
#make the pie chart a circle
plt.axis('equal')
plt.show()
