import multiprocessing
import time

def printhi():
    while(1):
        print ('Hi')
        time.sleep(2)

def main():

    print_hi = multiprocessing.Process(target=printhi)
    print_hi.start()

    while (input("Enter Bye: ") != "Bye"):
        pass

    print_hi.terminate()


if __name__ == '__main__':
    main()