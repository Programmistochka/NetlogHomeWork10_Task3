class Files:
    def __init__(self, name, lines, inf_lines):
        self.name = name
        self.lines = lines
        self.inf_lines = []

    def __str__(self):
        res = f'{self.name}\n{self.lines}\n{self.inf_lines}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Files):
            print(f'Ошибка. {other} не относится к классу Files')
        else:
            return self.lines < other.lines


file1 = Files('2.txt', 0, [])
file2 = Files('1.txt', 0, [])
file3 = Files('3.txt', 0, [])
file4 = Files('4.txt', 0, [])

list_files = [file1, file2, file3, file4]

for f in list_files:
    with open (f.name, 'rt', encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            f.inf_lines += [line]
            f.lines += 1
    #print(f)


list_files.sort()

print(f'\nРезультирующий файл: data.txt\n')
with open ('data.txt', 'w', encoding = 'utf-8') as file:
    for f in list_files:
        file.writelines(f'{f.name}\n')
        file.write(f'{f.lines}\n')
        for line in f.inf_lines:
            file.write(f'{line}\n')
        file.write('')

with open ('data.txt', 'rt', encoding = 'utf-8') as file:
    for line in file:
        print(line.strip())