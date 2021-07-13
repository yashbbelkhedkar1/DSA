file = open('patient_data.txt','r')

for line in file :
    list = line.split('|')
    
    for i in list[2:] :
        print(i,end= " ")
        
file.close()
