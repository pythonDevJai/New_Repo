import os

text = input("input text : ")

path = input("input path : ")

# os.chdir(path)


def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    print("files is ~~~~~~~~~~~~~~~~~~>>>>>>>>>>>",files)
    for file_name in files:
        print("item is ==================>>>>>>>>>>",file_name)
        abs_path = os.path.abspath(file_name)
        print("abs_path is ----------------->>>>>>",abs_path)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, "r")
            print("f is *****************>>>>>>>>>>",f)
            if text in f.read():
                f = 1
                print(text + " found in ")
                final_path = os.path.abspath(file_name)
                print("final_path is ###########>>>>>",final_path)
                return True

    if f == 1:
        print(text + " not found! ")
        return False


getfiles(path)


"""
‪E:\
['01-07-2022  Taskk.py', '04-05-2022   Decorator Practice.py', '09-08-2022 OOPS session practice.py',
'09-08-2022 session practice.py', '12-05-2022   API  ALL METHODS PRACTICE.py', '21-07-2022  Basic Get Method Practice.py',
'22-04-2022    Tasks.py', '22-07-2022  Basic Addition Function.py', '23-04-2022   Environment variable creating.py',
'23-04-2022   FOR & IF TASKS.py', '23-04-2022   userName & password  & dealerCode   API.py', '23-07-2022  PATCH METHOD',
'25-04-1998     API Validations.py', '26-07-2022  Fetch Newly Created Leads.py', '27-04-2022    Tasks  CoreTopics.py',
'29-04-2022  Task.py', 'ALL GET METHODS', 'All Get Methods.py', 'API validations  24-04-2022.py', 'ASDF.py', 'checking.py',
'copying data from one table to another table.py', "DataBase  Query's.py", 'Day 6 Session Practice 04-07-2022.py',
'decorator sample fun.py', 'DummyTable  To  MainTable  Inserting Records      25-04-2022.py', 'enumarate function.py',
'False To True.py', 'hgf.py', 'how to insert system data & time', 'INHERITANCE    19-04-2022.py',
'List Tuple Dict  Interview Questions.py', 'logs.log', 'mahesh code.py', 'POST METHOD', 'Project Structure',
'responce.py', 'sdfhs.py', 'std.log', 'sxs.py', "TASK'S.py", 'Task.py', 'TEST.py', "Testing For Api's.py",
'Therading   20-04-2022.py', 'Threading.py', 'w3 resource strings methods.py']

"""
