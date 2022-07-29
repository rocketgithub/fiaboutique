# -*- coding: utf-8 -*-

from odoo import api, models
import odoo.addons.l10n_gt_extra.a_letras as a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'fiaboutique.abstract.reporte_account_payment'

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_id.line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    def a_letras(self,monto):
        return a_letras.num_a_letras(monto)
    
    def _get_report_values(self, docids, data=None):
        model = 'account.payment'
        docs = self.env['account.payment'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'a_letras': self.a_letras,
            'totales': self.totales,
        }

class ReportPayment1(models.AbstractModel):
    _name = 'report.fiaboutique.reporte_account_payment1'
    _inherit = 'fiaboutique.abstract.reporte_account_payment'
    
class ReportPayment2(models.AbstractModel):
    _name = 'report.fiaboutique.reporte_account_payment2'
    _inherit = 'fiaboutique.abstract.reporte_account_payment'
    
class ReportPayment3(models.AbstractModel):
    _name = 'report.fiaboutique.reporte_account_payment3'
    _inherit = 'fiaboutique.abstract.reporte_account_payment'