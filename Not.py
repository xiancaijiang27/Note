# try:放想运行的代码;except放出错时运行的代码
# 改show_tasks()才能让展示的每个任务独占一行
# for 索引,元素 in enumerate(元素):             同时得到元素索引和元素本身,不写start索引默认从0开始
# return让函数在特定位置结束,防止执行不该执行的逻辑
tasks=[]
def add_task():
    name=input("请输入任务名:").strip()
    print(f"重置任务状态请重新输入任务名:\n")
    for task in tasks:
        if task["name"]==name:
            task["done"]=False
            print(f"任务\"{name}\"状态重置成功!\n")
            return
    tasks.append({"name":name,"done":False})
    print("任务添加成功!\n")
def show_tasks():
    print("----------任务列表----------")
    if not tasks:
        print("当前没有任务!\n")
    else:
        for num,task in enumerate(tasks,start=1):
            if task["done"]:
                print(f"{num}. {task['name']}                 已完成")
            else:
                print(f"{num}. {task['name']}                 待完成")

def mark_done():
    show_tasks()
    try:
        name_done = int(input("请输入已完成的任务编号:")) - 1
        if 0<=name_done<len(tasks):
            tasks[name_done]["done"]=True#外层写数字是因为外层为list,内层写"done"是因为内层为dict
            print("任务已完成!\n")
        else:
            print("无效的数字编号!\n")
            mark_done()
    except:
        print("请输入数字编号!\n")
        mark_done()
def delete_tasks():
    show_tasks()
    try:
        delete_name = int(input("请输入想删除的任务编号:")) - 1
        if 0 <= delete_name < len(tasks):
            del tasks[delete_name]
            print("删除成功!\n")
        else:
            print("无效的数字编号!\n")
            delete_tasks()
    except:
        print("请输入数字编号!\n")
        delete_tasks()

def main():
    while True:
        print("-----------menu-----------")
        print("添加任务、重置任务状态  【输入1】")
        print("查看任务               【输入2】")
        print("标记任务为完成         【输入3】")
        print("删除任务               【输入4】")
        print("退出                  【输入5】")
        choice=int(input(">>>"))
        if choice==1:
            add_task()
            continue
        elif choice==2:
            show_tasks()
            continue
        elif choice==3:
            mark_done()
            continue
        elif choice==4:
            delete_tasks()
            continue
        elif choice==5:
            print("退出成功")
            break
        else:
            print("请输入有效数字(1-5)\n")
            continue
main()
