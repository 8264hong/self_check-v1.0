单词  解释  忘记次数  程度  是否背过
create table word_(id int not null auto_increment,word varchar(20) not null,word_explanation varchar(50) not null,forget_number smallint,important smallint,pass smallint,primary key(id))default charset=utf8;
+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+------------------+-------------+------+-----+---------+----------------+
| id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| word             | varchar(20) | NO   |     | NULL    |                |
| word_explanation | varchar(50) | YES  |     | NULL    |                |
| forget_number    | smallint(6) | YES  |     | NULL    |                |
| important        | smallint(6) | YES  |     | NULL    |                |
| pass             | smallint(6) | YES  |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+
- 数据库
1. 这是我建的表    
2. 在复习完成后所有的forget会被清零，之后再次复习会用important取代  

- mysql_db.py  
1. 写了个数据库操作的类，里面放了些我这次需要用的对数据库操作的函数  

- word.py  
1. panel函数  
    1. 假的视图函数  
2. word_input函数  
    1. 输入要背的单词  
3. word_recite  
    1. 背诵  
    2. 每个单词出现两遍，什么都不输入为‘不认识’，输入为‘认识’  
    3. 每次‘不认识’会增加forget  
4. word_review   
    1. 复习  
    2. 以forget为参考进行随机选择  
    3. 如果forget全都为零则用important代替  
    4. 复习完成后所有的forget清零，import为forget的最大值  
    
- 备注  
  好长时间没写了，感觉写的很烂，有待改进的地方还有很多  
  在随机抽单词的地方也用了最原始的扩大列表的方法进行的  
    
