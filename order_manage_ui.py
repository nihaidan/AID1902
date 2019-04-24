#order_manage_ui.py
#(UI:User Interface,用户借口)
#订单管理程序用户接口层(视图层，View)
#接收用户指令、显示执行结果
from order import *
from order_manage import *

om=None  #订单管理对象、全局变量

def print_menu():   #打印主菜单
    menu='''--------订单管理程序--------
    1 - 查询所有订单
    2 - 根据ID号查询订单
    3 - 新增订单
    4 - 修改订单
    5 - 删除订单
    其他 - 退出'''
    print(menu)

def query_all():#查询所有订单
    orders = om.query_all_order()
    for o in orders:
        print(o)

def query_by_id():#根据订单号查询
    order_no = input("请输入要查询的订单")
    if not order_no:
        print("输入订单号不合法")
        return

    order = om.query_by_id(order_no)
    print("\n查询结果：")
    print(order)    #打印订单信息
    print("\n")

def add_order():#新增订单
    try:
        order_no=input("请输入订单号:")
        cust_id=input("请输入客户编号:")
        products_num=int(input("请输入商品数量:"))
        amt = float(input("请输入订单金额:"))

        new_order = Order(order_no,cust_id,products_num,amt)
        ret= om.insert_order(new_order)
        print(ret)
    except Exception as e:
        print("操作错误")
        print(e)
    return




def main():#主函数
    global om
    om = OrderManage()#实例化OrderManage
    while True:
        print_menu()
        oper = input("请输入要执行的操作")
        if oper =="1":   #查询所有订单
            query_all()
        elif oper == "2":    #根据id号查询订单
            query_by_id()
        elif oper == "3":    #新增订单
            add_order()
        elif oper == "4":    #修改订单
            pass
        elif oper == "5":    #删除订单
            pass
        else:    #其他则退出
            break
if __name__=="__main__":
    main()









