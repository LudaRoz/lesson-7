import os

with open('config.yaml', 'r', encoding='utf-8') as f:
    lines = []
    name_dir, dir = '', ''
    for line in f.readlines():
        print('---')
        print(line)
        dir_name = line.strip()
        lines.append(dir_name)

        if not line.startswith(' '):
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
                os.chdir(dir_name)
                name_dir = dir_name
                print('1')

        elif line.startswith(' ') and not line.endswith(('.py\n', '.html\n')):
            if not os.path.exists(dir_name):
                dir = dir_name
                os.path.join(name_dir, dir_name)
                os.mkdir(dir_name)
                print('2')

        elif line.endswith(('.py\n', '.html\n')):
            print('3')
            if os.path.exists(dir):
                os.path.join(name_dir, dir)
                file = open(dir_name, 'w+')
                file.close()
                print(os.path.join(name_dir, dir))
            else:
                print(os.path.join(name_dir, dir))
                file = open(dir_name, 'w+')
                file.close()
                os.path.join(name_dir)
            print('x')

        print(line)
