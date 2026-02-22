# Sistema de Boletim em Python

Projeto desenvolvido em Python para registro e cálculo de médias escolares.
O sistema permite inserir notas, calcular a média individual do aluno, determinar sua situação (aprovado ou reprovado) e gerar um relatório completo com estatísticas da turma.
Ao final da execução, é criado um arquivo .txt contendo todas as informações registradas, incluindo data e hora da geração do relatório no padrão brasileiro.

---

## Sobre o projeto

O sistema permite:

- Inserir três notas por aluno
- Validar se as notas estão entre 0 e 10
- Calcular a média automaticamente
- Classificar como Aprovado(a) ou Reprovado(a) 
- Armazenar os resultados em um arquivo `.txt`
- Registro automático da data e hora (formato brasileiro dd/mm/aaaa HH:MM:SS) no momento em que a nota é computada
- Exibir um resumo estatístico da turma ao final da execução
- (Média a partir de 7.0 para ser aprovado, menor do que 7.0 o aluno é reprovado)

---

## Conceitos praticados

Durante o desenvolvimento, trabalhei com:

- Definição e uso de funções
- Estruturas de repetição (`while`)
- Condicionais (`if/else`)
- Validação de dados
- Manipulação de arquivos com `open()`
- Cálculo de média geral e contadores
- Organização e legibilidade de código

---

## Estrutura

sistema-boletim/
│
├── boletim.py
└── README.md

---

## Como executar

Clone o repositório: https://github.com/BrunoSlvCh/v1.0-Sistema-de-boletim-com-3-notas-fixas

---

## Versionamento

### v1.0 – Estrutura inicial do sistema
- Cálculo de média com 3 notas fixas
- Validação de notas entre 0 e 10
- Classificação automática (Aprovado(a) / Reprovado(a))
- Registro individual dos alunos em arquivo .txt
- Geração de resumo final da turma
- Registro de data e hora no padrão brasileiro

Próxima melhoria planejada:
- Tornar a quantidade de notas dinâmica (usuário poderá definir quantas avaliações deseja inserir)

## Objetivo

Este projeto representa uma etapa importante na minha evolução como desenvolvedor.  
Com ele consegui evoluir e fortalecer a minha base em lógica, controle de fluxo e manipulação de dados em Python.

Continuo evoluindo este repositório conforme avanço nos estudos.
