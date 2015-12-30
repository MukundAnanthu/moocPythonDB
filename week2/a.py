import sqlite3
import re

fh = open('mbox.txt')

conn = sqlite3.connect('abc.sqlite')
curs = conn.cursor()

curs.execute('''
DROP TABLE IF EXISTS Counts
''')

curs.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')


for line in fh:
    if line.startswith('From: '):
        email = line.split()[1]
        email = re.findall('.+@(.+)',email)[0]
        curs.execute('''
        SELECT count FROM Counts WHERE org=?
        ''', (email, ))

        row = curs.fetchone()
        print row
        if row is None:
            curs.execute('''
                INSERT INTO Counts(org,count) VALUES (?,1)
            ''', (email, ))
        else:
            curs.execute('''
                UPDATE Counts SET count = count + 1 WHERE org=?
            ''', (email, ))
        conn.commit()



sqlQuery = ''' SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'''

for row in curs.execute(sqlQuery):
    print str(row[0]),row[1]

curs.close()
