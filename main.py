import warnings
warnings.filterwarnings('ignore')

import sys
import pandas as pd
import numpy as np
import re
from plotnine import *


pre_sale = pd.read_csv('전국_평균_분양가격_2021.7월_.csv', sep='\t', engine='python', encoding='CP949') # 파일 불러오기

print(pre_sale.head())
print(pre_sale.info())