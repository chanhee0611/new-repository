import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
cpu=pd.read_csv('CPU_r23_v2.csv')
st.title('cpu ranking')
st.dataframe(cpu)

amd_cpu = cpu[cpu['manufacturer'] == 'AMD']
amd_cpu = amd_cpu.sort_values('singleScore', ascending=False).head(7)

fig=plt.figure(figsize=(10, 6))
plt.bar(amd_cpu['cpuName'], amd_cpu['singleScore'])
for idx, txt in enumerate(amd_cpu['singleScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('Single Score')
plt.title('AMD CPU single score top 7')
plt.xticks(rotation=45)
plt.ylim(1400,1700)
st.pyplot(fig)
