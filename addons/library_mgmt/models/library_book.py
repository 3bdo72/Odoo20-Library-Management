from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char()
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date()
    pages = fields.Integer()
    active = fields.Boolean(default=True)
