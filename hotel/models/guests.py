# models/guests.py
from odoo import models, fields, api

class Guests(models.Model):
    _name = 'hotel.guests'
    _description = 'Hotel Guests'
    _order = 'lastname,firstname,middlename'

    # Create name field first (before other fields)
    name = fields.Char(string='Full Name', compute='_compute_name', store=True, index=True)
    
    lastname = fields.Char(string="Last Name", required=True)
    firstname = fields.Char(string="First Name", required=True)
    middlename = fields.Char(string="Middle Name")
    address_streetno = fields.Char(string="Address / Street & No.")
    address_area = fields.Char(string="Address / Area, Unit & Bldg, Brgy")
    address_city = fields.Char(string="Address / City / Town")
    address_province = fields.Char(string="Address / Province / State")
    zipcode = fields.Char(string="ZIP Code")
    contactno = fields.Char(string="Contact No.")
    email = fields.Char(string="Email")
    gender = fields.Selection([('FEMALE', 'Female'), ('MALE', 'Male')], string="Gender")
    birthdate = fields.Date(string="Birthday")
    photo = fields.Image(string="Guest Photo")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                record.age = today.year - record.birthdate.year - (
                    (today.month, today.day) < (record.birthdate.month, record.birthdate.day)
                )
            else:
                record.age = 0

    @api.depends('lastname', 'firstname', 'middlename')
    def _compute_name(self):
        for record in self:
            name = ""
            if record.lastname:
                name += record.lastname
            if record.firstname:
                if name:
                    name += ", " + record.firstname
                else:
                    name = record.firstname
            if record.middlename:
                if name:
                    name += " " + record.middlename  # Space instead of comma before middle name
                else:
                    name = record.middlename
            record.name = name