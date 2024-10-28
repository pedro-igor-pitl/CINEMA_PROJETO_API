class IngressoDTO:
    def __init__(self, id_ingresso=None, id_usuario=None, id_sala=None, id_poltrona=None, qrcode=None, data_pedido=None):
        self.id_ingresso = id_ingresso
        self.id_usuario = id_usuario
        self.id_sala = id_sala
        self.id_poltrona = id_poltrona
        self.qrcode = qrcode  # Agora permite receber o QR code
        self.data_pedido = data_pedido

    @staticmethod
    def from_model(ingresso):
        return IngressoDTO(
            id_ingresso=ingresso.id_ingresso,
            id_usuario=ingresso.id_usuario,
            id_sala=ingresso.id_sala,
            id_poltrona=ingresso.id_poltrona,
            qrcode=ingresso.qrcode,  # Atribui o QR code do modelo ao DTO
            data_pedido=ingresso.data_pedido
        )

    def to_dict(self):
        dto_dict = {
            'id_ingresso': self.id_ingresso,
            'id_usuario': self.id_usuario,
            'id_sala': self.id_sala,
            'id_poltrona': self.id_poltrona,
            'data_pedido': self.data_pedido
        }
        if self.qrcode is not None:
            dto_dict['qrcode'] = self.qrcode
        return dto_dict
