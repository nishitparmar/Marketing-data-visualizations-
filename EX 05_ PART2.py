'''
AUTHOR : NISHIT PARMAR
EXERCISE O5 , PART 2 . 
CWID : 10432431
'''

import matplotlib.pyplot as plt

#Define the function get_index

def get_index(parts):
    
    #Conditions for = Lower class, Medium class and Upper class respectively.
    
    if int(parts[0])<4:
        if int(parts[1])==1:
            return (0)
        else:
            return (1)
    if int(parts[0])>3 and int(parts[0])<7:
        if int(parts[1])==1:
            return (2)
        else:
            return (3)
    if int(parts[0])>6:
         if int(parts[1])==1:
            return (4)
         else:
            return (5) 

count=[0,0,0,0,0,0]
file_handle = open ("marketingdata.txt")
for line in file_handle:
    if "NA" in line:
        continue
    parts = line.strip().split()
    a= get_index(parts)
    count[a]= count[a]+1   
print'''

Who is at the mall? 
Lower class men: %s    Lower class women: %s
Middle class men: %s   Middle class women: %s 
Upper class men: %s   Upper class women: %s

''' %(count[0] , count[1] , count[2] , count [3] , count [4] , count[5])

#BAR GRAPH PLOTTING

x = [0,1,2,3,4,5]
y = [count[0],count[1],count[2],count[3],count[4],count[5]]
label =['Lower class Men', 'Lower class Women', 'Middle class Men', 'Middle class Women', 'High class Men', 'High class Women']
plt.subplot(2,2,1)
plt.bar(x,y)
plt.ylabel('INCOME')
plt.title('BAR CHART OF MARKETING DATA')
plt.xticks(x, label, rotation=90)

# PIE CHART PLOTTING
plt.subplot(2,2,2)
plt.title('PIE CHART OF MARKETING DATA')
plt.pie(y, labels = label, autopct = '%1.1f%%')
plt.suptitle("NUMBER OF MEN AND WOMEN AT THE MALL , BY SOCIAL CLASS")
plt.show()
              


