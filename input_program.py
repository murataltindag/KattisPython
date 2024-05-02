import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-o', type=str, default=None)
parser.add_argument('-t', type=str, default=None)
parser.add_argument('-h', action='store_true')

args = parser.parse_args()

o = args.o
t = args.t
h = args.h

print("Standard Input:")

while True:
    try:
        print(input())
    except EOFError:
        break

print("Command line arguments:")
if(o is not None):
    print("-o: " + o)
    
if(t is not None):
    print("-t: " + t)

if(h):
    print("-h: ")