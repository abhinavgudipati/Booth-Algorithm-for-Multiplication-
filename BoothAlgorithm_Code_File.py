#Function to convert the decimal integers to binary
def decimalToBinary(i):
    answer = "";
    temp = abs(i);
    while(temp > 0):
        answer = str(temp%2) + answer ;
        temp = temp//2;
    return(answer);

#Perform Right shift  operation
def right_shift_operation(i):
    return i[:-1]

#Take ones complement of the negative number 
def onescomplement(i):
    answer = "" # the answer is first stores as a string
    for t in i:
        if t == '0': 
            answer = answer + '1'; # 0 is changed to 1
        else:
            answer = answer + '0'; # 1 is changed to 0
    return answer

#Adds two binary numers
def binaryAddition(i,j):
    answer = "";
    carry = False;
    maximum_length = max(len(i), len(j))
    for q in range(0,maximum_length-len(i)):
        i = "0" + i
    for q in range(0,maximum_length-len(j)):
        j = "0" + j
    i = i[::-1]
    j = j[::-1]
    for p,q in zip(i,j):
        if p == '1' and q == '1' and not carry:
            carry = True;
            answer = answer + "0";
        elif p == '1' and q == '1' and carry:
            carry = True;
            answer =  answer + "1";
        elif p == '0' and q == '0' and not carry:
            carry = False;
            answer = answer + "0";
        elif p == '0' and q == '0' and carry:
            carry = False;
            answer = answer + "1";
        elif ((p == '0' and q == '1') or (p == '1' and q == '0')) and not carry:
            answer = answer + "1"
            carry = False;
        elif ((p == '0' and q == '1') or (p == '1' and q == '0')) and carry:
            answer = answer + "0"
            carry = True;
    if carry:
        answer = answer + "1"
    answer = answer[::-1]
    return answer

#Calculate twos complement
def twosComplement(i): 
    temp = onescomplement(i)
    return binaryAddition(temp, "1")

def main():
    print("Enter the numbers you want to be multiplied")
    a = int(input()) ## taking input of the two integers
    b = int(input()) 

    a_binary = decimalToBinary(abs(a)); # the given integers are converted to binary 
    b_binary = decimalToBinary(abs(b));

    #Normalise the binary
    maximum_length = max(len(a_binary), len(b_binary));

    #Obtaining the same length for both the inputs 
    for p in range(len(a_binary), maximum_length+1): 
        a_binary = '0' + a_binary;
    for p in range(len(b_binary), maximum_length+1):
        b_binary = '0' + b_binary;

    #If negative take twos complement
    if(a < 0):
        a_binary = twosComplement(a_binary)
    if(b < 0):
        b_binary = twosComplement(b_binary)

    maximum_length = max(len(a_binary), len(b_binary));
    #print(a_binary + "   " + b_binary)
    #Normalisation done
    ac = ''
    for p in range(0,maximum_length):
        ac += '0'
    q_nPlusOne = '0'

    count = maximum_length

    while not count == 0:
        #print(ac , a_binary , q_nPlusOne, count)

        count = count - 1;

        if(a_binary[-1] == '1' and  q_nPlusOne ==  '0'):
            ac = binaryAddition(ac,twosComplement(b_binary))
        elif(a_binary[-1] == '0' and  q_nPlusOne ==  '1'):
            ac = binaryAddition(ac,b_binary)
            #print(ac)
        ac = ac[-maximum_length:]
        #Right Shifting
        q_nPlusOne = a_binary[-1]
        last = ac[-1]
        if(ac[0] == '0'):
            ac = '0' + ac
        else:
            ac = '1' + ac


        if(count == -1):
            break
        a_binary = last + a_binary
        ac = right_shift_operation(ac)
        a_binary = right_shift_operation(a_binary)
    answer = ac + a_binary
    negative = False;
    if(answer[0] == '1'):
        answer = twosComplement(answer)
        negative = True;
    file = open('outputfile.txt', 'w')
    if(negative):
        answer1 = twosComplement(answer)
        a = int(answer, 2)
        file.write("Answer in Binary(2's complement) is : " + answer + "\n" + "Answer in Decimal is : - " + str(a) )
    else:
        a = int(answer,2)
        file.write("Answer in Binary is : " + answer +  "\n"  + "Answer in Decimal is : + " + str(a) )
    file.close()

main()

