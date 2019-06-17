import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'alim1234',
    database = 'world'
)

qr_pop_asean = '''
SELECT country.Name as 'Negara_ASEAN', country.Population, country.GNP, 
Ibukota_Negara.Name as Ibukota, Ibukota_Negara.Population as Populasi_Ibukota
FROM country
JOIN Ibukota_Negara ON country.Code = Ibukota_Negara.CountryCode
WHERE country.Name IN ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
ORDER BY country.Name;
'''
qr_luas_daratan = '''
SELECT country.Name as 'Negara_ASEAN', country.SurfaceArea as 'Luas_Daratan'
FROM country
WHERE country.Name IN ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
ORDER BY country.Name;
'''

populasi_asean = pd.read_sql(qr_pop_asean, con=mydb)
luas_negara =  pd.read_sql(qr_luas_daratan, con=mydb)

negara = populasi_asean['Negara_ASEAN']
populasi = populasi_asean['Population']
gnp = populasi_asean['GNP']
luas = luas_negara['Luas_Daratan']


plt.subplot(2,2,1)
plt.bar(negara, populasi)
plt.title('Populasi Negara Asean')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt Jiwa)')
plt.xticks(rotation=45)

plt.subplot(2,2,2)
plt.pie(populasi, labels=negara, autopct='%.2f')
plt.title('Persentase Penduduk Asean')

plt.subplot(2,2,3)
plt.bar(negara, gnp)
plt.title('Populasi Negara Asean')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
plt.xticks(rotation=45)

plt.subplot(2,2,4)
plt.pie(luas, labels=negara, autopct='%.2f')
plt.title('Persentase Luas Daratan Asean')

plt.show()

