# -*- coding: utf-8 -*-

from odoo import api, models
import odoo.addons.l10n_gt_extra.a_letras as a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'vidareal.abstract.reporte_account_payment'

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    def _get_report_values(self, docids, data=None):
        self.model = 'account.payment'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
            'data': data,
            'a_letras': a_letras,
            'totales': self.totales,
        }

class ReportPayment1(models.AbstractModel):
    _name = 'report.vidareal.reporte_account_payment1'
    _inherit = 'vidareal.abstract.reporte_account_payment'

class ReportPayment2(models.AbstractModel):
    _name = 'report.vidareal.reporte_account_payment2'
    _inherit = 'vidareal.abstract.reporte_account_payment'

class ReportPayment3(models.AbstractModel):
    _name = 'report.vidareal.reporte_account_payment3'
    _inherit = 'vidareal.abstract.reporte_account_payment'
