#!/usr/bin/env python
# coding: utf-8

# In[1]:


# open vcf file
# read vcf file
# add FORMAT column to vcf file with GT
# add SAMPLE column with 0/0 if REF matches ALT or 1/1 if ALT matches ALT
# Rename SAMPLE column to match input file prefix
# write vcf file

import sys
import os 
import re
import gzip


# In[2]:


# automate the reading and formatting of data from multiple input files.
vcf1 = []
vcf2 = []

for i in range(1,3):
    vcf = open('vcf'+str(i)+'.vcf')
    # Read by line
    vcf = vcf.readlines()
    # Add header row
    vcf[:0] = ["CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE"]
    # Split by tabs. Create list of lists
    vcf = [line.split('\t') for line in vcf]
    if i == 1:
        vcf1.extend(vcf)
    elif i == 2:
        vcf2.extend(vcf)

print(vcf1)
print(vcf2)

for row in vcf1:
    print(row)
    print(len(row))


# In[3]:


# Try this: https://www.geeksforgeeks.org/appending-to-list-in-python-dictionary/
# This works! Now make it scalable.
#dict1 = {'CHROM':[],'POS':[], 'ID':[], 'REF':[], 'ALT':[], 'QUAL':[], 'FILTER':[], 'INFO':[], 'FORMAT':[], 'SAMPLE':[]}
#keys = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'EXTRA','FORMAT', 'SAMPLE']

#for row in vcf1[1:]:
#    for item in row:
#        item_index = row.index(item)
#        # print(item_index) = 0,1,etc.
#        key = keys[item_index]
#        if key in dict1:
#            dict1[key].append(item)
#print(dict1)
# This is a great way to make dictionary from scratch
#    for key in keys:
#        test_dict[str(key)]= 1


# In[4]:



dict1 = {'CHROM':[],'POS':[], 'ID':[], 'REF':[], 'ALT':[],'QUAL':[], 'FILTER':[], 'INFO':[], 'FORMAT':[], 'SAMPLE':[]}
dict2 = {'CHROM':[],'POS':[], 'ID':[], 'REF':[], 'ALT':[],'QUAL':[], 'FILTER':[], 'INFO':[], 'FORMAT':[], 'SAMPLE':[]}
samples = [vcf1, vcf2]
keys = ['CHROM', 'POS', 'ID', 'REF', 'ALT','QUAL', 'FILTER', 'INFO','FORMAT', 'SAMPLE']

for sample in samples:
    for row in sample[1:]:
        row[2] = row[-1]
        row.pop(-1)
        #print("TEST", row)
        ref = row[3]
        alt = row[4]
        row.append('GT')
        if ref == alt:
            row.append('0|0')
        else:
            row.append('1|1')
        for i in range(0,10):#row:
            #item_index = row.index(i)
            key = keys[i]#item_index]
            print(i, key)#item_index, key)
            if sample == vcf1:
                dict0 = dict1
            else:
                dict0 = dict2
            if key in dict0:
                dict0[key].append(row[i])
                
for key in dict1:
    print(key, len(dict1[key]), dict1[key])


# In[5]:


from fuc import pyvcf
# Now I need to figure out how to import: from fuc import pyvcf
vf1 = pyvcf.VcfFrame.from_dict([], dict1)
vf2 = pyvcf.VcfFrame.from_dict([], dict2)
final_vf = pyvcf.merge([vf1, vf2]).df
print(final_vf)
#ofav = pyvcf.VcfFrame.from_dict([], dict1)
#oann = pyvcf.VcfFrame.from_dict([], dict2)
#ofrank = pyvcf.VcfFrame.from_dict([], dict3)
#pyvcf.merge([ofav, oann, ofrank]).df


# In[ ]:




