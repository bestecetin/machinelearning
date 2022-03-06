#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NUMPY TUTORIAL


# In[2]:


import numpy as np 


# In[3]:


tekBoyutluDizi= np.array([1.2,2.3,3.4,4.5,5.6,6.7])
print(tekBoyutluDizi)


# In[4]:


ikiBoyutluDizi=np.array([[1.2],[1.3],[1.4],[1.5]])
print(ikiBoyutluDizi)


# In[8]:


dizi=np.arange(5,12) #5 dahil 12 dahil değil arasında sayı dizisi oluştur.
print(dizi)


# In[17]:


np.zeros((2,2), dtype=np.int16)


# In[36]:


random_integers_between_50_and_100= np.random.randint(low=50, high=101, size=(6)) #50 ile 100 arasında random 6 tane elemanlı vektör oluştur.
print(random_integers_between_50_and_100)


# In[28]:


random_floats=np.random.random([3]) # np.random.random 0.0 ve 1.0 arasında random sayı üretir
print(random_floats)


# In[29]:


random_floats_between_2_and_3 = random_floats + 2.0 #yukarıdaki vektördeki her ögeye 2.0 ekledi böylece değerleriniz 2.0 ve 3.o arasında oldu.
print(random_floats_between_2_and_3)


# In[38]:


random_integers_between_150_and_300=random_integers_between_50_and_100*3 #yukarıdaki 50 ile 100 arasındaki 6 elemanlı vektörün her bir elemanını 3 ile çarptık.
print(random_integers_between_150_and_300)


# In[39]:


#TASK1
#1.Feature adlı bir NumPy dizisine 6 ila 20 (dahil) arasındaki tam sayı dizisini atayın.
#2.Label adlı bir NumPy dizisine şu şekilde 15 değer atayın: label = (3)(feature) + 4
feature=np.arange(6,21)
print(feature)
label=(feature*3)+4
print(label)


# In[48]:


#TASK2
#-2 ile +2 arasında farklı bir rastgele kayan nokta değeri ekleyerek label'a atanan her değeri değiştirin.
#label ile aynı boyuta sahip noise dizisi oluşturun.
noise = (np.random.random([15]) * 4) - 2
label = label + noise 
print(label)


# In[52]:


#PANDAS TUTORIAL
import pandas as pd


# In[64]:


myData=np.array([[0,3],[2,7],[15,4],[-3,4],[31,8],[10,2],[34,8]]) #7x2'lik bir numpy array
column_names=['temparature','activity'] #sütun isimleri
data_frame=pd.DataFrame(data=myData,columns=column_names) #dataframe oluşturduk
print(data_frame)


# In[65]:


print("Rows #0, #1 and #2:")
print(data_frame.head(3),'\n') #ilk 3 dataframe verisini görüntüledik.


# In[59]:


print("Row #2:")
print(data_frame.iloc[[2]],'\n')#2. indisteki veriler gelir.


# In[69]:


print("Rows #1, #2 and #3:")
print(data_frame[2:5],'\n') #birinci indis dahil fakat ikinci indis dahil değil yani 2 ve 4 dahil aradaki de veriler gelecek.


# In[71]:


print("Column 'temparature:'")
print(data_frame['temparature'])#sadece temparature sütunu verilerini getirir.


# In[95]:


#TASK1
#Create an 3x4 (3 rows x 4 columns) pandas DataFrame in which the columns are named 
#Eleanor, Chidi, Tahani, and Jason. Populate each of the 12 cells in the DataFrame with a random integer 
#between 0 and 100, inclusive.
#Output the following:
#the entire DataFrame
#the value in the cell of row #1 of the Eleanor column
#Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason.
people=['Eleanor','Chidi','Tahani','Jason']
r_int=np.random.randint(low=0,high=101,size=(3,4))
people_df=pd.DataFrame(data=r_int,columns=people)
print(people_df)

print("the value in the cell of row #1 of the Eleanor column: ",people_df['Eleanor'][1])

people_df['Janet']=people_df['Tahani']+people_df['Jason']
print(people_df)


# In[114]:


df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])
print(df)
reference_to_df=df; 


# In[115]:


df.at[5,'B']=df['B'][5]+8 #at=>Access a single value using a label.
print("Güncellenmis df=%d"%df['B'][5])
print("Güncellenmiş referans df=%d"%reference_to_df['B'][5])


# In[117]:


copy_of_my_df=df.copy()
df.at[4,'A']=df['A'][4]+10
print("Güncellenmis df=%d"%df['A'][4])
print("Güncellenmis copy df=%d"%copy_of_my_df['A'][4])


# In[118]:


print(df)


# In[ ]:




