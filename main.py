import warnings
warnings.filterwarnings('ignore')

import sys
import pandas as pd
import numpy as np
import re
from plotnine import *


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