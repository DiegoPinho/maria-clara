from datetime import datetime

def format_brazilian_date(date_obj):
    """
    Formata uma data para o padrão brasileiro (dd/mm/aaaa)
    """
    if isinstance(date_obj, datetime):
        return date_obj.strftime("%d/%m/%Y")
    elif isinstance(date_obj, str):
        try:
            # Tenta converter string ISO para datetime e depois formatar
            dt = datetime.fromisoformat(date_obj.replace('Z', '+00:00'))
            return dt.strftime("%d/%m/%Y")
        except:
            return date_obj
    return str(date_obj)

def format_brazilian_datetime(date_obj):
    """
    Formata uma data e hora para o padrão brasileiro (dd/mm/aaaa HH:MM)
    """
    if isinstance(date_obj, datetime):
        return date_obj.strftime("%d/%m/%Y %H:%M")
    elif isinstance(date_obj, str):
        try:
            # Tenta converter string ISO para datetime e depois formatar
            dt = datetime.fromisoformat(date_obj.replace('Z', '+00:00'))
            return dt.strftime("%d/%m/%Y %H:%M")
        except:
            return date_obj
    return str(date_obj)
