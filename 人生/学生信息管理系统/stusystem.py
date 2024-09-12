#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
filename = 'student.txt'
def main():
    while True:
        menm()
        choice=int(input('请选择'))
        if choice in range(0,8):
            if choice == 0:
                answer = input('您确定退出吗？y/n')
                if answer=='y' or answer =='Y':
                    print('谢谢您的使用')
                    break   #退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menm():
    print('===============学生信息管理系统=================')
    print('-------------------功能菜单---------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出')
    print('-------------------------------------------------')

def insert():
    student_list = []
    while True:
        id = input('请输入ID：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = input('请输入英语成绩：')
            python = input('请输入python成绩：')
            java = input('请输入java成绩：')
        except:
            input('输入无效，请重新输入')
            continue
        #将录入的学生信息保存到字典
        student = {'id':id,'name':name,'english':english,'python':python,'java':java}
        #将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    #调用save函数
    save(student_list)
    print('学生信息录入完毕')

def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass
def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    student_id = file.readlines()
            else:
                student_old = []
            flag=False   #标记书否有删除
            if student_old:
                with open(filename,'w',encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print('')

def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()