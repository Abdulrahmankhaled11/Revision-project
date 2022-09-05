''' 1_رساله ترحيبيه
    2_اختيار الالعاب 
    x exit
    3_ask to play again
    yes : reshow choises
    no: exit the game with bye message
    '''





class Game:

    def __init__(self):
        print('welcome')
        while True:
            print( '''\t1_ Even &odd nembers
        2_ Number of unbuplicate words in a sentence
        3_ Write from zero to the input number
        4_ Devisible numbers for the second number from zero to the first number
        5_ Devisible numbers from zero to 100 for two numbers
        x_ Exit
    ''')
            
            user_choise =input('enter your choise :')
            if user_choise =='1':
                   l =input('Enter a raw of numbers :')
                   numlist =map(int, l.split())
                   self.list_devider(numlist)
            elif user_choise =='2':
                sentence = input('enter your sentence :')
                self.unduplicate_num(sentence)
            elif user_choise =='3':
                end =int(input('enter your end number :'))
                self.from_zero_num(end)
            elif user_choise =='4':
                num1=int(input('enter the first number :'))
                num2=int(input('enter the second number :'))
                self.second_num_devisible(num1,num2)
            elif user_choise =='5':
                num1=int(input('enter the first number :'))
                num2=int(input('enter the second number :'))
                self.two_nums_devisible(num1,num2)
            elif user_choise =='x':
                print('goodbye.....')
                return
            print('''do you want to play again !
    -Yes
    -No''')
            agian_choise = input(':')
            if agian_choise=='No':
                print('goodbye.....')
                break

    #1
    def list_devider(self,num_list):
        l1=[]
        l2=[]
        for number in num_list:
            if number%2 ==0:
                l1.append(number)
            elif number%2 ==1:
                l2.append(number)

        print(f'even list :{l1}')
        print(f'odd list :{l2}')

    #2
    def unduplicate_num(self,sentence):
        non_duplicate =[]
        for word in sentence.split(' '):
            if word not in non_duplicate:
                non_duplicate.append(word)
        n=len(non_duplicate)
        print(f'number of words :{n}')

    #3
    def from_zero_num(self,end):
        for num in range(0,end+1):
            print(num)
        
    #4
    def second_num_devisible(self,n1,n2):
        devisible =[]
        if n2>n1:
            print('invalid input')
        else:
            for num in range(0,n1+1):
                if num%n2==0:
                    devisible.append(num)
                    
        print(f'devisible numbers for num2 :{devisible}')

    #5
    def two_nums_devisible(self,n1,n2):
        dev_n1 =[]
        dev_n2 =[]
        for num in range(0,101):
            if num%n1==0:
                dev_n1.append(num)
            elif num%n2==0:
                dev_n2.append(num)
        print(f'devisible numbers for first number :{dev_n1}')
        print(f'devisible numbers for second number :{dev_n2}')




    



u1 =Game()



    
