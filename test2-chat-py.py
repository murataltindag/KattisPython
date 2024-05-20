#! python3

"""
Automated testing
Assignment: Chat

1. Start the server program
2. Start client programs
3. Input data from standard input for the clients
4. Redirect standard output to files
5. Compare output files to input files

17 points total
"""

import os, time, subprocess, psutil, random, sys
from within_file import WithinFile

def get_port():
	# find a vacant port number
	random.seed(time.time())
	tries = 0
	while tries < 5:
		port = random.randrange(49152, 65535)
		if not (port in [i.laddr.port for i in psutil.net_connections()]):
			print('using port number', port)
		return port
		tries += 1
	return None

def file_exists(filename):
        if os.path.isfile(filename):
                return True
        else:
                print("{} doesn't exist".format(filename))
                return False

points= 0
withinFile= WithinFile()

if (not file_exists('ChatClient.py')) or (not file_exists('ChatServer.py')):
	sys.exit()

port = get_port()
if not port:
        print("Can't find a port number. Please re-run the script.")
        sys.exit()

print( 'Executing 2 clients with a single message...' )
args= ['py','-u','ChatServer.py',str(port)]
server_errors= open( 'server-errors.txt', 'w' )
server= subprocess.Popen( args, stderr= server_errors )

time.sleep( 1 ) 

shell_command= 'py input-writer.py 0 2 client1-msg.txt | py -u ChatClient.py {} >client1-recvd.txt 2>client1-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 1 2 client2-msg.txt | py -u ChatClient.py {} >client2-recvd.txt 2>client2-errors.txt'.format(port)
os.system( shell_command )

print( 'execution completed; grading...' )

found= withinFile.searchText( 'client1-recvd-single-ref.txt', 'client1-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client1 did not receive message' )

found= withinFile.searchText( 'client2-recvd-single-ref.txt', 'client2-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client2 did not receive message' )

print( 'Points so far: ' + str(points) + '/2' )

server.kill()
try:
	server_errors.close()
except Exception:
	pass

print( 'Executing 2 clients with multiple messages...' )

args= ['py','-u','ChatServer.py',str(port)]
server_errors= open( 'server-errors.txt', 'w' )
server= subprocess.Popen( args, stderr= server_errors )

time.sleep( 1 ) 

shell_command= 'py input-writer.py 0 2 client1-msgs.txt | py -u ChatClient.py {} >client1-recvd.txt 2>>client1-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 1 2 client2-msgs.txt | py -u ChatClient.py {} >client2-recvd.txt 2>>client2-errors.txt'.format(port)
os.system( shell_command )

time.sleep( 1 ) 

print( 'execution completed; grading...' )

found= withinFile.searchText( 'client1-recvd-multiple-ref.txt', 'client1-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client1 did not receive messages' )

found= withinFile.searchText( 'client2-recvd-multiple-ref.txt', 'client2-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client2 did not receive messages' )

print( 'Points so far: ' + str(points) + '/4' )

server.kill()
try:
	server_errors.close()
except Exception:
	pass

print( 'Executing 3 clients with a single message...' )

args= ['py','-u','ChatServer.py',str(port)]
server_errors= open( 'server-errors.txt', 'w' )
server= subprocess.Popen( args, stderr= server_errors )

time.sleep( 1 ) 

shell_command= 'py input-writer.py 0 1 client1-msg.txt | py -u ChatClient.py {} >client1-recvd.txt 2>>client1-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client2-msg.txt | py -u ChatClient.py {} >client2-recvd.txt 2>>client2-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client3-msg.txt | py -u ChatClient.py {} >client3-recvd.txt 2>>client3-errors.txt'.format(port)
os.system( shell_command )

time.sleep( 1 ) 

print( 'execution completed; grading...' )

subpoints= 0

found= withinFile.searchText( 'client1-recvd-from-client2-single-ref.txt', 'client1-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client1 did not receive message from client 2' )

found= withinFile.searchText( 'client1-recvd-from-client3-single-ref.txt', 'client1-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client1 did not receive message from client 3' )

