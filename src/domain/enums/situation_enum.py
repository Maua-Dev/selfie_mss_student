from enum import Enum


class SITUATION(Enum):
    APPROVED = "Aprovado"
    DECLINED = "Reprovado"
    IN_REVIEW = "Em análise"
    NOTSENT = "Não enviado"
