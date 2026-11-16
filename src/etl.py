import pandas as pd

def processar_dados(caminho_csv):
    # 1. Lê os dados exportados do Cerberus
    df = pd.read_csv(caminho_csv)
    
    # 2. Calcula o Saldo Retido (Sua dor específica)
    df['Saldo_Retido'] = df['Qtd_Recebida'] - df['Qtd_Devolvida']
    
    # 3. Cria a lógica de rastreamento
    def status_devolucao(row):
        if row['Saldo_Retido'] == 0:
            return "✅ Devolvido Total"
        elif row['Saldo_Retido'] > 0 and row['Qtd_Devolvida'] > 0:
            return f"⚠️ Parcial (Ref. NF {row['NF_Devolucao_Ref']})"
        else:
            return "❌ Pendente (Não devolvido)"
            
    df['Status_Devolucao'] = df.apply(status_devolucao, axis=1)
    
    return df