/*Escreva um programa que leia um número inteiro positivo e verifique se ele é primo utilizando um método otimizado (não verificando todos os números até ele, mas apenas até sua raiz quadrada).*/

#include <stdio.h>
#include <math.h>

int main(){

    int numero, i, primo = 1;
    float resto;

    printf("Digite um número inteiro positivo: ");
    scanf("%d", &numero);

    //caso se o numero for menor que 1
    if(numero <= 1){
        printf("O número %d não é primo.\n", numero);
        return 0;

    resto = numero % 2;

    //casos especias dos numeros primos
    if (numero == 2 || numero == 3){ {
        printf("O número %d é primo.\n", numero);
        return 0;
    }

    else{
        printf("O número %d é primo.\n", numero);
    }

    return 0;
    }