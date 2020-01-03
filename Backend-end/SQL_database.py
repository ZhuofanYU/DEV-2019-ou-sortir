import pymysql


connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='nopassword',
                             db='mysql',
                             charset='utf8')

cursor = connection.cursor()

# TODO basic table of data
effect_row = cursor.execute('''
CREATE TABLE `users` (
  `name` varchar(32) NOT NULL,
  `age` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
''')


# insert data(tuple or list)
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))

# insert dictionary
info = {'name': 'fake', 'age': 15}
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)

connection.commit()
