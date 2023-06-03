#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__== '__main__':
    items_amount={}
    num_of_orders=0
    largest_order=0
    hungriest=""
    with open(sys.argv[1],'r') as file_containing_orders:
        person = file_containing_orders.readline()
        while person:
            full_amount=0
            num_of_orders += 1
            for i in range(int(file_containing_orders.readline())):
                (item, quantity) = file_containing_orders.readline().split(': ')
                items_amount[item] = (float(quantity)+ items_amount.get(item,0.0))
                full_amount += float(quantity)
            if full_amount > largest_order:
                largest_order=full_amount
                hungriest=person.strip()
            person = file_containing_orders.readline()

    str_processing='Processing {}\n'.format(sys.argv[1])
    str_num_of_orders='Number of orders: {}\n'.format(num_of_orders)
    str_the_hungriest='The hungriest person today was {0}!\nThe largest order size was {1}.\n'.format(hungriest, largest_order)

    str_items='Item totals:\n'
    for item in items_amount:
        str_items += '    {0}: {1}\n'.format(item,items_amount[item])
            
    with open('orders_report.txt','w') as output_file:
        output_file.write(str_processing)
        output_file.write(str_num_of_orders)
        output_file.write(str_the_hungriest)
        output_file.write(str_items)

    print(str_processing + str_num_of_orders + str_the_hungriest + str_items)
