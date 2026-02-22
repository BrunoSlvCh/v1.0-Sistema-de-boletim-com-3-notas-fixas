from datetime import datetime

medias = []
aprovados = 0
reprovados = 0
aluno = 0

def media (nota1, nota2, nota3):
         
        if not (0 <= nota1 <= 10 and
                0 <= nota2 <= 10 and
                0 <= nota3 <= 10):
                return None

        return (nota1 + nota2 + nota3) / 3

dataAtual = datetime.now()
dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M:%S")

while True:

        print("\n==== 📝 SISTEMA DE BOLETIM 📝 ====")

        primeiraNota = float(input("Digite a primeira nota: "))
        segundaNota = float(input("Digite a segunda nota: "))
        terceiraNota = float(input("Digite a terceira nota: "))

        resultado = media (primeiraNota, segundaNota, terceiraNota)

        if resultado is None:
                 print("🚫 NOTA INVÁLIDA! DIGITE VALORES ENTRE 0 E 10! 🚫")
        else:
                aluno += 1
                medias.append(resultado)

                if resultado >= 7:
                        print("Situaçao: Aprovado(a)! 🎉")
                        aprovados += 1
                        situacao = "Aprovado(a)"
                else:
                        print("Situaçao: Reprovado(a)! 👎")
                        reprovados += 1
                        situacao = "Reprovado(a)"

                print(f"\nSua média final é de: {resultado:.2f}")

                with open ("boletimFinal.txt", "a", encoding="utf-8-sig") as arquivo:
                        arquivo.write(f"\nAluno: {aluno} - Media: {resultado:.2f} - Situacao: {situacao}\n")
        
        pergunta = input("Deseja continuar calculando médias? [s/n] ").lower()

        if pergunta != "s":
             print("\n==== ENCERRAMENTO DO SISTEMA ====")

             break


if len(medias) > 0:

        media_geral = sum(medias) / len(medias)

        print("=== 📊 RESUMO DO DESEMPENHO DA TURMA 📊 ===")
        print(f"🧑‍🎓 Total de alunos: {len(medias)}")
        print(f"📝 Média geral da turma: {media_geral:.2f}")
        print(f"✅ Alunos aprovados: {aprovados}")
        print(f"❌ Alunos reprovados: {reprovados}")

        with open("boletimFinal.txt", "a", encoding="utf-8-sig") as arquivo:
                arquivo.write("\n=== RESUMO DO DESEMPENHO DA TURMA ===")
                arquivo.write(f"\nGerado em: {dataFormatada}\n")
                arquivo.write(f"\nTotal de alunos: {len(medias)}")
                arquivo.write(f"\nMedia geral da turma:  {media_geral:.2f}")
                arquivo.write(f"\nAlunos aprovados: {aprovados}")
                arquivo.write(f"\nAlunos reprovados: {reprovados}")
                arquivo.write("\n-------------------------------------------\n")

else:
        print("Nenhuma média válida foi registrada no sistema.")