from odoo import api, fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string='Title', required=True, help="Give course title here")
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)
    session_id = fields.One2many('openacademy.session', 'course_id', string='Sessions')
