__all__ = ["estado"]

estado = {
        "partida": False,
        "cor_selecionada": -1,
        "tentativa_tmp": [-1, -1, -1, -1, -1, -1]
}

def get_estado():
    global estado
    return estado
