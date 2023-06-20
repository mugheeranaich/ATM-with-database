import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="atm"
        )
cursor = conn.cursor()

while True:
    print("1:Register\n2:Login\n3:Quit")
    user_choice =int(input("Enter your choice: "))
    print("="*30)

    if user_choice == 3:
        print("By By !!")
        break
    elif user_choice == 1:
        print("Welcome for registration!! ")
        my_name = input("Enter your name: ")
        user_name = input("Enter user name: ")
        password = input("Enter your password: ")

        cursor.execute("SELECT username, password FROM users")
        myresult = cursor.fetchall()

        for i in myresult:
            x =list(i)
            if user_name == x[0]:
                print("already user avalible\n try anothrer user name")
                exit()

        query = "INSERT INTO users (name, username, password, amount) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (my_name, user_name,password,"0"))
        conn.commit()
        print("Registeration succesful!!")

    elif user_choice == 2:
        print("welcome for login!!")
        username = input("Enter your user name: ")
        pin = input("Enter your password: ")
        cursor.execute("SELECT username, password FROM users")
        myresult = cursor.fetchall()
        for i in myresult:
            x =list(i)
            if username == x[0] and pin  == x[1]:
                while True:
                    print("="*30)
                    print(f"Welcome {username}!!")
                    print("1:Deposit\n2:Withdrawal\n3:Check balance\n4:Transfer Money\n5Logout")
                    user_input = int(input("Enter your choice: "))
                    if user_input ==5:
                        print("logout succesful!!")
                        quit()
                    elif user_input == 1:
                        amount =int(input("Enter the amount to deposit: "))
                        if amount > 0:
                            cursor.execute("SELECT username, password, amount FROM users")
                            myresult = cursor.fetchall()
                            for i in myresult:
                                x =list(i)
                                if username == x[0] and pin == x[1]:
                                    amount1 = amount + i[2]

                                    query = "UPDATE users SET amount=%s WHERE username=%s"
                                    cursor.execute(query, (amount1, username))
                                    conn.commit()
                                    print("amount deposit succesful !!")
                        elif  amount < 0:
                            print("Invalid amount")

                    elif user_input == 2:
                        withdrawal = int(input("Enter the amount to withdrawal: "))
                        cursor.execute("SELECT username,amount FROM users")
                        myresult = cursor.fetchall()
                        if withdrawal >0:
                            for i in myresult:
                                x =list(i)

                                if username == x[0] and withdrawal <= x[1]:
                                    amount2 = i[1] - withdrawal
                                    query = "UPDATE users SET amount=%s WHERE username=%s"
                                    cursor.execute(query, (amount2, username))
                                    conn.commit()
                                    print("Amount withdrawal succesful!!")
                                elif username == x[0]:
                                    print("Low account balance")
                        elif   withdrawal < 0:
                            print("Invalid amount")

                    elif user_input == 3:
                        cursor.execute("SELECT username, password, amount FROM users")
                        myresult = cursor.fetchall()
                        for i in myresult:
                            x =list(i)
                            if username == x[0] and pin == x[1]:
                                print(f"your account balance is: {x[2]}")
                    elif user_input == 4:
                        recipient =  input("Enter the recipient username: ")
                        cursor.execute("SELECT username,amount FROM users")
                        myresult = cursor.fetchall()
                        for i in myresult:
                            x =list(i)
                            # if username == x[0]:
                            if recipient == x[0] and recipient != username:
                                money = int(input("Enter the money that you want to  send: "))
                                if money > 0:
                                    for j in myresult:
                                        if username == j[0]:
                                            for amount in myresult:
                                                if amount[0] == username:
                                                    if money <= amount[1]:
                                                        amount3 = amount[1] - money
                                                        query = "UPDATE users SET amount=%s WHERE username=%s"
                                                        cursor.execute(query, (amount3, username))
                                                        conn.commit()

                                                        for b in myresult:
                                                            if recipient == b[0]:
                                                                for a in myresult:
                                                                    if a[0] == recipient:
                                                                        amount4 = a[1] + money
                                                                        query = "UPDATE users SET amount=%s WHERE username=%s"
                                                                        cursor.execute(query, (amount4, recipient))
                                                                        conn.commit()

                                                                        print("Amount transfer succesful!!")

                                                    elif username ==amount[0]:
                                                        print("Low account balance")
                                    break

                                elif username !=x[0]:
                                    print("Invalid amount")

                            elif recipient == username:
                                print("Recipient user name could't be  same to your user name")
                                break






        print("No user avalible Register first\nOR\nWrong password")
        print("="*30)
