import os
import shutil
import json

##Global val
LoginUser = dict()
ProductInfo = list()
CartInfo = list()

#json file Dir string
customerDir = "./data/Customer.json"
productDir = "./data/pdata.json"
def cartDirbyUser(uid):
    return f"./data/cart/{uid}.json"

def init():
    if len(LoginUser) > 0: ##already login
        orderFunc(showOrder())
    else: ## not login
        print(">>welcome to OrderApp<<")
        i = prompt("1. Login\n2.Register\n>>")

        os.system('clear') ## refresh screen

        if i == "1": ##login > orderlist
            if login():
                orderFunc(showOrder())

        elif i == "2": ##register > login > orderlist
            register() 
            if login():
                orderFunc(showOrder())

def orderFunc(o):
    if(o == "1"):
        # selet and add to cart
        promptSelectProduct()
    elif(o == "2"):
        # show customer's cart
        goToCart()
    elif(o == "3"):
        # show customerInfo & balance
        showUserInfo()

def prompt(val): ## press q exit()
    i = input(val)
    if(i.upper() =='Q'):
        exit()
    return i

def register():
    user = {}
    userArr = readFile(customerDir)
    lastIdx = len(userArr) -1

    if(len(userArr) > 0):
        id = int(userArr[lastIdx]["id"]) + 1
    else:
        id = 1001
    if id > 9999:
        print("we can't accept user anymore!")
        exit()

    print(id)
    name = prompt("name:")
    address = prompt("address:")
    email = existEmail4R(userArr) ## if email exist get again else get input value

    user ={
        "id" : id,
        "name" : name,
        "email" : email,
        "address" : address,
        "balance" : 1000
    }

    appendFile(customerDir, user, True if len(userArr) > 0 else False)
    os.system('clear')

def existEmail4R(userArr):
    email = prompt("email:")
    for e in userArr:
        if email == e['email']:
            print("Already Exist Email. Try again")
            existEmail4R(userArr)
    return email

def login():
    email = prompt("What's your email?")
    userArr = readFile(customerDir)
    return isEmailExist4Login(userArr, email)


def isEmailExist4Login(userArr, email):
    for user in userArr:
        if user["email"] == email:
            LoginUser.update(user)
            print("success")
            return True

    # if email not exist
    if(len(LoginUser) == 0):
        print("fail")
        return False

def showOrder():
    os.system('clear')
    productList = readFile(productDir)
    ProductInfo.clear()
    ProductInfo.extend(productList)

    print("======================================================================")
    print("Product List")
    print("======================================================================")
    for product in ProductInfo:
        print(f"code:{product['pid']:<5}   name:{product['pname']:<35}     price:{product['price']}")
    print("======================================================================")
    print("1. Select Product")
    print("2. Go to Shopping Cart")
    print("3. User Info")
    return prompt(">>")
    
def promptSelectProduct():
    print("----------------------------------------------------------------------")
    if os.path.exists(cartDirbyUser(LoginUser['id'])):
        CartInfo.extend(readFile(cartDirbyUser(LoginUser['id'])))
        print(CartInfo)

    selectProduct()

def selectProduct(): 
    pid = prompt("Type the code of product: ")
    amount = prompt("Type amount of product: ")
    isExist = False
    for product in ProductInfo:
        if product["pid"] == int(pid):
            u = dict()
            u.update({"uid": LoginUser['id']})
            u.update(product)
            u.update({"amount" : int(amount)})
            CartInfo.append(u)
            isExist = True
            break

    if not isExist:
        print("This product does not exist")
    else:
        yn = prompt("Do you want to add more product in your cart? (Y/N): ")

        if yn.upper() == "Y":
            selectProduct()
        else:
            writeFile(cartDirbyUser(LoginUser['id']), CartInfo)
            goToCart()

def goToCart():
    os.system('clear')
    print("======================================================================")
    print("Shopping Cart")
    print("======================================================================\n")
    cartList =  readFile(cartDirbyUser(LoginUser['id']))
    if not cartList:
        print("cart is empty")
        input("Press U if you want to back!")
    else:
        totalPrice = 0
    
        for product in cartList:
            print(f"{product['pname']} price:{product['price']} amount:{product['amount']} total:{product['price'] * product['amount']:.2f}\n")
            print("----------------------------------------------------------------------\n")
            totalPrice += product['price'] * product['amount']
        print(f"Total Price: {totalPrice:>.2f}, User Balance: {LoginUser['balance']}")
        p = prompt("1. Order\nPress U if you want to back!\n>>")
    
        if p == "1":
            order(totalPrice)
        elif p.upper() == "U":
            orderFunc(showOrder())

def order(totalPrice):
    if totalPrice <= LoginUser["balance"]:
        LoginUser["balance"] -= totalPrice
        userList = readFile(customerDir)

        for user in userList:
            if user['id'] == LoginUser["id"]:
                user['balance'] = LoginUser['balance']
                break
        writeFile(customerDir,userList)
        os.remove(cartDirbyUser(LoginUser['id']))
        CartInfo.clear() ## reset cart
        print(f"Remain User balance: {LoginUser['balance']}")
        input("Press U if you want to back!")
    else:
        print("Balance is not enough")
        input("Press U if you want to back!")



def showUserInfo():
    os.system('clear')
    print(f"name: {LoginUser['name']}\nemail: {LoginUser['email']}\naddress: {LoginUser['address']}\nbalance:{LoginUser['balance']}")
    if prompt("Press U if you want to back!\n>>").upper() == "U":
        orderFunc(showOrder())


def readFile(dir):
    if os.path.exists(dir):
        file = open( dir , "r")
        list = json.loads(file.read())
        file.close()
        return list
    else:
        return False

def writeFile(dir, content):
    file = open( dir , "w")
    file.write(json.dumps(content))
    file.close()
    return list

def appendFile(dir, content, isExist):
    file = open( dir , "a+")
    file.seek(file.tell() -1)
    file.truncate()
    if(isExist):
        file.write(","+json.dumps(content))
    else:
        file.write(json.dumps(content))
    file.write("]") 
    file.close()

while(1):
    init()