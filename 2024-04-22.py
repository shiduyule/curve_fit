# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:19:16 2024

@author: shiduyule
"""

import numpy as np

data = np.array([1, 2, np.nan, 4, np.inf, 6])

# 删除包含NaN或inf的元素
cleaned_data = data[~np.isnan(data) & np.isfinite(data)]

print(cleaned_data)
