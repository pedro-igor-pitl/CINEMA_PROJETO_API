class PoltronaDTO:
    def __init__(self, id_poltrona=None, posicao=None, tipo_poltrona=None, id_sala=None):
        self.id_poltrona = id_poltrona
        self.posicao = posicao
        self.tipo_poltrona = tipo_poltrona
        self.id_sala = id_sala

    @staticmethod
    def from_model(poltrona):
        return PoltronaDTO(
            id_poltrona=poltrona.id_poltrona,
            posicao=poltrona.posicao,
            tipo_poltrona=poltrona.tipo_poltrona,
            id_sala=poltrona.id_sala
        )

    def to_dict(self):
        return {
            'id_poltrona': self.id_poltrona,
            'posicao': self.posicao,
            'tipo_poltrona': self.tipo_poltrona,
            'id_sala': self.id_sala
        }
