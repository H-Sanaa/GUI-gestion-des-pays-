import mysql.connector as MC
try:
    conn=MC.connect(host='localhost',database='gestion_pays',user='root',password='')
    mycursor=conn.cursor()
    # print("la connexion bien fait ")

except MC.Error as err:
    print(err) 


