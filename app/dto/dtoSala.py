class SalaDTO:
    def __init__(self, id_sala=None, qt_poltrona=None, id_sessao=None):
        self.id_sala = id_sala
        self.qt_poltrona = qt_poltrona
        self.id_sessao = id_sessao

    @staticmethod
    def from_model(sala):
        return SalaDTO(
            id_sala=sala.id_sala,
            qt_poltrona=sala.qt_poltrona,
            id_sessao=sala.id_sessao
        )

    def to_dict(self):
        return {
            'id_sala': self.id_sala,
            'qt_poltrona': self.qt_poltrona,
            'id_sessao': self.id_sessao
        }
