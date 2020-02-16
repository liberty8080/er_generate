# -*- coding: utf-8 -*-


from sqlalchemy import (MetaData, Table, Column, Integer, String, ForeignKey)
from eralchemy import render_er
import json

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


if __name__ == '__main__':
    dat = {
        "user": [{
            "column_name": 'user_table',
            "data_type": "VARCHAR",
        }],
        "表1": [{
            "column_name": "列名",
            "data_type": "VARCHAR",
            "fk": "user.column_name"
        }]
    }
    tab = transfer_table(dat)
    render_er(tab, 'test.png')
    print(tab)
