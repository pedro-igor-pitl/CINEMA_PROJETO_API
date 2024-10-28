from ..dto.dtoIngresso import IngressoDTO
from ..model.modelIngresso import Ingresso
from ..repository.repositoryIngresso import RepositoryIngresso
import qrcode
import base64
from io import BytesIO

class ServiceIngresso:
    def __init__(self, db):
        self.RepositoryIngresso = RepositoryIngresso(db)

    def criar_ingresso(self, ingresso_dto: IngressoDTO):
        """Cria um novo ingresso com base em um DTO e salva no banco de dados"""
        novo_ingresso = Ingresso(
            id_usuario=ingresso_dto.id_usuario,
            id_sala=ingresso_dto.id_sala,
            id_poltrona=ingresso_dto.id_poltrona,
            qrcode=None,  # O QR Code será gerado a seguir
            data_pedido=ingresso_dto.data_pedido
        )

        # Dados a serem codificados no QR Code
        qr_data = f"{ingresso_dto.id_usuario}_{ingresso_dto.id_sala}_{ingresso_dto.id_poltrona}_{ingresso_dto.data_pedido}"

        # Gera o QR Code como imagem
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Salva o QR Code em Base64 no ingresso
        novo_ingresso.qrcode = qr_code_base64

        # Salva o ingresso no repositório
        ingresso_salvo = self.RepositoryIngresso.save(novo_ingresso)

        # Retorna o modelo convertido para DTO
        return IngressoDTO.from_model(ingresso_salvo)


    def obter_ingresso_por_id(self, id_ingresso):
        """Retorna um ingresso pelo ID, como um DTO"""
        ingresso = self.RepositoryIngresso.find_by_id(id_ingresso)
        if ingresso:
            return IngressoDTO.from_model(ingresso)
        return None

    def listar_ingressos(self):
        """Retorna todos os ingressos como uma lista de DTOs"""
        ingressos = self.RepositoryIngresso.find_all()
        # Converte todos os modelos em DTOs
        return [IngressoDTO.from_model(ingresso) for ingresso in ingressos]

    def atualizar_ingresso(self, id_ingresso, ingresso_dto: IngressoDTO):
        """Atualiza as informações de um ingresso existente com base no DTO"""
        ingresso = self.RepositoryIngresso.find_by_id(id_ingresso)
        if ingresso:
            # Atualiza os campos do modelo com os valores do DTO, se presentes
            ingresso.id_usuario = ingresso_dto.id_usuario if ingresso_dto.id_usuario is not None else ingresso.id_usuario
            ingresso.id_sala = ingresso_dto.id_sala if ingresso_dto.id_sala is not None else ingresso.id_sala
            ingresso.id_poltrona = ingresso_dto.id_poltrona if ingresso_dto.id_poltrona is not None else ingresso.id_poltrona
            ingresso.data_pedido = ingresso_dto.data_pedido if ingresso_dto.data_pedido is not None else ingresso.data_pedido
            
            ingresso_atualizado = self.RepositoryIngresso.update(ingresso)
            return IngressoDTO.from_model(ingresso_atualizado)
        return None

    def deletar_ingresso(self, id_ingresso):
        """Deleta um ingresso pelo ID"""
        return self.RepositoryIngresso.delete(id_ingresso)
