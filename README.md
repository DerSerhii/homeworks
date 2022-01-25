# homeworks
'''
2.
select concat('This is ', name, case gender when 'm' then ', he' when 'f' then ', she' end, ' has email ', email) as info from people;

This is Vasya, he has email sadsd@sdsdsa.com
 This is Alex, he has email ksj2@sdfdssa.com
 This is Alexey, he has email ywy3@df.com
 This is Helen, she has email hel3@cder.com
 This is Jenny, she has email jer23@sdfdsf.com
 This is Lora, she has email lora@sasdsf.com

3.
select concat('We have ', count(id), ' boys!') as "Genger information:" from people where gender = 'm'
library-# union
library-#  select concat('We have ', count(id), ' girls!') as "Genger information:" from people where gender = 'f';

 Genger information:
---------------------
 We have 3 boys!
 We have 3 girls!
 
5.
select name, count(*) as words from vocabulary v left join word ON  word.vocabulary_id=v.id group by vocabulary_id, name order by name;

name   | words
---------+-------
 animals |    10
 human   |    10
 nature  |    10
 school  |    10
 SF      |    10


'''
