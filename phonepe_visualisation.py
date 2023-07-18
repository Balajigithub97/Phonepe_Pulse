import streamlit as st
import pandas as pd
import json
import csv
import mysql.connector as sql
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px

img=Image.open("C:/Users/Lenovo/Desktop/DS/Phonepe/pulse-master/phonepe.png")

st.set_page_config( page_title="Phonepe pulse Data Visvalization - By M.Balaji", page_icon=img,layout="wide",initial_sidebar_state="expanded", menu_items={"About": """# This dashboard app is crated by M.Balaji"""})

st.sidebar.header(":violet[Phonepe Pulse]")

mydb=sql.connect(host="localhost",user="root", password="1234", database="phonepe_pulse")

mycursor=mydb.cursor(buffered=True)

#sidebar option menu
with st.sidebar:
    Select=option_menu("Menu",["Home", "Top 10 Transactions/Users", "Explore Data", "About"],icons=["house","graph-up-arrow","bar-chart-line","exclamation-circle"],menu_icon="menu-button-wide",default_index=0,styles={"nav-link":{"font-size":"20px","text-align":"left","margin":"-2px","--hover-color":"#6739B7"},"nav-link-selected":{"background-color":"#6739B7"}})

if Select=="Home":
    image1=Image.open("C:/Users/Lenovo/Desktop/DS/Phonepe/pulse-master/phonepe.png")
    im=image1.resize((50,35))
    col1,col2=st.columns([1,15])
    with col1:
        a=st.image(im)
    with col2:
        st.markdown("### :violet[Phonepe Data Visualization and Exploration]")
    st.markdown("## :violet[A User-Friendly Tool using streamlit and plotly]")
    c1,c2=st.columns([3,2],gap="medium")
    with c1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[Domain:] Fintech")
        st.markdown("### :violet[Technologies used:] Github Cloning, Pandas, Streamlit, MySQL, Python, Ploty, mysql-connector-python")
        st.markdown("### :violet[Overview:] In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.")
    with c2:
        image2=Image.open("C:/Users/Lenovo/Desktop/DS/Phonepe/pulse-master/phonepe pulse.jpg")
        st.image(image2)

if Select=="Top 10 Transactions/Users":
    st.markdown("## :violet[Top 10 Transactions/Users]")
    Type=st.selectbox("**Type**",("Transaction","User"))
    col1,col2,col3=st.columns([1,1,1], gap="small")
       
    if Type == "Transaction":
        with col1:
            A=st.selectbox("**Select the type**",("State","District","Pincode"))    

        with col2:
            Year=st.selectbox("**Select the Year**",(2018,2019,2020,2021,2022))

        with col3:
            Quarter=st.selectbox("**Select the Quarter**",(1,2,3,4))

        if A == "State":

            st.markdown("### :violet[State]")
            mycursor.execute(f"select state, sum(Count) as Total_Transactions_Count, sum(Amount) as Total from agg_trans1 where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(),columns=["State", "Transactions_Count", "Total_Amount"], )
            fig = px.pie( df, values="Total_Amount", names="State",title="State Wise Top 10 Transaction",color_discrete_sequence=px.colors.sequential.Agsunset,hover_data=["Transactions_Count"],labels={"Transactions_Count": "Transactions_Count"},)
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig, use_container_width=True)

        if A == "District":
            st.markdown("### :violet[District]")
            mycursor.execute(f"select District, sum(Count) as Total_Transaction_count, sum(Amount) as Total from map_trans1 where year={Year} and quarter={Quarter} group by District order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(),columns=["District", "Transactions_Count", "Total_Amount"], )
            fig = px.pie( df, values="Total_Amount", names="District",title="District Wise Top 10 Transaction",color_discrete_sequence=px.colors.sequential.Agsunset,hover_data=["Transactions_Count"],labels={"Transactions_Count": "Transactions_Count"},)
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig, use_container_width=True)

        elif A == "Pincode":    
            st.markdown("### :violet[Pincodes]")
            mycursor.execute(f"select Pincodes, sum(Count) as Total_Transaction_count, sum(Amount) as Total from top_trans1 where year={Year} and quarter={Quarter} group by Pincodes order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(),columns=["Pincodes", "Transactions_Count", "Total_Amount"], )
            fig = px.pie( df, values="Total_Amount", names="Pincodes",title="Pincode Wise Top 10 Transaction",color_discrete_sequence=px.colors.sequential.Agsunset,hover_data=["Transactions_Count"],labels={"Transactions_Count": "Transactions_Count"},)
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig, use_container_width=True)

    if Type == "User":
        st.markdown('## :violet Top 10 Users')
        col1,col2,col3=st.columns([1,1,1],gap="small")
        with col1:
            A=st.selectbox("**Select the type**",("Brand","State","District","Pincode"))
        with col2:
            B=st.selectbox("**Select the Year**",(2018,2019,2020,2021,2022))
        with col3:
            C=st.selectbox("**Select the Quarter**",(1,2,3,4))

        if A=="Brand":

            if B==2022 or (C==1 or C==2 or C==3):
                st.write("No Data Available for the selected timeperiod")

            else:
                st.markdown("## :violet[Brand]")
                mycursor.execute(f"select  Brands, sum(Count) as Total_users, sum(Percentage) as Percentage from agg_users1 where year={B} and quarter={C} group by Brands order by Total_Users desc limit 10")
                df=pd.DataFrame(mycursor.fetchall(),columns=["Brands","Total_Users","Total_Percentage"])
                fig=px.bar(df,title="Top 10 Brands",x="Total_Users",y="Brands",orientation='h',color="Total_Percentage",color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)

        if A=="District":

            if B==2022 or (C==1 or C==2 or C==3):
                st.write("No Data Available for the selected timeperiod")

            else:
                st.markdown("## :violet[District]")
                mycursor.execute(f"select Districts,sum(RegisteredUsers) as RegisteredUsers, sum(AppOpens) as AppOpens from map_users1 where year={B} and quarter={C} group by Districts order by RegisteredUsers desc limit 10")
                df=pd.DataFrame(mycursor.fetchall(),columns=["Districts","RegisteredUsers","AppOpens"])
                df.RegisteredUsers=df.RegisteredUsers.astype(float)
                fig=px.bar(df,title="Top 10 RegisteredUsers",x="RegisteredUsers",y="Districts",orientation="h",color="RegisteredUsers",color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)

        if A=="State":
            if B==2022 or (C==1 or C==2 or C==3):
                st.write("No avaliable data for the selected timeperiod")
            
            else:
                st.markdown("## :violet[State]")
                mycursor.execute(f"select State,sum(RegisteredUsers) as RegisteredUsers, sum(AppOpens) as AppOpens from map_users1 where year={B} and quarter={C} group by State order by RegisteredUsers desc limit 10")
                df=pd.DataFrame(mycursor.fetchall(),columns=["State","RegisteredUsers","AppOpens"])
                df.RegisteredUsers=df.RegisteredUsers.astype(float)
                fig=px.bar(df,title="Top 10 RegisteredUsers",x="RegisteredUsers",y="State",orientation="h",color="RegisteredUsers",color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)

        if A=="Pincode":
            if B==2022 or (C==1 or C==2 or C==3):
                st.write("No data available on the selected timeperiod")

            else:
                st.markdown("## :violet[Pincode]")
                mycursor.execute(f"select Pincodes,sum(RegisteredUsers) as RegisteredUsers from top_users1 where year={B} and quarter={C} group by Pincodes order by RegisteredUsers desc limit 10")
                df=pd.DataFrame(mycursor.fetchall(),columns=["Pincodes","RegisteredUsers"])
                df.RegisteredUsers=df.RegisteredUsers.astype(float)
                fig=px.pie(df,title="Top 10 RegisteredUsers",values="RegisteredUsers",names="Pincodes",hover_data=["RegisteredUsers"],color_discrete_sequences=px.colors.sequential.Agsunset)
                fig.update_traces(textposition="inside", textinfo="percent+label")
                st.plotly_chart(fig,use_container_width=True)


