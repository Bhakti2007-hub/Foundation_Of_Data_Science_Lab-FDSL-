import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import binom 

data=pd.read_csv("archive/Train_psolI3n.csv")

n=20
p=data['Email_Status'].mean()

x=np.arange(0,n+1) 
pmf=binom.pmf(x,n,p) 
cdf=binom.cdf(x,n,p) 

mean,var=binom.stats(n,p,moments='mv') 
std_dev=np.sqrt(var) 

print('Mean (Expected successful emails):',mean) 
print('Variance:',var) 
print('Standard Deviation:',std_dev) 

plt.figure(figsize=(8, 5))

plt.bar(x, pmf, color='skyblue', edgecolor='black', label='PMF')
plt.plot(x,pmf,marker='o',color='blue',linewidth=2,label='Binomial Curve')

plt.axvline(mean,color='red',linestyle='--',linewidth=2,label=f'Mean={mean:.2f}')

plt.title(f'Binomial Distribution of Email Status (n={n}, p={p:.2f})')
plt.xlabel('Number of Successful Emails')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show() 

p_at_least_5=1-binom.cdf(4,n,p) 
print('P(X>=5):',p_at_least_5) 

p_exactly_8=binom.pmf(8,n,p) 
print('P(X=8):',p_exactly_8)