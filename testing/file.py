import sys, subprocess

def entry():
    try:
        script, filename = sys.argv

        if sys.platform == "linux" or sys.platform == "linux2":
            subprocess.call("clear", shell=True)
        else:
            subprocess.call("cls", shell=True)

        banner()

        global txt
        txt = open(filename, "w")

        sys.stdout.write("""This tool is going to erase the contents in the file
Press Ctrl^C to stop this process
You can hit RETURN to continue
""")
        print(input("?" ))

        print("\ncontent is wiped!!")
        txt.truncate()

        print("Do you want to write in this file?")
        admit = input("> ")

        if admit == "yes":
            line1 = input("Enter first line: ")
            line2 = input("Enter second line: ")
            line3 = input("Enter last line: ")

            print("writing....\n")
            txt.write(line1)
            txt.write("\n")
            txt.write(line2)
            txt.write("\n")
            txt.write(line3)
            txt.write("\n")

            txt.close()
            
            print("Your contents are as follows:")
            txt = open(filename)
            print(txt.read())
        else:
            close()

    except KeyboardInterrupt:
        close()

def close():
    sys.exit("\nExiting... Thank you!!")

def banner():
    BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
    sys.stdout.write(YELLOW + """

██╗        ██╗ ███████╗██╗   ██╗ ██████╗ ██╗     ██╗   ██╗███████╗
██║ 	   ██║ ██╔════╝██║   ██║██╔═══██╗██║     ██║   ██║██╔════╝
██║        ██║ █████╗  ██║   ██║██║   ██║██║     ██║   ██║█████╗
██║   █═╗  ██║ ██╔══╝  ╚██╗ ██╔╝██║   ██║██║     ██║   ██║██╔══╝
██║  ███║  ██║ ███████╗ ╚████╔╝ ╚██████╔╝███████╗╚██████╔╝███████╗ 
╚██╗ ███╚═██╔╝ ╚══════╝  ╚═══╝   ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝  
 ╚████ ████╔╝""" + RED +"   We wipe, We write and We change your files auto" + YELLOW + """
  ╚══╝ ╚═══╝\n\n""" + END)


entry()
