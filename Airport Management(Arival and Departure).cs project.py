# Computer Science Project "Airport Management(Arival and Departure)"

import mysql.connector

print("\t\t\t\tAirport Mangement")

print()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("\t1. Add details.\n\t2. View detail.\n\t3. Search details.\n\t4. Modify details.\n\t5. Delete details.\n\t6. Exit.")
        print('\n')
        cho=int(input("Enter the corresponding number among the given operation(1 to 6) : "))
        print()
        if cho==1:
            add_details()
        elif cho==2:
            view_details()
        elif cho==3:
            search_details()
        elif cho==4:
            modify_details()
        elif cho==5:
            delete_details()
        elif cho==6:
            print("\n\t\t\t\t    Thank you\n\t\t\t\t         *****")
            break
        else:
            print("*You made a wrong chose try it again*\n")


def add_details():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="AMS")
    cursor=db.cursor()
    command="insert into airport_management (A_line,F_name,Date,F_place,T_place,D_time,A_time) values(%s,%s,%s,%s,%s,%s,%s)"
    print()
    A_line=input("Enter the Airline Name : ")
    F_name=input("Enter Flight Name : ")
    Date=input("Enter the Date (YYYY-MM-DD): ")
    F_place=input("Enter From (Place) : ")
    T_place=input("Enter To (Place) : ")
    D_time=input("Enter the Departure Time : ")
    A_time=input("Enter the Arrival Time : ")
    values=(A_line,F_name,Date,F_place,T_place,D_time,A_time)
    cursor.execute(command,values)
    db.commit()
    print()
    print(cursor.rowcount,"row successfully inserted\n")
    db.close()


def view_details():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="AMS")
    cursor=db.cursor()
    cursor.execute("Select * from airport_management")
    result=cursor.fetchall()
    print()
    print('S No.\tAirline Name \tFlight Name\tDate\t\t From\t\t\tTo\t\tDeparture Time\tArrival Time\t\n\n')
    for a in result:
        print(a[0],'\t',a[1],'\t',a[2],'\t\t',a[3],'\t',a[4],'\t\t',a[5],'       \t',a[6],'\t\t',a[7],'\n')
    db.close()


def search_details():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="AMS")
    cursor=db.cursor()
    print("\nSearch details in either ways :\n\n\ta. Flight Name\n\tb. Destination & Date\n")
    while True:
        sel=input("Enter your choice for searching details(a or b) : ")
        print()
        if sel=="a":
            command="select * from airport_management where Flight_name=%s"
            F_Name=input("Enter Flight Name : ")
            val=(F_Name,)
            cursor.execute("select F_name from airport_management")
            result1=cursor.fetchall()
            if val in result1:
                cursor.execute(command,val)
                result2=cursor.fetchall()
                print('\n')
                print('Airline Name\t','Flight Name\t','Date\t\t','From\t\t','To\t\t','Departure Time\t','Arrival Time\t\n\n')
                for a in result2:
                    print(a[1],'\t\t',a[2],'\t\t',a[3],'\t',a[4],'\t\t',a[5],'\t\t',a[6],'\t\t',a[7])
                    print()
            else:
                print("\n\nThere is no Flight named ",F_Name,'\n')
            break
        elif sel=='b':
            des=input("Enter your Destination : ")
            print()
            date=input("Enter the Date (YYYY-MM-DD,Optional): ")
            print('\n')
            if date=="":
                command="select * from airport_management where To_place=%s"
                val=(des,)
                cursor.execute("select To_place from airport_management")
                result1=cursor.fetchall()
                if val in result1:
                    cursor.execute(command,val)
                    result2=cursor.fetchall()
                    print('Airline Name\t','Flight Name\t','Date\t\t','From\t\t','To\t\t','Departure Time\t','Arrival Time\t\n\n')
                    for a in result2:
                        print(a[1],'\t\t',a[2],'\t\t',a[3],'\t',a[4],'\t\t',a[5],'\t\t',a[6],'\t\t',a[7],'\n')
                else:
                    print("Sorry!! No flights to ",des,'\n')
                break
            else:
                command="select * from airport_management where T_place=%s and Date=%s"
                val=(des,date)
                cursor.execute("select To_place from airport_management")
                result1=cursor.fetchall()
                cursor.execute("select date from airport_management")
                result2=cursor.fetchall()
                if ((des,) in result1) and ((date,) in result2):
                    cursor.execute(command,val)
                    result3=cursor.fetchall()
                    print('Airline Name\t','Flight Name\t','Date\t\t','From\t\t','To\t\t','Departure Time\t','Arrival Time\t\n\n')
                    for a in result3:
                        print(a[1],'\t\t',a[2],'\t\t',a[3],'\t',a[4],'\t\t',a[5],'\t\t',a[6],'\t\t',a[7],'\n\n')
                else:
                    cursor.execute("select T_place from airport_management")
                    result3=cursor.fetchall()
                    cursor.execute("select Date from airport_management")
                    result4=cursor.fetchall()
                    if (des,) not in result3:
                        print("Sorry!! No flights to ",des)
                    elif (date,) not in result4:
                        print("Sorry!! No flights on",date," to ",des)
                    print()
                break
        else:
            print("*Entered option is invalid try again*\n\n")
    db.close()


def modify_details():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="AMS")
    cursor=db.cursor()
    print("\nFor modifing data :")
    print("\n\t1. Airline.\n\t2. Flight Name.\n\t3. Date.\n\t4. From.\n\t5. To.\n\t6. Departure Time.\n\t7. Arrival Time")
    print()
    dic={1:'Airline_name',2:'Flight_name',3:'date',4:'From_place',5:'To_place',6:'Departure_time',7:'Arrival_time'}
    while True:
        cho=int(input("Enter the corresponding number to modify data(1-7) : "))
        print()
        if cho >=1 and cho<=7:
            S_no=int(input("Enter the serial number at which row you have to change the value : "))
            print()
            old_data=input("Enter the Data that to be modified : ")
            print()
            new_data=input("Enter the new Data to be inserted : ")
            if cho==1:
                command="update airport_management set A_line=%s where S_no=%s and A_line=%s"
            elif cho==2:
                command="update airport_management set F_name=%s where S_no=%s and F_name=%s"
            elif cho==3:
                command="update airport_management set Date=%s where S_no=%s and Date=%s"
            elif cho==4:
                command="update airport_management set F_place=%s where S_no=%s and F_place=%s"
            elif cho==5:
                command="update airport_management set T_place=%s where S_no=%s and T_place=%s"
            elif cho==6:
                command="update airport_management set D_time=%s where S_no=%s and D_time=%s"
            elif cho==7:
                command="update airport_management set A_time=%s where S_no=%s and A_time=%s"
            values=(new_data,S_no,old_data)
            cursor.execute(command,values)
            print()
            print(cursor.rowcount , " row modified\n")
            db.commit()
            break
        else:
            print("*Entered option is invalid try again*\n\n")
    db.close()


def delete_details():
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="AMS")
    cursor=db.cursor()
    print()
    S_no=int(input("Enter the serial number of row which have to be deleted : "))
    command1="delete from airport_management where S_no=%s"
    value1=(S_no,)
    cursor.execute(command1,value1)
    print()
    print(cursor.rowcount , " row deleted\n")
    db.commit()
    cursor.execute("select S_no from airport_management")
    result=cursor.fetchall()
    print()
    while (S_no,)<=max(result):
        S_no+=1
        new_S=S_no-1
        command2="update airport_management set S_no=%s where S_no=%s"
        value2=(new_S,S_no)
        cursor.execute(command2,value2)
        db.commit()
    db.close()



main_menu()



