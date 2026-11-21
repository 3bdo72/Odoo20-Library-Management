from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string="Author's Name", required=True)
    country = fields.Char()
    birth_date = fields.Date()
    book_ids = fields.Many2many('library.book', 'library_book_author_rel', 'author_id', 'book_id', string='Books')
