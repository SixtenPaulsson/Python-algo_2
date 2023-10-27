import time
import math
# seed the pseudorandom number generator
from random import seed
from random import random
from random import randint

class data:
    
    def create_list(length):
        list=[]
        for i in range (length):
            list.append((i))
        return list
    
    def string_list(list):       
        
        text=""
        for i in range (len(list)):
            text+=(str(list[i])+", ")
            
        return text

    def checkList(lista):

        for i in range (len(lista)-1):
            if(lista[i]>lista[i+1]):
                return False
        return True


    def sequence_search(list,search_value):
        start = time.perf_counter()
        for i in range (len(list)):
            if(list[i]==search_value):
                end = time.perf_counter()
                print("The time of execution of above program is :",
                (end-start) * 10**3, "ms")
                return i
        end = time.perf_counter()
        print("The time of execution of above program is :",
        (end-start) ,"sek")
        return -1
        
    
    def binary_search(list,search_value):
        start = time.perf_counter()
        if(data.checkList(list)==False):
            list=data.quicksort(list)
            #list=data.bubbleSort(list)
            #list=data.insertion_sort(list)
            
        lowest_index, highest_index=0,len(list)-1
        
        while(lowest_index<=highest_index):
            
            current_index=((lowest_index+highest_index)//2)
            
            
            if(list[current_index]==search_value):
                end = time.perf_counter()
                print("The time of execution of above program is :",
                (end-start) ,"sek")
                return current_index
            elif(list[current_index]<search_value):
                lowest_index=current_index+1
            else:
                highest_index=current_index-1
        end = time.perf_counter()
        print("The time of execution of above program is :",
        (end-start),"sek")  
        return -1
    

            
    def bubbleSort(lista):
        while True:
            for i in range (len(lista)-1):
                if(lista[i]>lista[i+1]):
                    x=lista[i]
                    lista[i]=lista[i+1]
                    lista[i+1]=x
            if(data.checkList(lista[:])):
                return lista[:]
    
    def insertion_sort(lista):
        #Går igenom processen ett vist antal gånger
        for i in range (len(lista)):      
            if(data.checkList==True):
                return lista
            for x in range (len(lista)-1):
                if(lista[x]>lista[x+1]):
                    for y in range(x+1):
                        if(lista[x+1]<lista[x-y]):
                            o=lista[x-y]
                            lista[x-y]=lista[x+1]
                            lista[x+1]=o
                        else:
                            break
                        
                            
                    
        return lista

    def quicksort(lista):
        if(len(lista)<=1):
            return lista
        
        left=[]
        right=[] 
        
        for i in range(len(lista)):
            
            if(lista[i]>lista[0]):
               right.append(lista[i])
               
            elif(lista[i]<lista[0]):
                left.append(lista[i])

        return data.quicksort(left) + [lista[0]] + data.quicksort(right)
            

    def quicksort_v_2(lista,start,end):
        if(end-start<=1):
            return lista
        
        
        max=end
        min=start
        while(max>min):
            while(lista[0]>lista[max]):
                max-=1
            while(lista[0]<lista[min]):
                min+=1
            
            temp=lista[max]
            lista[max]=lista[min]
            lista[min]=temp
        
        return data.quicksort_v_2(lista) + [lista[0]] + data.quicksort_v_2(lista)
    
    
    def findBinary(decimal_number):
        print("Nytt call, Decimal=:",decimal_number)
        if (decimal_number == 0):
            print("Decimal är 0 så returna noll")
            
            return 0; 
        else:
            print("Decimal%2=:",decimal_number%2,"Ska få ut",10*data.test(decimal_number // 2))
            return (decimal_number % 2 + 10 * 
                data.findBinary(decimal_number // 2))
        
        
    def test(decimal_number):
        if (decimal_number == 0):        
            return 0; 
        else:           
            return (decimal_number % 2 + 10 * data.test(decimal_number // 2))
            
            
            
    
    
    def to_binary(tal):
        if(tal==0):
            binary=0
        else:
            binary=tal%2+10*(data.to_binary(tal/2))
        print(binary)
    
 
    
   
   
    
    
    def fib(i,start=1,prev=0):
        if(i<=0):return start
        return data.fib((i-1),(prev+start),start)
        
    def countdown(i):
        if(i<=0):return "i är noll"
        print(i)
        return data.countdown(i-1)    

    def count_digits(tal):
        if(tal>0):
            return (1+data.count_digits(tal//10))
        else:
            return 0
        
    def show_digits(tal):
        if(tal>0):
            return (data.count_digits())
        else:
            return 0

    def reverse(string):
        if(len(string)==0):
            return ""
        return data.reverse(string[1:])+string[0] 
        
    def check_palindrome(string):
        if(len(string)<=1):
            return True
        elif(string[0]==string[len(string)-1]):
            return (data.check_palindrome," ",(string[1:len(string)-1]))
        return False
        
    def digital_root(number):
        if(number<10):
            return number
        return data.digital_root(data.digital_sum(number))
        
    def digital_sum(number):
        if(number<10):
            return number
        return number%10+data.digital_sum(number//10)
        
        
    def in_order(node):
        sträng=""
        sträng+=data.in_order(node.left)
        node.value+" "
        sträng+=data.in_order(node.right)
        
    def list_to_linked(list):
        if(len(list)==0):
            return
        x=Node(list[len(list)//2])
        x.left=data.list_to_linked(list[:len(list)//2])
        x.right=data.list_to_linked(list[(len(list)//2):])
        return x
        
        
 
class Node:
        def __init__(self,value):
            self.value=value
            self.left=None
            self.right=None
 
 
 
 