# -*- coding: utf-8 -*-
{
    'name': 'Расходная накладная для Украины - Sale Order Report Ukrainian ',
    'author': 'Hlv Team Ukraine',
    'website': 'https://hlv-ua.pro',
    'category': 'Sales',
    'depends': ['sale'],
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'UAH',
    'description': """
Друкована форма пропозиції продажу та видаткової накладної 
=======================================
Модуль встановлює форму для другу комерційної пропозиції
та договору на поставки. 
Аналог документа в 1С Заказ покупателя и Реализация товаров и услуг
""",
    'auto_install': False,
    'demo': [],
    'data': [
            'views/report_saleorder.xml',
            'data/sale_report.xml'
        ],
    'installable': True,
    'application': True,
}