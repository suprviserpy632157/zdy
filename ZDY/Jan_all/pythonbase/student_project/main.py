# file:main.py
import student_info as si
import menu
def main():
    #此列表用于保存学生数据
    infos=[]
    while 1:
        menu.show_menu()
        s=input("请选择：")
        if s=="1":
            infos+=si.input_student()
        elif s=="2":
            si.output_student(infos)
        elif s=="3":
            si.del_stu(infos)
        elif s=="4":
            si.modify_stu(infos)
        elif s=="5":
            si.student_score_sort_h_l(infos)
        elif s=="6":
            si.student_score_sort_l_h(infos)
        elif s=="7":
            si.student_age_sort_h_l(infos)
        elif s=="8":
            si.student_age_sort_l_h(infos)
        elif s=="9":
            infos = si.stu_read()
        elif s=="10":
            si.save_to_file(infos)
        elif s=="q":
            break                
main()  