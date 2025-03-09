/*
Você foi encarregado de desenvolver um sistema para analisar dados de
jogadores que participarão de um campeonato de e-sports, a análise é
feita de forma individual. O sistema deve coletar informações sobre o
jogador, realizar alguns cálculos baseados nos dados fornecidos, e, em
seguida, exibir um resumo detalhado das informações e dos cálculos
realizados.


Entrada:
Nome do Jogador: O nome pode conter espaços e deve ser armazenado em uma string com capacidade para até 50
caracteres.
Inicial do Nome de Jogo (Nickname): O sistema deve solicitar ao usuário que digite a inicial do seu nickname e armazene em
uma variável do tipo char.
Idade do Jogador: A idade deve ser armazenada como um número inteiro (int).
Nível de Habilidade: O sistema deve solicitar ao usuário que informe seu nível de habilidade em uma escala de 1 a 100.
Armazene em uma variável do tipo (float).
Anos de Experiência: Quantos anos ele joga competitivamente. Esse valor deve ser armazenado como um número inteiro
sem sinal (unsigned int).
Preferência por Jogos em Equipe: O usuário deve responder com 1 (para Sim) ou 0 (para Não), e a resposta deve ser
armazenada em uma variável booleana (bool)
*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main(){
    char name [50]; //armazernar a string
    char nickname;
    int idade;
    float skill;
    unsigned int exp;
    bool equipe;

    //pedir nome
    printf("Qual o seu nome completo?: \n");
    scanf("%49[^\n]", &name);

    //apelido
    printf("Qual é o seu apelido (nickname)?: \n");
    scanf("%s", &nickname);

    //idade
    printf("Digite quantos anos voce tem: \n");
    scanf("%d", &idade);

    //habilidade
    printf("Digite a sua habilidade(1 a 100): ");
    scanf("%f", &skill);

    //experiencia
    printf("Digite quantos anos você tem de experiência competitiva: ");
    scanf("%u", &exp);

    printf("Você prefere jogos em equipe? (1 para Sim, 0 para Não): ");
    int temp;
    scanf("%d", &temp);
    equipe = temp;

    /*Area onde havera os calculos pedidos pelo exercicio*/
    // Cálculo da idade em dias
    double idadeEmDias = idade * 365.25;

    //nivel de habilidade ajustado
    float nivelAjustado = skill * (1 + exp / 100);

    //verificações booleanas
    bool maioridade = idade >= 18;
    bool novato = exp < 2;
    bool veteranoPrefereEquipe = exp * !novato;

    // Incremento e Decremento
    unsigned int anosDepoisIncremento = exp++;
    unsigned int anosDepoisDecremento = --exp;

    // Deslocamento de Bits
    int metadeAnos = exp >> 1;
    int dobroAnos = exp << 1;

    /*Local onde havera a impressão */
    printf("\n ***resumo do jogador!*** \n");
    printf("Nome Completo: %s\n", name);
    printf("Inicial do Nickname: %c\n", nickname);
    printf("Idade: %d anos\n", idade);
    printf("Idade em Dias: %.0f dias\n", idadeEmDias);
    printf("Nível de Habilidade Ajustado: %.2f\n", nivelAjustado);
    printf("Anos de Experiência: %u\n", exp);
    printf("Prefere Jogos em Equipe: %d\n", exp);


    printf("\n*** Análise ***\n");
    printf("É maior de idade? %d\n", maioridade);
    printf("É novato? %d\n", novato);
    printf("Jogador Experiente e Prefere Jogos em Equipe? %d\n", veteranoPrefereEquipe);
    printf("\n*** Incremento e Decremento ***\n");
    printf("Anos de Experiência após Incremento: %d\n", anosDepoisIncremento);
    printf("Anos de Experiência após Decremento: %d\n", anosDepoisDecremento);
    printf("\n*** Deslocamento de Bits ***\n");
    printf("Metade dos Anos de Experiência: %u\n", metadeAnos);
    printf("Dobro dos Anos de Experiência: %u\n", dobroAnos);

    return 0;
}