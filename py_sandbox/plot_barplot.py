'''
date: 200410
objective: try to make bar plots display easily and correctly

'''

import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# x1 = [20, 34, 30, 35, 27]
# x2 = [25, 32, 34, 20, 25]

x1=[20]
x2=[25]

wide = .7
data = [x1] # ,x1,x2,x1
width = wide/len(data)
x = np.arange(len(labels))  # the label locations

fig, ax = plt.subplots()
# ax.bar(midpoint of each bar, height, width of each bar)
rects = []
for i,idat in enumerate(data):
    # rects.append(   ax.bar(x-wide+width/2+(i+3)*width, idat,width)   )
    rects.append(   ax.bar(x+(i)*width, idat,width)   )


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ticklocs=x
print(ticklocs)
ax.set_xticks(ticklocs)
ax.set_xticklabels(labels)

# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
# for irect in rects:
#     autolabel(irect)

fig.tight_layout()

plt.show()