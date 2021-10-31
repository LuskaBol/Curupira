from ..database.setup import Attempt


def check_flag(challId, flag, userId):
    return Attempt.select().where(Attempt.correct == True, Attempt.user_id == userId, Attempt.chall_id == challId)
    # Precisa verificar se o usuário já fez essa chall
    # Precisa verificar a flag
    # Se a flag for correta, marcar como correto