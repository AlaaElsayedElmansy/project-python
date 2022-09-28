import time
import datetime
def saveuserdatails(userdetails):
    try:
        fileobj= open ("users.txt", "a")
    except:
        print("issue happend")
        return False
    else:
        fileobj.write(f"{userdetails}\n")
        return True
def saveprojectdatails(detail):
    try:
        fileobj= open ("projects.txt", "a")
    except:
        print("issue happend")
        return False
    else:
        fileobj.write(f"{detail}\n")
        return True

def askforemail(message):
    import re
    email = input(message)
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
        return email
    else:
        print("Not vaild")
        return askforemail(message)

def askforstring(message):
    mystr = input(message)
    if mystr.isspace() or not mystr:
        print("Not vaild")
        return askforstring(message)
    return mystr

def askforphonenumber(message):
    PhoneNumber = input(message)
    import re
    if len(PhoneNumber) > 7:
        if re.match("^01[01245][0-9]{8}$", PhoneNumber) :
            return PhoneNumber
        else:
            print("not vaild")
            return askforphonenumber(message)

    else:
        print("must be 11 numbers")
        return askforphonenumber(message)

def askforpassword(message):
    pass1 = input(message)
    pass2 = input("enter your password again")
    if pass1 == pass2:
        print("done")
        return str(pass1)
    else:
        print("not the same")
        return askforpassword(message)


def askfordate(message):
    projdate = input(message)

    try:
        datetime.datetime.strptime(projdate, '%Y-%m-%d')

    except:
        print("should be YYYY-MM-DD")
        askfordate(message)

    else:
        return str(projdate)


def askfordetails():
    FirstName = askforstring("enter your first name ")
    LastName = askforstring("enter your last name ")
    email= askforemail("enter your email")
    password = askforpassword("enter password ")
    Phonenumber = askforphonenumber("enter your phone number")
    #id = input("enter id")
    return  FirstName, LastName, email, str(password), str(Phonenumber)


def projectmenu(usermail):
    choice = input(
        "Please enter:\n (1) for 'create new Project'\n (2) for 'view Projects'\n (3) for 'delete a Project' \n (4) for 'edit a Project'\n")
    if choice == "1":
        print("create")
        create()
    elif choice == "2":
        print("view")
        view()
    elif choice == "3":
        print("delete")
        delete()

    elif choice == "4":
        print("edit")
        finaledit()


    else:
        print("invalid input")
        return projectmenu()



def generate_id():
    id = round(time.time())
    return id


def Registration():
    print("YOUR DATA")
    details = list(askfordetails())
    print(details)
    id = generate_id()
    details.insert(0, str(id))
    details = ":".join(details)
    print(details)
    added = saveuserdatails(details)
    if added:
        print("done")
    else:
        print("error")
        return Registration()
def create():
    detail = list(creatprojet())
    print(detail)
    detail = ":".join(detail)
    print(detail)
    added = saveprojectdatails(detail)
    return detail

def login():
    email = askforemail("Enter e-mail: ")
    password = input("Enter login Password: ")

    try:
        loginfo = open("users.txt", "r")
    except Exception as e:
        print(" error happend ")
    else:

        loginn = loginfo.readlines()
        loginfo.close()

        for info in loginn:
            userinfo = info.strip("\n")
            userinfo = userinfo.split(":")
            #print(userinfo)

            if userinfo[3] == email and userinfo[4] == password:
                return projectmenu(email)


        else:
            print("Wrong e-mail or password!!")
            login()

def creatprojet():
    Title = askforstring("enter Title :")
    Details = askforstring("enter description :")
    TotalTarget = str(input("enter Target :"))
    StartDate = askfordate("enter start (yyyy-mm-dd)")
    EndDate = askfordate("enter end (yyyy-mm-dd)")
    proid = str(input("project id"))
    return str(proid), Title,Details,str(TotalTarget),StartDate,EndDate

def view():

    try:
        users_projects = open("projects.txt", "r")
    except Exception as e:
        print(e)
    else:
        projects=users_projects.readlines()
        for project in projects:
            user_project = project.strip("\n")
            user_project = user_project.split(":")
            print(user_project)

        users_projects.close()
        return projects



def deleteproject(usermail):
    view()
    project_id = input("Please choose id of the book you want to delete: ")
    #deleted = delete_project_from_file(project_id, usermail)


def delete():
    all_projects = view()
    project_name = input('\nSelect one projct to edit : ')
    count =-1
    for project in all_projects:
        count+=1
        user_project = project.strip("\n")
        user_project = user_project.split(":")
        if user_project[0] == project_name:
            project_name_index = count
            all_projects.pop(project_name_index)
            print("done")
            break
    else:
        print("this project name is n't exist ,, please try again")
    w = open("projects.txt", "w")
    w.writelines(all_projects)
    w.close()

def edit():
    all_projects = view()
    project_name = input('\nSelect one projct to edit : ')
    count = -1
    for project in all_projects:
        count += 1
        user_project = project.strip("\n")
        user_project = user_project.split(":")
        if user_project[0] == project_name:
            project_name_index = count
            all_projects.pop(project_name_index)
            print("done")

            break
    else:
        print("this project name is n't exist ,, please try again")
    w = open("projects.txt", "w")
    w.writelines(all_projects)
    w.close()
    if project_name:
        proid = project_name
        Title = askforstring("enter Title :")
        Details = askforstring("enter description :")
        TotalTarget = str(input("enter Target :"))
        StartDate = askfordate("enter start (yyyy-mm-dd)")
        EndDate = askfordate("enter end (yyyy-mm-dd)")
        return str(proid), Title, Details, TotalTarget, StartDate, EndDate











def finaledit():
    print('okay')
    detail = edit()
    print(detail)
    detail = ":".join(detail)
    print(detail)
    added = saveprojectdatails(detail)
    return detail









