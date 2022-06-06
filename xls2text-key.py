import xlrd

def file_name(cell):
    num_type = type(cell.value)
    if num_type == float:
        num = str(int(cell.value))
    elif num_type == int:
        num = str(cell.value)
    elif num_type == str:
        num = cell.value    
    return num

def split_title(cell):
    string1 = cell.value.split(" / ")
    string2 = string1[0].replace("*", "")
    return string2

def split_key(cell):
    return cell.value.split(" - ")

wb = xlrd.open_workbook("test.xls")
sh = wb.sheet_by_index(0)

for row in sh.get_rows():
    n = file_name(row[0])
    txt = split_title(row[1])
    keys = split_key(row[2])
    
    txt_file = n + ".txt"
    with open(txt_file, 'w+', encoding='utf-8') as tf:
        tf.write(txt)
    
    key_file = n + ".key"
    with open(key_file, 'w+', encoding='utf-8') as kf:
        for key in keys:
            kf.write(key)
            kf.write('\n')