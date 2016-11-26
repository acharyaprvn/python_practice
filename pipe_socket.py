#function to convert a list into hash table

def convert_to_hash(list):
    hash_table = {}
    index = 0
    for x in list:
        hash_table[x] = index
        index = index+1
    return hash_table

####

pipe_size = [4,5.5,6,7]  #set of pipe with different sizes
socket_size = [7,6,5.5,4] # set of socket with different sizes
hash_table_pipe_size = {} # hash table for pipe data. 
hash_table_socket_size = {} # hash table for socket data. 
output_list = [] # list to store the output

# convert list to hash table
hash_table_pipe_size = convert_to_hash(pipe_size)
hash_table_socket_size = convert_to_hash(socket_size)
###

#matching size of pipe to corresponding socket size.

for size in hash_table_pipe_size.keys():
	pipe_index = hash_table_pipe_size[size]
	socket_index = hash_table_socket_size[size]
	output_list.append((pipe_index, socket_index))


#####
	
print output_list

#Note: Format of output (i,j); where i is the index of pipe in pipe_size
#                                    j is the index of socket that matches the pipe at i
