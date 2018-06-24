import scipy.stats as ss

x = [1,2,3,1,1]
y = [1,2,1,1,1]

r = ss.pearsonr(x,y)
print(r)

