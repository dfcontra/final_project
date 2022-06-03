#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:45:34 2022

@author: gowthamarumugam
"""

import numpy as np
import pandas as pd

words = pd.read_csv("/Users/gowthamarumugam/Documents/pp_data.csv")


def narrow(s,df,i):
    #s is a string, input word
    #df is the dataset in dataframe format
    #i is the character offset: 
    #eg if you want words in range one character more or less,then i=1
    length = len(s)
    vec = df["word"].str.len()
    lens = pd.DataFrame.to_numpy(vec)
    narrowedspacebool = np.logical_or(lens>(length+i),lens<(length-i))
    narrowedspacebool = np.logical_not(narrowedspacebool)
    return df[narrowedspacebool]










            
            