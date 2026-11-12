# Nagro / AgRisk - Risk Score Sync

Utilitario interno para consolidar respostas de score AgRisk no fluxo de analise da Nagro.

O processo le amostras de propostas, normaliza o resultado do score e gera um arquivo local para verificacao manual. Integracao de rede ainda nao implementada neste branch.

## Contexto

- Organizacao consumidora: Nagro (`nagro.co`)
- Motor de score: AgRisk (`agrisk.com.br`)
- Operacao: sincronizacao de scores para conciliacao de propostas

## Execucao local

```bash
python src/sync.py
```

## Configuracao

Ver `config/integration.yaml` e `.env.local` para os parametros locais. Os exemplos incluidos usam dados e credenciais sinteticos sem acesso a servicos reais.

// qmx //
