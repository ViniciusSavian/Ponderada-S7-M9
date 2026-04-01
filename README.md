# Ponderada-S7-M9

Projeto em Python inspirado na arquitetura de recomendação da Netflix para demonstrar:
- **1 RF documentado em código**.
- **1 RNF aferido por execução de código**.
- Testes complementares de **Blue Team** e **Red Team**.

## Estrutura
- [docs/Ponderada-S7-M9.md](docs/Ponderada-S7-M9.md)
- [src](src)
- [tests](tests)

## RF-01 implementado
**Top 10 por perfil e gênero com filtro etário**.

Código principal:
- [src/aplicacao/servico_recomendacao.py](src/aplicacao/servico_recomendacao.py)

## RNF-01 aferido
**Desempenho local da recomendação**.

Métricas:
- Média $\leq 80$ ms
- p95 $\leq 120$ ms
- Pico de memória $\leq 150$ MB

Código de aferição:
- [src/benchmark_rnf.py](src/benchmark_rnf.py)

## Como executar
### 1. Validar testes funcionais e de robustez
```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

### 2. Rodar benchmark do RNF
```bash
python3 -m src.benchmark_rnf
```

## Rastreabilidade requisito → evidência
- RF-01: implementado em serviço + validado por [tests/unitarios/test_servico_recomendacao.py](tests/unitarios/test_servico_recomendacao.py) e [tests/blue_team/test_blue_team.py](tests/blue_team/test_blue_team.py)
- RNF-01: aferido por [src/benchmark_rnf.py](src/benchmark_rnf.py) e validado por [tests/nao_funcionais/test_desempenho_recomendacao.py](tests/nao_funcionais/test_desempenho_recomendacao.py)
- Robustez (Red Team): [tests/red_team/test_red_team.py](tests/red_team/test_red_team.py)