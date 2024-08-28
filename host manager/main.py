
''''
    Sample host manager for networking (cisco switches, routers, firewalls)
    It works just with show * command
    The netword devices need to have username and password already configured
    The comm  protocol is SSH 
    1. First add he hostname, ip, username and password and press "Add host" button
    2. Write the command to send, select the destination host from list
    3. Click "Send" button and the output will be displayed in the output window
'''

# import the libs
from tkinter import *
from netmiko import ConnectHandler



def is_online(ip):
    try:
        
        response = requests.get("http://"+ip, timeout=5)
        print(f"{ip} is reachable")
        return True
    except requests.ConnectionError:
        print(f"{ip} is unraechable")
        return False
    





root = Tk()
# Tkinter window size
root.geometry("1400x800")
# Tkinter window title
root.title("Host Manager")


# define devices variables
Name = StringVar()
Ip= StringVar()
Username = StringVar()
Password = StringVar()
Command = StringVar()



# Hosts dict 
hosts = {}
def add():
    '''
        This function populate the hosts dict with username, pass, hostname, ip
    '''
    global hosts
    # Add hosts
    hosts[Ip.get()] = {"username":Username.get(), "password":Password.get(),"hostname":Name.get(), "online":True }
    select.delete(0,END) 

    # Add hosts to the GUI window
    for n in hosts.keys():
        select.insert(END, n + " > "+  hosts[n]['hostname'] )#+ " - online" if hosts[n]["online"] else " - offline") 

    # Reset the hosts variables
    Name.set("")
    Ip.set("")
    Username.set("")
    Password.set("")
   
    
    
def remove():
    '''
        This function is to remove the selected host from host GUI window
    '''
    global hosts
    for i in select.curselection():
        print()
        host = select.get(i).split(" ")
        del hosts[host[0]]
        print(select.get(i))
    selection = select.curselection()
    select.delete(selection[0])
    print(hosts)

def send():
    '''
        Send command function
    '''
    print(Command.get())
    ip=[]
    for i in select.curselection():
        local_ip = select.get(i).split(" ") 
        ip.append(local_ip[0])
    command = ConnectHandler(
        device_type = "cisco_xe",
        host=ip[0],
        username = hosts[ip[0]]["username"],
        password=hosts[ip[0]]["username"]

    )
    # recive the output from network device
    response = command.send_command(Command.get())
    
    print(response, type(response))
    # print the output recived in the GUI output window
    output.insert(END, response )
    output.insert(END, "\n \n ")
    del command

    # Tkinter windows 
host_frame = Frame()
host_frame.pack(pady=10)
Label(host_frame, text = "Hostname", font="arial 10").pack(side=LEFT)
Entry(host_frame, textvariable=Name, width=50).pack()

ip_frame = Frame()
ip_frame.pack(pady=10)

Label(ip_frame, text = "Ip:", font="arial 10" ).pack(side=LEFT)
Entry(ip_frame, textvariable=Ip, width=50 ).pack()

username_frame = Frame()
username_frame.pack(padx=10)

Label(username_frame, text = "Username: ", font="arial 10").pack(side=LEFT)
Entry(username_frame, textvariable=Username, width=50).pack()

pass_frame = Frame()
pass_frame.pack(padx=10)

Label(pass_frame, text = "Password", font="arial 10").pack(side=LEFT)
Entry(pass_frame, textvariable=Password, width=50).pack()

Button(root, text = "Add host", font = "arial 10 ", command=add).place(x=10, y=100)


scroll_bar = Scrollbar(root, orient=VERTICAL) 
yscroll_bar = Scrollbar(root, orient=HORIZONTAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12, width=60, foreground="blue") 
Button(root, text="Remove", font="arial 10", command= remove).place(x=10, y=330)
command_frame = Frame()
command_frame.pack(padx=20)

command = Label(command_frame, text = "Show comand to send", font="arial 10").pack(side=LEFT)

entr = Entry(command_frame, textvariable=Command, width=50)
entr.place(x = 50, y = 460)
entr.pack()
Button(root, text="Sent", font="arial 10", command= send).place(x=10, y=480)

output = Text(root,  height=18, width=130, foreground="white", background="black")
output.pack()
output.place(x=200, y=500)
select.place(x=200,y=260) 


root.mainloop()