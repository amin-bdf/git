from odoo import api, fields, models, _
import xlwt
from xlwt import *
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition
import base64
import io


class JournalItemReportXLS(models.TransientModel):
    _name = 'journal.items.report.xls'
    _description = 'Journal Item Report Xls'

    name = fields.Char('Report')
    data = fields.Binary('Data Excel')

    def journal_line_generate_xls_report(self):
        borders = Borders()
        borders.bottom = Borders.THIN
        borders.top = Borders.THIN
        borders.left = Borders.THIN
        borders.right = Borders.THIN

        borders1 = Borders()
        borders1.left = 6
        borders1.right = 6
        borders1.top = 6
        borders1.bottom = 6

        wbk = xlwt.Workbook()

        style_left = xlwt.easyxf('align: horiz left;borders: top HAIR, bottom HAIR, left HAIR, right HAIR;')
        style_num = xlwt.easyxf('align: horiz right;borders: top HAIR, bottom HAIR, left HAIR, right HAIR;')
        style_num_dec = xlwt.easyxf('align: horiz right;borders: top HAIR, bottom HAIR, left HAIR, right HAIR;')
        style_num_dec.num_format_str = '0.00'
        style_bold_purple = xlwt.easyxf(
            'pattern: pattern solid;font: bold 1,height 240,color white; align: horiz center, wrap 1;borders: top HAIR, bottom HAIR, left HAIR, right HAIR;')
        style_center = xlwt.easyxf('align: horiz center;borders: top HAIR, bottom HAIR, left HAIR, right HAIR;')

        sheet1 = wbk.add_sheet("Journal Items Report")
        row = 0
        sheet1.row(row).height = 700
        sheet1.write_merge(row, row, 0, 10, 'Journal Items Report', style_bold_purple)

        row = 1
        sheet1.row(row).height = 600
        sheet1.col(0).width = 2000
        sheet1.col(1).width = 4000
        sheet1.col(2).width = 6000
        sheet1.col(3).width = 6000
        sheet1.col(4).width = 12000
        sheet1.col(5).width = 8000
        sheet1.col(6).width = 8000
        sheet1.col(7).width = 5000
        sheet1.col(8).width = 5000
        sheet1.col(9).width = 5000
        sheet1.col(10).width = 4000

        sheet1.row(row).height = 700
        sheet1.write(row, 0, 'Sl.No', style_bold_purple)
        sheet1.write(row, 1, 'Date', style_bold_purple)
        sheet1.write(row, 2, 'Reference', style_bold_purple)
        sheet1.write(row, 3, 'Origin', style_bold_purple)
        sheet1.write(row, 4, 'Partner', style_bold_purple)
        sheet1.write(row, 5, 'Journal', style_bold_purple)
        sheet1.write(row, 6, 'Account', style_bold_purple)
        sheet1.write(row, 7, 'Debit', style_bold_purple)
        sheet1.write(row, 8, 'Credit', style_bold_purple)
        sheet1.write(row, 9, 'Balance', style_bold_purple)
        sheet1.write(row, 10, 'Currency', style_bold_purple)

        rec_id = self._context.get('active_ids')
        active_model = self._context.get('active_model')
        active_id = self.env[active_model].search([('id', 'in', rec_id)])
        sl = 0
        total_debit = 0.0
        total_credit = 0.0
        total_balance = 0.0
        for line in active_id:
            row = row + 1
            total_debit += line.debit
            total_credit += line.credit
            total_balance +=  line.balance
            sl = sl + 1
            sheet1.write(row, 0, sl, style_num)
            sheet1.write(row, 1, line.date.strftime('%d-%m-%Y'), style_center)
            sheet1.write(row, 2, line.ref or '', style_left)
            sheet1.write(row, 3, line.move_id.name or '', style_left)
            sheet1.write(row, 4, line.partner_id.name or '', style_left)
            sheet1.write(row, 5, line.journal_id.name or '', style_left)
            sheet1.write(row, 6, line.account_id.name or '', style_left)
            sheet1.write(row, 7, line.debit, style_num_dec)
            sheet1.write(row, 8, line.credit, style_num_dec)
            sheet1.write(row, 9, line.balance, style_num_dec)
            sheet1.write(row, 10, line.move_id.currency_id.name, style_left)

        row += 1
        sheet1.write(row, 6, "Total", style_bold_purple)
        sheet1.write(row, 7, total_debit, style_num_dec)
        sheet1.write(row, 8, total_credit, style_num_dec)
        sheet1.write(row, 9, total_balance, style_num_dec)

        fp = io.BytesIO()
        o = wbk.save(fp)
        out = base64.b64encode(fp.getvalue())
        self.write({'data': out, 'name': 'Journal Items Report.xls'})
        return {
            'type': 'ir.actions.act_url',
            'url': '/journal_items_print/journal_item_xls_report?model=salary.computation.report&id=%s' % self.id,
            'target': 'new',
        }


class return_xls_download(http.Controller):
    _cp_path = '/product_extended'

    @http.route('/journal_items_print/journal_item_xls_report', type='http', auth="public")
    def harvest_report_xls_download(self, **data):
        harvest_search = http.request.env['journal.items.report.xls'].search([('id', '=', data.get('id'))])
        if harvest_search:
            filecontent = base64.b64decode(harvest_search.data)
            filename = harvest_search.name
            if filecontent and filename:
                return request.make_response(filecontent,
                                             headers=[('Content-Type', 'application/octet-stream'),
                                                      ('Content-Disposition', content_disposition(filename))])
        return request.not_found()