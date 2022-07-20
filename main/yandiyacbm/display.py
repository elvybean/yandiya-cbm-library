from yandiyacbm.py4dbp import Order, Packer
from yandiyacbm.py4dbp_utils import initiate_pallets, pre_pack, re_pack


def divider():
    print("\n------------------------------------------------------------------------------------------------------------------------\n")

def excelrows_display(excelrows: list):
    divider()
    print("excel row data and item quanity")
    for i in range(len(excelrows)):
        row = excelrows[i]
        print("\n",row)
    divider()

def formattedData_display(formattedData: list):
    print("excel row data in the format of Item class objects")
    for i in range(len(formattedData)):
        item = formattedData[i]
        for j in range(len(item)):
            if j == 0:
                print("\n:::::::::::", item[j])
            else:
                print("====> ", item[j])
    divider()

def order_display(order: Order):
    print("Order class object with Products (Item class objects) fitted onto pallets (Bin class objects)")
    for Packer in order.packers:
        for Bin in Packer.bins:
            print("\n:::::::::::", Bin.string())
            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
            if len(Bin.unfitted_items) != 0:
                print("UNFITTED ITEMS:")
                for item in Bin.unfitted_items:
                    print("====> ", item.string())
    divider()            
