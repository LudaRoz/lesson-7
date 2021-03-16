import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

os.chdir(dir_name)
dir_list = 'authapp', 'adminapp', 'mainapp', 'settings'
for index in dir_list:
    if not os.path.exists(index):
        os.mkdir(index)
