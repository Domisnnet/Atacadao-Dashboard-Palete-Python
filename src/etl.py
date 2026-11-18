import pandas as pd

def processar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['Saldo_Retido'] = df['Qtd_Recebida'] - df['Qtd_Devolvida']
    def status_devolucao(row):
        if row['Saldo_Retido'] == 0:
            return "✅ Devolucão Total"
        elif row['Saldo_Retido'] > 0 and row['Qtd_Devolvida'] > 0:
            nf_ref = str(row['NF_Devolucao_Ref']).replace('.0', '')
            return f"⚠️ Parcial - Referente a NF {nf_ref}"
        else:
            return "❌ Pendente/Não devolvido"     
    df['Status_Devolucao'] = df.apply(status_devolucao, axis=1)
    return df
