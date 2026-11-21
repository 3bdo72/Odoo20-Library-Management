from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_ids = fields.Many2many('library.author', 'library_book_author_rel', 'book_id', 'author_id', string='Authors')
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date()
    pages = fields.Integer()
    active = fields.Boolean(default=True)
