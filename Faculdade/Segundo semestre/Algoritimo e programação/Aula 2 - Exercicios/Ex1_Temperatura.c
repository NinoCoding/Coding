/*
Você foi contratado por um jornal meteorológico para desenvolver uma ferramenta que ajude os jornalistas a converter temperaturas de graus Fahrenheit para graus Celsius. Isso é essencial porque a maioria das fontes meteorológicas internacionais utiliza Fahrenheit, enquanto o público que assiste ao jornal está mais acostumado com temperaturas em Celsius.  

Escreva uma função em C chamada `converterParaCelsius`, que receberá uma temperatura em graus Fahrenheit como entrada e retornará a temperatura equivalente em graus Celsius. A função deve utilizar a seguinte fórmula de conversão:  


C = \frac{5}{9} \times (F - 32)


Na função principal, implemente uma lógica que permita ao usuário inserir várias temperaturas em Fahrenheit e visualizar suas equivalentes em Celsius. O programa deve continuar solicitando entradas até que o usuário decida sair.
*/


//chamada das bibliotecas
#include <stdio.h>

// Prototipo da função de converter para Celsius
float converterParaCelsius(float grausF);

// Função principal
int main(){

    // Definir variaveis
    float grausF, grausC;

    // Comandos de entrada do usuario
    printf("Insira as temperaturas em Fahrenheit que deseja converter para celsius: ");
    scanf("%f", &grausF);

    // Chamada da função ConverterParaCelcius
    grausC = converterParaCelsius(grausF);

    // Imprimir resultado
    printf("A temperatura em Celsius é: %.2f\n", grausC);
}

// Função para converter F para C
float converterParaCelsius(float grausF){
    float grausC;

    grausC = (5.0/9.0) * (grausF - 32);


    return grausC;
}