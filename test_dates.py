#!/usr/bin/env python3
"""
Script para testar a formatação de datas brasileiras
"""

from datetime import datetime
from app.utils.date_utils import format_brazilian_date, format_brazilian_datetime

def test_date_formatting():
    # Teste com data atual
    now = datetime.now()
    print(f"Data atual: {now}")
    print(f"Formato brasileiro (data): {format_brazilian_date(now)}")
    print(f"Formato brasileiro (data e hora): {format_brazilian_datetime(now)}")
    print()
    
    # Teste com data específica
    test_date = datetime(2023, 12, 25, 14, 30, 0)
    print(f"Data de teste: {test_date}")
    print(f"Formato brasileiro (data): {format_brazilian_date(test_date)}")
    print(f"Formato brasileiro (data e hora): {format_brazilian_datetime(test_date)}")
    print()
    
    # Teste com string ISO
    iso_string = "2023-12-25T14:30:00"
    print(f"String ISO: {iso_string}")
    print(f"Formato brasileiro (data): {format_brazilian_date(iso_string)}")
    print(f"Formato brasileiro (data e hora): {format_brazilian_datetime(iso_string)}")

if __name__ == "__main__":
    test_date_formatting()
