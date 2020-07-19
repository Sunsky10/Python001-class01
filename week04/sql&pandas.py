
import pandas as pd

data = pd.DataFrame({
    "id":[x for x in range(1000,2001,100)],
    "age":[x for x in range(10,21)]
    })
# table1 = data
# table2 = data

# 1. SELECT * FROM data;
data                #直接读取data数据

# 2. SELECT * FROM data LIMIT 10;
data.head(10)       #读取data前10行数据

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
data['id']          #取出data中id这一列的数据

# 4. SELECT COUNT(id) FROM data;
data['id'].count()    #统计data中id这一列数据的个数

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
data[ (data['id']<1000) & (data['age']>10) ]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.groupby('id').agg({'order_id':pd.Series.nunique})

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1,table2,on='id',how='inner')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1,table2])

# 9. DELETE FROM table1 WHERE id=10;
table1[~(table1['id'] == 10)]

# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop('column_name',axis = 1)