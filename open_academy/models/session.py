from odoo import api, fields, models

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Session'

    name = fields.Char(required=True)
    start_date = fields.Date(string='Start Date')
    duration = fields.Float(string='Duration', digits=(6,2), help='Duration in days')
    seats = fields.Integer(string='Number of seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
    attendance_id = fields.Many2many('res.partner', string='Attendace')