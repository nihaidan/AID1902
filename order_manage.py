#order_manage.py
#订单管理类（业务逻辑层/控制层）
#处理跟订单相关的逻辑操作，调用DAO来实现数据存取
from order import *
from order_dao import *

class OrderManage:
    def __init__(self):
        #实例化数据访问对象
        self.order_dao=OrderDao()
    
    #根据订单号查询订单
    def query_by_id(self, order_id):
        if not order_id:
            pritn("订单编号对象非法")
            return None
        if order_id == "":
            print("订单编号不能为空")
            return None
        return self.order_dao.query_by_id(order_id)


    #查询所有订单
    def query_all_order(self):
        #做业务逻辑方面处理，此处不需要做
        return self.order_dao.query_all_order()
    
    #修改订单
    def update_order(self,order):
        if (not order.order_id) or order.order_id=="":
            print("订单编号不能为空")
            return
        if order.products_num < 1:
            print("商品数量非法")
            return
        if order.amt - 10.00<0.00001:#订单金额小于十元
            print("订单金额小于最低起购价")
            return
        return self.order_dao.update_order(order)

