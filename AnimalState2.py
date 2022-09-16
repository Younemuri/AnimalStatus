import pandas as pd
import matplotlib.pyplot as plot
from matplotlib import font_manager, rc


df = pd.read_csv('C:/animal_data/Daejeon_Abandoned_Animals_Status.csv', encoding='cp949')
df = df[['구분', '2018년 개', '2019년 개', '2020년 개']]

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df.plot()
plot.title("대전유기견보호현황 분석 그래프")
plot.xlabel("월")
plot.ylabel("유기견 수(마리)")

plot.show()
