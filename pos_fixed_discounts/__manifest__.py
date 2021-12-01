# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Point of Sale Fixed Discounts',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

This module allows the cashier to quickly give percentage-based
discount to a customer.

""",
    'author':'Sahar Dagher',
    'license':'LGPL-3',
    'depends': ['point_of_sale','pos_discount'],
    'data': [
        'data/product_data.xml',
        'views/pos_fixed_discount_views.xml',
        'views/pos_fixed_discount_templates.xml'
    ],
    'qweb': [
        'static/src/xml/FixedDiscountButton.xml',
    ],
    'installable': True,
    'auto_install': True,
}
