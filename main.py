import os
import sys

def command_line_inputs():
    filename, origin, destination = None, None, None
    try:
        filename = sys.argv[1]
        origin = sys.argv[2]
        destination = sys.argv[3]
    except IndexError:
        print('Usage: python main.py filename origin destination')
        sys.exit(1)
    return filename, origin, destination

def main():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    filename, origin, destination = command_line_inputs()
    print('filename: ', filename)
    print('origin: ', origin)
    print('destination: ', destination)
    
    


if __name__ == '__main__':
    main()