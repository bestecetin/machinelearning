import numpy as np #çok boyutlu diziler,matrislerle çalışmak ileri düzey matematiksel işlem yapmak için kütüphane.
import pandas as pd #veri işlemesi ve ver analizi için kullanılan kütüphane.
import matplotlib.pyplot as plt #veri görselleştirilmesi için kullanılan pyhton kütüphanesi.
import seaborn as sns #istatiksel bir python veri görselleştirme kütüphanesidir.

from subprocess import check_output # subprocess standart girdi, çıktı ve hataları yönetmemizi sağlar.
print(check_output(["ls", "/Users/bestecetin/PycharmProjects/lab1/archive 2/pokemon.csv"]).decode("utf8")) #bir komutu çalıştırıp çıktısını geri döndürür
import os
for dirname, _, filenames in os.walk("/archive 2/pokemon.csv"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
data = pd.read_csv('/Users/bestecetin/PycharmProjects/lab1/archive 2/pokemon.csv')
data.head()
data.info()
data.corr()

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

data.head(10)

data.columns