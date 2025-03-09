/*
Uma biblioteca está digitalizando seu acervo e precisa de um sistema para registrar os livros. O sistema deve
coletar o título do livro, o número de páginas e o ano de publicação. Deve então calcular o número total de
caracteres no título, dobrar o número de páginas e ajustar o ano de publicação multiplicando-o por 2.
Entrada:
Título do Livro (string)
Número de Páginas (unsigned int)
Ano de Publicação (inteiro)
Saída:
Título Completo
Número Total de Caracteres no Título
Número de Páginas Dobrado
Ano de Publicação Ajustado
*/

#include <stdio.h>
#include <string.h>

char livro [99];
unsigned int paginas;
int ano;

int main(){
    printf("Insira o o título do livro: \n");
    fgets(livro, sizeof(livro), stdin);

    livro[strcspn(livro, "\n")] = '\0';

    printf("Insira o numero de paginas: \n");
    scanf("%u", &paginas);

    printf("Ano de publicao: \n");
    scanf("%d", ano);

    //Local onde havera a impressao dos dados

    printf("Nome do livro: %s \n", &livro);
    printf("numero de caracteres do titulo: %zu \n", strlen(livro));
    float nova_paginas = paginas * 2;
    printf("numero de paginas: %u", &nova_paginas);
    printf("Ano de publicacao: %d\n", &ano);

    return 0;
}