/*
Um funcionário está trabalhando em um projeto de engenharia no qual é necessário calcular a área de esferas de diferentes tamanhos para determinar a quantidade de material necessário para revesti-las. Esse cálculo é essencial para garantir a precisão do projeto e evitar desperdícios.  

Escreva uma função em C chamada `calcularAreaEsfera` que receba o raio de uma esfera como entrada e retorne a área correspondente como um valor em ponto flutuante. A função deve utilizar a fórmula:  

\[
A = 4 \pi r^2
\]

Onde:  
- **A** é a área da esfera,  
- **r** é o raio da esfera,  
- **π** é uma constante matemática, que deve ser definida utilizando a biblioteca `<math.h>`.  

Na função principal, implemente uma lógica que solicite ao usuário o raio da esfera, utilize a função para calcular a área e exiba o resultado. O programa deve permitir que o usuário realize diversos cálculos para diferentes raios até decidir encerrar.
*/

#include <stdio.h>

// Protótipo da função
float calcularAreaEsfera(float r);

// Função principal
int main() {
    float a, r;

    while (1) {
        printf("Insira o raio da esfera (ou um valor negativo para sair): ");
        scanf("%f", &r);

        if (r < 0) break; // Sai do loop se o usuário inserir um valor negativo

        a = calcularAreaEsfera(r);
        printf("A área total da esfera é: %.2f\n", a);
    }

    printf("Programa encerrado...\n");
    return 0;
}

// Função que calcula a área da esfera
float calcularAreaEsfera(float r) {
    return 4.0 * 3.1415 * (r * r);
}
