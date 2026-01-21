import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
subjects=['maths','science','english']
scores=[30,70,80]
plt.bar(subjects,scores,color="orange")
plt.title("Subject scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()
#plotting histogram
data=np.random.randn(800)
plt.figure(figsize=(10,6))
plt.hist(data,bins=20,color="purple",edgecolor="black")
plt.title("Histogram of random data")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()
