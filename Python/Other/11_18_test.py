import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Python\\Other\\3.txt'
data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=['Degree', 'Intensity'])

plt.figure(figsize=(10, 6))
plt.plot(data['Degree'], data['Intensity'], marker='.')

plt.xlabel('Degree')
plt.ylabel('Intensity')

plt.grid(True)
plt.show()