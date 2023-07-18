import os
import json
import csv
import mysql.connector as sql 
import pandas as pd

loc1= "C:/Users/lenovo/desktop/DS/phonepe/pulse-master/data/aggregated/transaction/country/india/state/"

dic1={"State":[], "Year":[], "Quarter":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}

agg_trans_list=os.listdir(loc1)

print(agg_trans_list)

for state in agg_trans_list:
    year_loc=loc1+state+"/"
    agg_trans_year= os.listdir(year_loc)

    for year in agg_trans_year:
        files_loc=year_loc+year+"/"
        agg_trans_files= os.listdir(files_loc)
        
        for file  in agg_trans_files:
            file_1=files_loc+file
            data=open(file_1,"r")
            A=json.load(data)
            
            for i in A["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                dic1["Transaction_type"].append(name)
                dic1["Transaction_count"].append(count)
                dic1["Transaction_amount"].append(amount)
                dic1["State"].append(state)
                dic1["Year"].append(year)
                dic1["Quarter"].append(int(file.strip(".json")))

df_agg_trans=pd.DataFrame(dic1)


loc2= "C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/data/aggregated/user/country/india/state/"

dic2={"State":[], "Year":[], "Quarter":[], "Brands":[], "Count":[], "Percentage":[]}

agg_user_list=os.listdir(loc2)

for state in agg_user_list:
    st=loc2+state+"/"
    agg_user_year=os.listdir(st)

    for year in agg_user_year:
        yr=st+year+"/"
        agg_user_file=os.listdir(yr)

        for file in agg_user_file:
            file2=yr+file
            data=open(file2,"r")
            A=json.load(data)

        try:

            for i in A["data"]["usersByDevice"]:
                
                brand=i["brand"]
                count=i["count"]
                percentage=i["percentage"]
                dic2["Brands"].append(brand)
                dic2["Count"].append(count)
                dic2["Percentage"].append(percentage)
                dic2["State"].append(state)
                dic2["Year"].append(year)
                dic2["Quarter"].append(int(file.strip(".json")))

        except:
            pass


df_agg_user=pd.DataFrame(dic2)

loc3= "C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/data/map/transaction/hover/country/india/state/"

dic3={"State":[], "Year":[], "Quarter":[], "District":[], "Count":[], "Amount":[]}

map_trans_list=os.listdir(loc3)

for state in map_trans_list:
    st=loc3+state+"/"
    map_trans_state=os.listdir(st)

    for year in map_trans_state:
        yr=st+year+"/"
        map_trans_year=os.listdir(yr)

        for file in map_trans_year:
            file3=yr+file
            data=open(file3,"r")
            A=json.load(data)

            for i in A["data"]["hoverDataList"]:
                name=i["name"]
                count=i["metric"][0]["count"]
                amount=i["metric"][0]["amount"]
                dic3["District"].append(name)
                dic3["Count"].append(count)
                dic3["Amount"].append(amount)
                dic3["State"].append(state)
                dic3["Year"].append(year)
                dic3["Quarter"].append(int(file.strip(".json")))

df_map_trans=pd.DataFrame(dic3)


loc4= "C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/data/map/user/hover/country/india/state/"

dic4={"State":[], "Year":[], "Quarter":[], "District":[], "registeredUsers":[], "appOpens":[]}

map_user_list=os.listdir(loc4)

for state in map_user_list:
    st=loc4+state+"/"
    map_user_state=os.listdir(st)

    for year in map_user_state:
        yr=st+year+"/"
        map_user_year=os.listdir(yr)

        for file in map_user_year:
            file4=yr+file
            data=open(file4,"r")
            A=json.load(data)

            for i in A["data"]["hoverData"].items():
                name=i[0]
                reguser=i[1]["registeredUsers"]
                app=i[1]["appOpens"]
                dic4["District"].append(name)
                dic4["registeredUsers"].append(reguser)
                dic4["appOpens"].append(app)
                dic4["State"].append(state)
                dic4["Year"].append(year)
                dic4["Quarter"].append(int(file.strip(".json")))

df_map_user=pd.DataFrame(dic4)

loc5= "C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/data/top/transaction/country/india/state/"

dic5={"State":[], "Year":[], "Quarter":[], "Pincode":[], "Count":[], "Amount":[]}

top_trans_list=os.listdir(loc5)

for state in top_trans_list:
    st=loc5+state+"/"
    top_trans_state=os.listdir(st)

    for year in top_trans_state:
        yr=st+year+"/"
        top_trans_year=os.listdir(yr)

        for file in top_trans_year:
            file5=yr+file
            data=open(file5,"r")
            A=json.load(data)

            for i in A["data"]["pincodes"]:
                name=i["entityName"]
                count=i["metric"]["count"]
                amount=i["metric"]["amount"]
                dic5["Pincode"].append(name)
                dic5["Count"].append(count)
                dic5["Amount"].append(amount)
                dic5["State"].append(state)
                dic5["Year"].append(year)
                dic5["Quarter"].append(int(file.strip(".json")))

df_top_trans=pd.DataFrame(dic5)


loc6= "C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/data/top/user/country/india/state/"

dic6={"State":[], "Year":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

top_user_list=os.listdir(loc6)

for state in top_user_list:
    st=loc6+state+"/"
    top_user_state=os.listdir(st)

    for year in top_user_state:
        yr=st+year+"/"
        top_user_year=os.listdir(yr)

        for file in top_user_year:
            file5=yr+file
            data=open(file5,"r")
            A=json.load(data)

            for i in A["data"]["pincodes"]:
                name=i["name"]
                reguser=i["registeredUsers"]
                dic6["Pincodes"].append(name)
                dic6["RegisteredUser"].append(reguser)
                dic6["State"].append(state)
                dic6["Year"].append(year)
                dic6["Quarter"].append(int(file.strip(".json")))

df_top_user=pd.DataFrame(dic6)

print(df_top_user)

#converting from df to csv

df_agg_trans.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/agg_trans1.csv",index=False)
df_agg_user.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/agg_user1.csv",index=False)
df_map_trans.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/map_trans1.csv",index=False)
df_map_user.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/map_user1.csv",index=False)
df_top_trans.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/top_trans1.csv",index=False)
df_top_user.to_csv("C:/Users/lenovo/Desktop/DS/Phonepe/pulse-master/csv/top_user1.csv",index=False)


#connecting with database
mydb=sql.connect(host="localhost", user="root", password="1234", database="phonepe_pulse", auth_plugin='mysql_native_password')


mycursor=mydb.cursor()
mycursor.execute("create table agg_trans1(state varchar(100), Year int, Quarter int, Transaction_type varchar(100), Count int, Amount double)")

for i,row in df_agg_trans.iterrows():
    a="INSERT INTO agg_trans1 VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()


mycursor.execute("create table agg_users1(state varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")

for i,row in df_agg_user.iterrows():
    a="INSERT INTO agg_users1 VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()


mycursor.execute("create table map_trans1(state varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")

for i,row in df_map_trans.iterrows():
    a="INSERT INTO map_trans1 VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()

mycursor.execute("create table map_users1(state varchar(100), Year int, Quarter int, Districts varchar(100), RegisteredUsers int, AppOpens int)")

for i,row in df_map_user.iterrows():
    a="INSERT INTO map_users1 VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()

mycursor.execute("create table top_trans1(state varchar(100), Year int, Quarter int, Pincodes int, Count int, Amount double)")

for i,row in df_top_trans.iterrows():
    a="INSERT INTO top_trans1 VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()


mycursor.execute("create table top_users1(state varchar(100), Year int, Quarter int, Pincodes int, RegisteredUsers int)")

for i,row in df_top_user.iterrows():
    a="INSERT INTO top_users1 VALUES(%s,%s,%s,%s,%s)"
    mycursor.execute(a,tuple(row))
    mydb.commit()



