from marshmallow import Schema, fields, pre_dump

class IrSchema(Schema):
    salario = fields.Float(required=True)
    dependentes = fields.Float(default=0, blank=True)
    educacao = fields.Float(default=0, blank=True)
    saude = fields.Float(default=0, blank=True)
    pensao = fields.Float(default=0, blank=True)
    previdencia = fields.Float(default=0, blank=True)
    doacoes = fields.Float(default=0, blank=True)
    livro_caixa = fields.Float(default=0, blank=True)