#-*- coding:utf-8 -*-
import argparse
import sys
import os

def main(args):
    folder_name = args.input
    identifier = args.count
    fname = args.output

    file_list = sorted(os.listdir(folder_name), key=len)
    if not fname:
        fname = "result_" + folder_name + ".sql"
    for f in file_list:
        parse_hla = parsing(f, folder_name)
        write_sql(parse_hla, fname, identifier)
        identifier+=1

def write_sql(parse_list, fname, identifier):
    file = open(fname, 'a')
    sql='INSERT INTO `HLA_TYPE`(Subject_Identifier, Gene, Field1, Field2, Field3, Field4, Suffix) VALUES '
    for a in parse_list:
        a = list(map(lambda x: "NULL" if x == " " else x, a))
        sql += f"({identifier}, '{a[0]}', '{a[1]}', '{a[2]}', '{a[3]}', '{a[4]}', '{a[5]}'),"

    sql = sql[:-1] + ";"
    file.writelines(sql)

    file.close()

def parsing(file_name, folder_name):
    f = open(folder_name + "/" + file_name, 'r')
    data = f.read()
    r0 = data.split('\n\n\n\t\t\t\t')
    parse_hla = []
    r1 = []
    for r in r0:
        r1.append(r.split('\n\t\t\t\t'))
    r1.pop(0)
    for r in r1:
        # for loop
        count = 0
        try:
            for i in range(2):
                # spacing split 
                temp = r[i].split(' ')
                # 맨 앞 숫자 판단 2번 넣을 지 1번 넣을 지 판단 
                count += int(temp[0])
                if count == 2:
                    # 앞의 allele 그대로 넣기 
                    parse_hla.append(parse_hla[-1])
                    continue
                # * split 
                gene = temp[2].split('*')
                
                suffix = ' '
                try: 
                    int(gene[1][-1])
                except:
                    suffix = gene[1][-1]
                    gene[1] = gene[1][:-1]

                # : split
                field = gene[1].split(':') 
                # field 개수 세기 
                null_cnt = 4-len(field)
                # list 만들기 
                allele = []
                allele.append(gene[0])
                for f in field:
                    allele.append(f)
                for i in range(null_cnt):
                    allele.append(' ')
                allele.append(suffix)
                # append to parse_hla 
                parse_hla.append(allele)
        except IndexError:
            parse_hla.append(parse_hla[-1])
    return parse_hla
        
def __main__():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('Data Settings')
    group.add_argument('-i', '--input', required=True, metavar='DIR', help='path to the directory with the input report files')
    group.add_argument('-o', '--output', default=None, type=str, help='output file name')
    group.add_argument('--count', default=1, type=int, help='start of identifier number')
    
    args=parser.parse_args(sys.argv[1:])
    main(args)

if __name__=='__main__':
    __main__()
