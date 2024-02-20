# -*- coding: utf-8 -*-
{
    'name': "demo_hr",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','hr','hr_expense','hr_recruitment','hr_attendance','hr_skills','hr_holidays',
    'hr_contract','hr_contract_types','hr_gamification','hr_employee_updation','hr_employee_transfer',
    'hr_leave_request_aliasing',
    'hr_timesheet','hr_payroll_community','hr_timesheet_attendance','hr_resignation','event','hr_reward_warning','hrms_dashboard',
    'hr_multi_company',
    'hr_payroll_account_community',
    'hr_reminder',
    'oh_employee_creation_from_user',
    'oh_employee_documents_expiry',
    'ohrms_loan','ohrms_loan_accounting','ohrms_salary_advance','ohrms_core',],
    'external_dependencies': {
        'python': ['pandas'],
    },

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'sequence' : -100,
}
