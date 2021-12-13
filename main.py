import warnings
warnings.filterwarnings('ignore')

import sys
import pandas as pd
import numpy as np
import re
from plotnine import *


pre_sale = pd.read_csv('전국_평균_분양가격_2021.7월_.csv', sep='\t', engine='python', encoding='CP949') # 파일 불러오기

print(pre_sale.hist())
#pre_sale['연도'] = pre_sale['연도'].astype(str)  # 연도와 월은 카테고리 형태의 데이터이므로 스트링 형태로 변경
#pre_sale['월'] = pre_sale['월'].astype(str)

#pre_sale_price = pre_sale['분양가격(㎡)']                               # 분양가격을 평당분양가격으로 전처리
#pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')   # 분양가격의 타입을 숫자로 변경
#pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3                     # 평당 분양가격 추출