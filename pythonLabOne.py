def coffeeshop():

        receipt = " "
        name = input("Welcome to our virtual coffee shop! What is your name?\n")
        order = input("What kind of drink would you like?\n")
        receipt =( name+" orders "+order+".   Their order number is 69")
        return receipt

def  Palindrome(s):
        
        pali= True
        
        for i in range(len(s)):
                if  ( s[i] == s[len(s)-i-1:len(s)-i]):
                        pali= True
                else:
                        return False
        return pali 
                
        

def  main():
        
        print (coffeeshop())
        strr= input("enter strings")
        print(Palindrome(strr))
        
    


if __name__ == "__main__":
        main()
