# -*- coding: utf-8 -*-
from sqlalchemy import (MetaData, Table, Column, String, ForeignKey)

from eralchemy import render_er

'''
metadata = MetaData()
users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              )
orders = Table('orders', metadata,
               Column('order_id', Integer()),
               Column('user_id', ForeignKey('users.user_id')),
               )
'''


def transfer_table(data):
    metadata = MetaData()
    if isinstance(data, dict):
        for table_name, columns in data.items():
            table = Table(table_name, metadata)
            for col in columns:
                x = _transfer_column(col)
                table.append_column(x)
        return metadata


def _transfer_column(col_dict):
    if isinstance(col_dict, dict):
        col = Column(col_dict['column_name'], String)
        if col_dict.__contains__('fk'):
            col.append_foreign_key(ForeignKey(col_dict['fk']))
        return col


def transfer_table2(data):
    metadata = MetaData()
    if isinstance(data, list):
        for entity in data:
            table = Table(entity["entity"], metadata)

            # print(entity["entity"])
            index = 0
            for col in entity["column"]:
                col = Column(col)
                if entity["fk"] != "" and index == 0:
                    col.append_foreign_key(ForeignKey(entity["fk"]))
                table.append_column(col)
                print(index)
                index += 1

    return metadata


if __name__ == '__main__':
    dat = {
        "user": [{
            "column_name": 'user_table',
            "data_type": "VARCHAR",
        }],
        "表1": [{
            "column_name": "列名",
            "data_type": "VARCHAR",
            "fk": "user"
        }]
    }
    data2 = [{"entity": "user1", "column": ["c1", "c2", "c3"], "fk": ""},
             {"entity": "user2", "column": ["c1", "c2", "c3"], "fk": "user1"},
             {"entity": "user3", "column": ["c1", "c2", "c3"], "fk": "user1"}]

    # tab = transfer_table(dat)
    # render_er(tab, 'test2.png')
    # print(tab)

    render_er(transfer_table2(data2), "test2.png")