found= withinFile.searchText( 'client2-recvd-from-client1-single-ref.txt', 'client2-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client2 did not receive message from client 1' )

found= withinFile.searchText( 'client2-recvd-from-client3-single-ref.txt', 'client2-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client2 did not receive message from client 3' )

found= withinFile.searchText( 'client3-recvd-from-client1-single-ref.txt', 'client3-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client3 did not receive message from client 1' )

found= withinFile.searchText( 'client3-recvd-from-client2-single-ref.txt', 'client3-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client3 did not receive message from client 2' )

points+= (subpoints / 2)

print( 'Points so far: ' + str(points) + '/8' )

server.kill()
try:
	server_errors.close()
except Exception:
	pass

print( 'Executing 3 clients with multiple messages...' )

args= ['py','-u','ChatServer.py',str(port)]
server_errors= open( 'server-errors.txt', 'w' )
server= subprocess.Popen( args, stderr= server_errors )

time.sleep( 1 ) 

shell_command= 'py input-writer.py 0 1 client1-msgs.txt | py -u ChatClient.py {} >client1-recvd.txt 2>>client1-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client2-msgs.txt | py -u ChatClient.py {} >client2-recvd.txt 2>>client2-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client3-msgs.txt | py -u ChatClient.py {} >client3-recvd.txt 2>>client3-errors.txt'.format(port)
os.system( shell_command )

time.sleep( 1 ) 

print( 'execution completed; grading...' )

subpoints= 0

found= withinFile.searchText( 'client1-recvd-from-client2-multiple-ref.txt', 'client1-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client1 did not receive messages from client 2' )

found= withinFile.searchText( 'client1-recvd-from-client3-multiple-ref.txt', 'client1-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client1 did not receive messages from client 3' )

found= withinFile.searchText( 'client2-recvd-from-client1-multiple-ref.txt', 'client2-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client2 did not receive messages from client 1' )

found= withinFile.searchText( 'client2-recvd-from-client3-multiple-ref.txt', 'client2-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client2 did not receive messages from client 3' )

found= withinFile.searchText( 'client3-recvd-from-client1-multiple-ref.txt', 'client3-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client3 did not receive messages from client 1' )

found= withinFile.searchText( 'client3-recvd-from-client2-multiple-ref.txt', 'client3-recvd.txt' )
if found:
	subpoints+= 1
else:
	print( 'client3 did not receive messages from client 2' )

points+= (subpoints / 2)

print( 'Points so far: ' + str(points) + '/11' )

print( 'Executing 3 *new* clients with multiple messages...' )

shell_command= 'py input-writer.py 0 1 client4-msgs.txt | py -u ChatClient.py {} >client4-recvd.txt 2>client4-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client5-msgs.txt | py -u ChatClient.py {} >client5-recvd.txt 2>client5-errors.txt &'.format(port)
os.system( shell_command )

shell_command= 'py input-writer.py 0 1 client6-msgs.txt | py -u ChatClient.py {} >client6-recvd.txt 2>client6-errors.txt'.format(port)
os.system( shell_command )

time.sleep( 1 ) 

print( 'execution completed; grading...' )

found= withinFile.searchText( 'client4-recvd-from-client5-multiple-ref.txt', 'client4-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client4 did not receive messages from client 5' )

found= withinFile.searchText( 'client4-recvd-from-client6-multiple-ref.txt', 'client4-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client4 did not receive messages from client 6' )

found= withinFile.searchText( 'client5-recvd-from-client4-multiple-ref.txt', 'client5-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client5 did not receive messages from client 4' )

found= withinFile.searchText( 'client5-recvd-from-client6-multiple-ref.txt', 'client5-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client5 did not receive messages from client 6' )

found= withinFile.searchText( 'client6-recvd-from-client4-multiple-ref.txt', 'client6-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client6 did not receive messages from client 4' )

found= withinFile.searchText( 'client6-recvd-from-client5-multiple-ref.txt', 'client6-recvd.txt' )
if found:
	points+= 1
else:
	print( 'client6 did not receive messages from client 5' )

server.kill()
try:
	server_errors.close()
except Exception:
	pass

print( 'Points: ' + str(points) );
