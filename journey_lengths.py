def read_journey_lengths(filename):
    my_file= open(filename, 'r')  #the file is opened
    lines = my_file.readlines()
    d={}
    e={}  #the empty dictionaries are defined to create a nested dictionary
    f={}
    for line in lines:
        words = line.split()  # this line is to create a list which has the list of words that are in line.
        if words[0] not in d:
            d[words[0]] = words[0]  #key takes value
            d[words[0]] = {}       #to define the key as dictionary
            d[words[0]][words[1]] = int(words[2])  #value takes a number
            
        if words[1] not in d:   #this if statement is to create the dictionary reversely
            d[words[1]] = words[1]     
            d[words[1]] = {}                
            d[words[1]][words[0]] = int(words[2])      
        
        if words[0] in d:  #if d has a city, the time is just appended
            e = d[words[0]]   #the key will be equal to e which is the empty dictionary to don't lose the previous key's dictionary
            e[words[1]] = int(words[2])
                            
        if words[1] in d:
            f = d[words[1]]
            f[words[0]] = int(words[2])         
    
    my_file.close()    
    return d
    
def read_train_schedule(filename):  
    file = open(filename,'r') 
    lines = file.readlines()
    c=[]   
    d={}
    e={}  #e is defined to create nested dictionary
    
    for line in lines:
        words = line.split()
    
        for a in range (len(words)):
            if words[a].isdigit():
                c += [int(words[a])]  #c will be include integer values of time schedules
        
        if words[0] not in d:     #the same things with the first function
            d[words[0]] = words[0]
            d[words[0]] = {}        
            d[words[0]][words[1]] = c  
                
        if words[0] in d:
            e=d[words[0]]
            e[words[1]] = c
                
        c=[]      #here c will be empty again. because, if it is not, c continue to take values over the previous ones 
    file.close()    
    return d

def reachable_from (journey_lengths, train_schedules, dest_city, time):
    l = []
    for city in train_schedules:       
        if dest_city in train_schedules[city]:   #we try to reach values which mean also dest cities
            if city in journey_lengths and dest_city in journey_lengths[city]:
                if min(train_schedules[city][dest_city]) + journey_lengths[city][dest_city] <= time:
                    l.append(city)  #if we want to arrive in time or before the time, we have to sum up min schedule and journey length
    return l

def write_to_file (list_of_cities, output_filename):  #the function is defined to write the file
    f = open(output_filename, 'w')
    for city in list_of_cities:
        f.write(city + "\n")   #this is to pass to the new row which contain city
    f.close()
        
#print(read_journey_lengths("journey_lengths.txt"))
#print(read_train_schedule("train_schedule.txt"))
#print(reachable_from (read_journey_lengths("journey_lengths.txt"), read_train_schedule("train_schedule.txt"), dest_cty, time))
dict_journey = read_journey_lengths('journey_lengths.txt')
dict_schedule = read_train_schedule('train_schedule.txt')
list_cities = reachable_from(dict_journey, dict_schedule, 'Paris', 15)
write_to_file(list_cities, 'results.txt')   #we will write a file which contains the list of cities