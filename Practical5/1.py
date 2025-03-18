#create the directory
language= {"JavaScript": 62.3, "HTML": 52.9, "Python": 52, "SQL": 51, "TypeScript": 38.5 }
#print it
print(language)

#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
#draw the bar plot
# Extract languages and percentages for plotting
languages = list(language.keys())
percentages = list(language.values())
width = 0.5 #the width of the bars
# Create a bar plot
p1= plt.bar(languages, percentages, width)
plt.title('Popularity of Programming Languages')
plt.xlabel('Languages')
plt.ylabel('Popularity percentage(%)')
#show the plot
plt.show()
#print a specifi language's popularity
selected_language = "Python"  # You can modify this variable to test other languages
if selected_language in language:
    print(f"The percentage of developers who use {selected_language} is {language[selected_language]}%")
else:
    print(f"Sorry, {selected_language} is not in the data.")