if Select=="Explore Data":
    Type=st.selectbox("**Select the type**",("Transaction","User"))
    if Type=="User":
        col1,col2=st.columns([1,1],gap="medium")
        with col1:
            A=st.selectbox("**Select the year**",(2018,2019,2020,2021,2022))
        with col2:
            B=st.selectbox("**Select the Quarter**",(1,2,3,4))

        mycursor.execute(f"select sum(RegisteredUsers) as RegisteredUsers from map_users1 where year={A} and quarter={B}")
    
        st.markdown(f"### :violet[Total RegisteredUsers for the year {A}, quarter {B} is] {mycursor.fetchall()}")

        c1,c2=st.columns([1,1],gap="small")
        with c1:
            mycursor.execute(f"select Year, sum(RegisteredUsers) as RegisteredUsers from map_users1 group by Year")
            df=pd.DataFrame(mycursor.fetchall(),columns=["Year","RegisteredUsers"])
            fig=px.bar(df,title="RegisteredUsers from 2018-2022",y="RegisteredUsers", x="Year", orientation="v")
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            mycursor.execute(f"select Year, sum(AppOpens) as AppOpens from map_users1 group by Year")
            df=pd.DataFrame(mycursor.fetchall(),columns=["Year","AppOpens"])
            fig=px.bar(df,title="AppOpens from 2018-2022",y="AppOpens", x="Year", orientation="v")
            st.plotly_chart(fig,use_container_width=True)


    if Type=="Transaction":
        col1,col2=st.columns([1,1],gap="medium")
        with col1:
            A=st.selectbox("**Select the year**",(2018,2019,2020,2021,2022))
        with col2:
            B=st.selectbox("**Select the Quarter**",(1,2,3,4))

        mycursor.execute(f"select sum(Count) as Count from agg_trans1 where year={A} and quarter={B}")
        C=mycursor.fetchall()
    
        for i in C:
            st.markdown(f"### :violet[Total Transaction for the year {A}, quarter {B} is] {i[0]}")

        st.markdown("## Category wise Transactions")

        mycursor.execute(f"select Transaction_type, sum(Count) as Count, sum(Amount) as Amount from agg_trans1 where year={A} and quarter={B} group by Transaction_type order by Amount")
        D=mycursor.fetchall()

        for i in D:
            colu1,colu2=st.columns([4,3],gap="medium")
            with colu1:
                st.markdown(f"### :violet[{i[0]}]")
            with colu2:
                st.markdown(f"### {i[1]}")


if Select=="About":
    st.markdown("## :violet[About the project]")
    st.markdown("## Step1: Cloned the phonepe pulse data from git respirotory")
    st.markdown("## Step2: After that analysed the data and transformed the data from Json to Data Frame")
    st.markdown("## Step3: After that stored the datas into MYSQL DataBase")
    st.markdown("## Step4: Then Created a Streamlit app and extrated the datas from MYSQL Database")
    st.markdown("## Step5: Completed the analysis using streamlit and ploty")









            
    
        