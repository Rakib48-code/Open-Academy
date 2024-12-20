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
    taken_seats = fields.Float(string='Taken seats', compute='_taken_seats')



    @api.depends('seats','attendance_id')
    def _taken_seats(self):
        for r in self:
            if r.seats > 0:
                r.taken_seats = 100.0 * len(r.attendance_id) / r.seats
            else:
                r.taken_seats = 0.0
    #
    # @api.depends('attendance_id')
    # def _get_attendance_count(self):
    #     for r in self:
    #         r.attendees_count = len(r.attendee_ids)
