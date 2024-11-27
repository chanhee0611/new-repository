import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
cpu=pd.read_csv('CPU_r23_v2.csv')
st.title('cpu ranking')
st.dataframe(cpu)

amd_cpu = cpu[cpu['manufacturer'] == 'AMD']
intel_cpu = cpu[cpu['manufacturer'] == 'Intel']

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

amd_cpu5 = amd_cpu.sort_values('multiScore', ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(amd_cpu5['cpuName'], amd_cpu5['multiScore'])
for idx, txt in enumerate(amd_cpu5['multiScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('multi Score')
plt.title('AMD CPU multi score top 5')
plt.xticks(rotation=45)
plt.ylim(40000,80000)

intel_cpu = intel_cpu.sort_values('singleScore', ascending=False).head(7)

plt.figure(figsize=(10, 6))
plt.bar(intel_cpu['cpuName'], intel_cpu['singleScore'])
for idx, txt in enumerate(intel_cpu['singleScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('Single Score')
plt.title('Intel CPU single top 7')
plt.xticks(rotation=45)
plt.ylim(1900,2100)

intel_cpu5 = intel_cpu.sort_values('multiScore', ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(intel_cpu5['cpuName'], intel_cpu5['multiScore'])
for idx, txt in enumerate(intel_cpu5['multiScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('multi Score')
plt.title('Intel CPU multi score top 5')
plt.xticks(rotation=45)
plt.ylim(25000,28000)

cpu7_s = cpu.sort_values('singleScore', ascending=False).head(7)

plt.figure(figsize=(10, 6))
plt.bar(cpu7_s['cpuName'], cpu7_s['singleScore'])
for idx, txt in enumerate(cpu7_s['singleScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('Single Score')
plt.title('전체 CPU 싱글 스코어 top 7')
plt.xticks(rotation=45)
plt.ylim(1900,2100)

cpu5_m = cpu.sort_values('multiScore', ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(cpu5_m['cpuName'], cpu5_m['multiScore'])
for idx, txt in enumerate(cpu5_m['multiScore']):
    plt.text(idx, txt+3, str(txt), ha='center',color='blue')
plt.xlabel('CPU Name')
plt.ylabel('multi Score')
plt.title('all CPU multi top 5')
plt.xticks(rotation=45)
plt.ylim(40000,80000)
