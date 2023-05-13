import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("-l","--list",type=str,help="Enter elements, separated by commas.",default="1,2,3,4,5,6,7,8,9,10")
parser.add_argument("-a","--amount",type=int,help="Enter the amount of elements to be randomly picked.",default=1)

def ListCutter(elements):
    try:
        new_list = elements.split(",")
    except:
        new_list = ["1","2","3","4","5","6","7","8","9","10"]
    return new_list

def RandomPicker(elements,amount):
    try:
        a = len(elements)
        q = []
        if(amount <=a):
            q = random.sample(range(a),amount)  
        else:
            q.append("error")
    except:
        q = []        
    return q

def Export(elements,result):
    c = 0
    if(result[0]=="error"):
        print("[ERROR] : The amount of elements to be randomly picked can't be higher than the elements entered.")
    else:
        if(len(result)==1):
            print("I picked this option for you!")
            print("<===========================>\n")
        else:
            print("I picked these options for you!")
            print("<===========================>\n")
        for i in range(len(result)):
            c+=1
            print(str(c)+". "+elements[result[i]])
        print()
        print("<===========================>\n")
args = parser.parse_args()

#print(args)


listaCortada = ListCutter(args.list)
rp = RandomPicker(listaCortada,args.amount)
#print(listaCortada)
#print(rp)
Export(listaCortada,rp)