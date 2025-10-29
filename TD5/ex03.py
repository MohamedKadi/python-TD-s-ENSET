
#file == queue
#use an array of tupels [(element,priorite)]
def deposer_dans_queue(file, element,priorite ):
    file.append((element,priorite))

#search for highest priority
#in case there are multiple elements share same priority u go to the older one
# ghykono append donc search linear the first highest priority ght popi
def retirer_de_queue(file):
    max_priority = -1
    if len(file) == 0:
        return -1
    for element in file:
        if max_priority < element[1]:
            max_priority = element[1]
    index = 0
    for element in file:
        if element[1] == max_priority:
            return file.pop(index)
        index +=1

    
        

