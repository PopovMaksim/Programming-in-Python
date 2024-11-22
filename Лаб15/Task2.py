import pandas as pd

import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('source.csv', sep=',', encoding='latin1',parse_dates=['Date'], dayfirst=True, index_col='Date')
fixed_df = fixed_df.iloc[:, 2:4]
columns = list(fixed_df.columns)
fixed_df['Total'] = fixed_df.sum(axis=1)
fixed_df['Month'] = fixed_df.index.month
df_by_month = fixed_df.groupby('Month')['Total'].sum()
popular_month = df_by_month.idxmax()
quantity  = int(df_by_month[popular_month])
print("Пошук найпопулярнішого місяці для велодоріжок", columns)
print("Найпопулярніший місяць: {}, Кількість велосипедистів: {}".format(popular_month, quantity))

df_by_month.plot(kind='bar', color='red')
plt.title("Кількість велосипедистів у 2016 році на велодоріжках"+str(columns))
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(12), [
    "Січень", "Лютий", "Березень", "Квітень", "Травень",
    "Червень", "Липень", "Серпень", "Вересень", "Жовтень",
    "Листопад", "Грудень"
], rotation=0)
plt.show()