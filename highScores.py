# By Bilal Majeed and Ivan Nesevski on June 2/2013
# These have the functions for writing, and reading, and saving the scores
# from and to the "singleScore.py" file 

def write(l):
    """ writes the scores from the list "l" to the
        singleScores.txt file """
    
    fin = open("singleScore.txt", "w") #open the file for writing
    for item in l:
        fin.write(str(item)+"\n")  #writes the scores

def read():
    """ reads the scores file and finds the highest score """
    
    count = 0
    fin = open("singleScore.txt")
    for line in fin:
        line = line.strip()

        num = int(line)
        
        if count == 0:
            high = num
    
        if num > high:
            high = num
            
        count = 1

    return high

def save():
    """ saves all scores in the file to a list """
    
    fin = open("singleScore.txt")
    l = []
    for line in fin:
        word = line[:-1]
        l.append(int(word))
    return l


        

        
    
