import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card(
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
            )""")
conn.commit()


def in_menu():
    while True:
        print('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
        ''')

        instr = input()
        if instr == '1':
            cur.execute(
                f"SELECT balance FROM card WHERE number = '{card_number}'")
            print(cur.fetchone())
        if instr == '2':
            print('Enter income: ')
            income = input()
            cur.execute(
                f"update card set balance = balance + '{income}' where number = '{card_number}';")
            print('Income was added!')
            conn.commit()
        if instr == '3':
            print("Transfer\nEnter card number:")
            aa_number = input()
            a_number = []
            for index in range(len(aa_number)):
                a_number.append(int(aa_number[index]))
            for index in range(0, len(a_number), 2):
                a_number[index] = int(a_number[index]) * 2
                if a_number[index] > 9:
                    a_number[index] -= 9
            qq = ((int(a_number[0]) + int(a_number[1]) + int(a_number[2]) + int(a_number[3]) + int(a_number[4]) + int(a_number[5]) + int(a_number[6]) + int(
                a_number[7]) + int(a_number[8]) + int(a_number[9]) + int(a_number[10]) + int(a_number[11]) + int(a_number[12]) + int(a_number[13]) + int(a_number[14])) % 10)
            if qq % 10 != 0:
                check_digit = 10 - qq
            else:
                check_digit = 0
            if check_digit != a_number[15]:
                print('Probably you made mistake in card number. Please try again!')
                cur.execute(
                    f"SELECT number FROM card WHERE number = '{card_number}'")
            elif cur.fetchone() is None:
                sum = input("Enter how much money you want to transfer: ")
                cur.execute(
                    f"SELECT balance FROM card WHERE number = '{card_number}'")
                num = cur.fetchone()
                if int(num[0]) > int(sum):
                    cur.execute(
                        f"update card set balance = balance - {sum} where number = '{card_number}';")
                    conn.commit()
                    cur.execute(
                        f"update card set balance = balance + {sum} where number = '{aa_number}';")
                    conn.commit()
                    print('Success!')
                else:
                    print("Not enough money!")
            else:
                print("Such a card does not exist.")
        if instr == '4':
            cur.execute(f"delete from card where number = '{card_number}';")
            conn.commit()
        if instr == '5':
            break
        if instr == '0':
            exit()


class Card:
    card_pull = []
    pin_pull = []

    def new_card(self):
        ran_num = [4, 0, 0, 0, 0, 0]
        ran_num.append(random.randint(1, 9))
        check = 0
        while check < 8:
            check += 1
            ran_num.append(random.randint(0, 9))
        str_ran_num = ''.join(str(i) for i in ran_num)
        for index in range(0, len(ran_num), 2):
            ran_num[index] = ran_num[index] * 2
            if ran_num[index] > 9:
                ran_num[index] -= 9
        qq = ((int(ran_num[0]) + int(ran_num[1]) + int(ran_num[2]) + int(ran_num[3]) + int(ran_num[4]) + int(ran_num[5]) + int(ran_num[6]) + int(
            ran_num[7]) + int(ran_num[8]) + int(ran_num[9]) + int(ran_num[10]) + int(ran_num[11]) + int(ran_num[12]) + int(ran_num[13]) + int(ran_num[14])) % 10)
        if qq % 10 != 0:
            check_digit = 10 - qq
        else:
            check_digit = 0

        card_number = f'{str_ran_num}{check_digit}'
        PIN = random.randint(1000, 9999)

        print(f'\nYour card number:\n{card_number}')
        print(f'Your card PIN:\n{PIN}')
        cur.execute("INSERT INTO card(number, pin) VALUES(?, ?);",
                    (card_number, PIN))
        conn.commit()

    def login(self, card_number, PIN):
        error = 0
        cur.execute(f"SELECT number FROM card WHERE number = '{card_number}'")
        if cur.fetchone() is None:
            error += 1
        cur.execute(f"SELECT pin FROM card WHERE pin = '{PIN}'")
        if cur.fetchone() is None:
            error += 1
        if error == 0:
            print('You have successfully logged in!\n')
            in_menu()
        else:
            print('Wrong card number or PIN!')


while True:
    print('''
1. Create an account
2. Log into account
0. Exit''')

    instruction = input()
    if instruction == '1':
        card1 = Card()
        card1.new_card()

    if instruction == '2':
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        PIN = input()
        card1 = Card()
        card1.login(card_number, PIN)

    if instruction == '0':
        exit()
