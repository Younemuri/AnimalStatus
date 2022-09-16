import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('C:/animal_data/Daejeon_Abandoned_Animals_Status.csv', encoding='cp949')
df = df[['구분', '2018년 개']]

plot.figure(figsize=(15, 8))
plot.rcParams['font.family'] = 'Malgun Gothic'
plot.rcParams.update({'font.size': 22})

ax = df.set_index('구분')['2018년 개'].plot(kind='line', marker='d')
ax.set_ylabel("유기견 수(마리)")
ax.set_xlabel("2018년")

plot.show()
