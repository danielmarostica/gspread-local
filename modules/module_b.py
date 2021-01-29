import pandas as pd
import pyodbc as pyodbc
def run_bgc):
    wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1AaPoJgBuXCe6jzjUIaR7zDk')
    mega = wb.worksheet('Sheet1')
    
    print('...')

    server = ''
    database = ''
    username = ''
    password = ''

    try:
        connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = connection.cursor()
    except:
        sys.exit('Falha na conexão.')
    else:
        print('Conectado!')
    
    print('Executando query...')
    sql = "SELECT"
    rows = cursor.execute(sql)
    
    print('Atualizando dados...')
    df = pd.DataFrame.from_records(rows, columns=[col[0] for col in cursor.description])

    mega.update([df.columns.values.tolist()] + df.values.tolist())
    print('Dados atualizados: https://docs.google.com/spreadsheets/d/1AaPoJgBG6jzjUIaR7zDk')