import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')

pre_sale = pd.read_csv('전국_평균_분양가격_2021.7월_.csv', sep='\t', engine='python', encoding='CP949') # 파일 불러오기

d_list = pre_sale['지역명,규모구분,연도,월,분양가격(㎡)'].str.split(',')

pre_sale['지역명'] = d_list.str.get(0)
pre_sale['규모구분'] = d_list.str.get(1)
pre_sale['연도'] = d_list.str.get(2)
pre_sale['월'] = d_list.str.get(3)
pre_sale['분양가격(㎡)'] = d_list.str.get(4)

pre_sale_price = pre_sale['분양가격(㎡)']
pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')
pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3

print(pre_sale.head())
print(pre_sale.info())
print(pre_sale.describe())
print(pre_sale['지역명'].value_counts())
print(pre_sale['규모구분'].value_counts())
print(pre_sale['연도'].value_counts())

pre_sale_low_60 = pre_sale[pre_sale['규모구분'] == '전용면적 60㎡이하']
pre_sale_low_60_Seoul = pre_sale_low_60[pre_sale_low_60['지역명'] == '서울']
pre_sale_low_60_Chungbuk = pre_sale_low_60[pre_sale_low_60['지역명'] == '충북']
pre_sale_low_60_Seoul.plot(y = ['평당분양가격'])
pre_sale_low_60_Chungbuk.plot(y = ['평당분양가격'])
plt.show()