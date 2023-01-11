import csv
import mysql.connector
try:
  mydb = mysql.connector.connect(
  host="hostname",
  user="username",
  password="password"
  )
except Exception as e:
  print("Error while connecting to MySQL", e)
else:
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE IF NOT EXISTS youtube")
  mycursor.execute("SHOW DATABASES")
  for x in mycursor:
    if x[0] == "youtube":
      try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS youtube.CSV_LOAD (region VARCHAR(255),video_id VARCHAR(255), \
        trending_date VARCHAR(255), title LONGTEXT, channel_title VARCHAR(255), category_id VARCHAR(255),\
        category VARCHAR(255), publish_time LONGTEXT, tags LONGTEXT, views VARCHAR(255), likes VARCHAR(255),\
        dislikes VARCHAR(255), comment_count VARCHAR(255), thumbnail_link VARCHAR(255), comments_disabled VARCHAR(255), \
        ratings_disabled VARCHAR(255), video_error_or_removed LONGTEXT, description LONGTEXT)")
        #break
      except Exception as e:
        print("Error in creating table: ",e)
      else:
        try:
          #open the clean csv to read content
          samplecsvfile = open("clean_output.csv", "r", errors="ignore")
          samplecsvfilereader = csv.reader(samplecsvfile)
          sampledata = list(samplecsvfilereader)
        except Exception as e:
          print("Unable to extract information from csv file ",e)
        else:
          samplecsvfile.close()
          insert_data = []
          #converting each element of reader list to tuple and inserting to new list
          for data in range(1, len(sampledata)):
            insert_data.append(tuple(sampledata[data]))
          mySql_insert_query = '''INSERT INTO youtube.csv_load (region,video_id, trending_date, title, channel_title, category_id,
          category, publish_time, tags, views, likes,dislikes, comment_count, thumbnail_link , comments_disabled,
          ratings_disabled , video_error_or_removed , description) 
          VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

          try:
            #insert records from clean csv to mysql db
            mycursor.executemany(mySql_insert_query, insert_data)
            mydb.commit()
          except Exception as e:
            print("Error in inserting to table: ", e)
          else:
            mycursor.close()
  mydb.close()
