def calcular_nova_taxa_de_conversao(melhoria):
  return df['Taxa de Conversão (%)'].mean() * (1 + melhoria)

def calcular_conversoes_adicionais(melhoria):
  taxa_de_nova_conversao = calcular_nova_taxa_de_conversao(melhoria)
  return taxa_de_nova_conversao * df['Visitantes Únicos'].sum() - df['Taxa de Conversão (%)'].mean() * df['Visitantes Únicos'].sum()

valores_melhoria = np.linspace(0.01, 0.2, 10)

resultado = []

for melhoria in valores_melhoria:

  taxa_de_nova_conversao = calcular_nova_taxa_de_conversao(melhoria)
  conversoes_adicionais = calcular_conversoes_adicionais(melhoria)

  resultado.append({
    'melhoria': melhoria,
    'taxa_de_nova_conversao': taxa_de_nova_conversao,
    'conversoes_adicionais': conversoes_adicionais
  })

df_results = pd.DataFrame(resultado)

sns.lineplot(data=df_results, x='melhoria', y='taxa_de_nova_conversao')
plt.xlabel('Melhoria na taxa de conversão')
plt.ylabel('Conversões adicionais')
plt.show()
