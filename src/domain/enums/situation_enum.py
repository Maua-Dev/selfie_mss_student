from enum import Enum


class SITUATION(Enum):
    APPROVED = "Aprovado"
    DECLINED = "Reprovado"
    INREVIEW = "Em análise"
    NOTSENT = "Não enviado"
