#include <stdio.h>
#include <string.h>

//TRABALHO 7 AUTOR: JOSIMAR RACHETTI PEIXOTO RA:1430481921015 CURSO: ANÁLISE DESENVOLVIMENTO DE SISTEMAS FATEC CARAPICUIBA
typedef struct
{
    char nome[50];
    char cidade[20];
    char cpf[20];
    char telefone[20];
    char email[50];
    int cod_cliente;
} cliente;

typedef struct
{
    char nome[50];
    char cidade[20];
    char telefone[20];
    char cnpj[20];
    char email[50];
    int cod_restaurante;
} restaurante;

typedef struct
{
    int cod_cliente;
    int cod_restaurante;
    char descricao[255];
    float valor;
    char forma_pagamento[20];
    int cod_pedido;
} pedido;

int apenasNumero(char* valor){
int i;
for(i=0;i<strlen(valor);i++){
    if(isdigit(valor[i])== 0){
        return 1;
    }
}
    return 0;
}

void formaPagamento(char *forma, int opcao){
    if(opcao==0){
         strcpy(forma,"dinheiro");
        return;
    }else if(opcao==1){
        strcpy(forma,"cartao credito");
        return;
    }else if(opcao==2){
        strcpy(forma,"cartao debito");
        return;
    }else{
        strcpy(forma,"invalido");
        return;
    }
}

int clientesCadastro(cliente dados_clientes[],int qtd_novos_clientes, int qtd_total_clientes){
    int y=0;
    int dados_encontrados=0;
    int x = qtd_novos_clientes+qtd_total_clientes;
    printf("\ndigite os seguintes dados do(s) cliente(s):");
    for(qtd_total_clientes;qtd_total_clientes<x;qtd_total_clientes++){
        printf("\ncliente numero %i\n",qtd_total_clientes+1);

        printf("nome:\n");
        scanf(" %[^\n]s%*c",dados_clientes[qtd_total_clientes].nome);

        printf("cidade:\n");
        scanf(" %[^\n]s%*c",dados_clientes[qtd_total_clientes].cidade);

        do{
            dados_encontrados=0;
            y=0;
            printf("cpf [sem espaco e apenas numeros]:\n");
            scanf(" %s%*c",dados_clientes[qtd_total_clientes].cpf);

            for(y;y<qtd_total_clientes;y++){
                if(strcmp(dados_clientes[y].cpf,dados_clientes[qtd_total_clientes].cpf)==0){
                    printf("cpf ja cadastrado\n");
                    dados_encontrados=1;
                }}
        }while(apenasNumero(dados_clientes[qtd_total_clientes].cpf) == 1 || dados_encontrados == 1);

        do{
        printf("telefone [sem espaco e apenas numeros]:\n");
        scanf(" %s%*c",dados_clientes[qtd_total_clientes].telefone);
        }while(apenasNumero(dados_clientes[qtd_total_clientes].telefone));

        printf("email:\n");
        scanf(" %[^\n]s%*c",dados_clientes[qtd_total_clientes].email);

        do{
            dados_encontrados=0;
            y=0;
            printf("codigo cliente[somente numeros]:\n");
            scanf("%i%*c",&dados_clientes[qtd_total_clientes].cod_cliente);

            for(y;y<qtd_total_clientes;y++){
                if(dados_clientes[y].cod_cliente==dados_clientes[qtd_total_clientes].cod_cliente){
                    printf("codigo cliente ja cadastrado\n");
                    dados_encontrados=1;
                }}
        }while(dados_encontrados == 1);


    }


return qtd_total_clientes;

}

int restaurantesCadastro(restaurante dados_restaurantes[],int qtd_novos_restaurantes, int qtd_total_restaurantes){
    int y=0;
    int dados_encontrados=0;
    int x = qtd_novos_restaurantes+qtd_total_restaurantes;

    printf("\ndigite os seguintes dados do(s) restaurante(s):");
    for(qtd_total_restaurantes; qtd_total_restaurantes<x;qtd_total_restaurantes++)
    {
        printf("\nrestaurante numero %i\n",qtd_total_restaurantes+1);

        printf("nome:\n");
        scanf(" %[^\n]s%*c",dados_restaurantes[qtd_total_restaurantes].nome);

        printf("cidade:\n");
        scanf(" %[^\n]s%*c",dados_restaurantes[qtd_total_restaurantes].cidade);

        do{
        dados_encontrados=0;
        y=0;
        printf("cnpj [sem espacos e apenas numeros]:\n");
        scanf(" %s%*c", &dados_restaurantes[qtd_total_restaurantes].cnpj);
        for(y;y<qtd_total_restaurantes;y++){
            if(strcmp(dados_restaurantes[y].cnpj,dados_restaurantes[qtd_total_restaurantes].cnpj)==0){
                printf("cnpj ja cadastrado\n");
                dados_encontrados=1;
            }}


        }while(apenasNumero(dados_restaurantes[qtd_total_restaurantes].cnpj) == 1 || dados_encontrados == 1);

        do{
        printf("telefone [sem espacos e apenas numeros]:\n");
        scanf(" %s%*c",dados_restaurantes[qtd_total_restaurantes].telefone);
        }while(apenasNumero(dados_restaurantes[qtd_total_restaurantes].telefone) == 1);

        printf("email:\n");
        scanf(" %[^\n]s%*c",dados_restaurantes[qtd_total_restaurantes].email);
        do{
        dados_encontrados=0;
        y=0;
        printf("codigo restaurante:\n");
        scanf("%i%*c",&dados_restaurantes[qtd_total_restaurantes].cod_restaurante);
        for(y;y<qtd_total_restaurantes;y++){
            if(dados_restaurantes[y].cod_restaurante == dados_restaurantes[qtd_total_restaurantes].cod_restaurante){
                printf("codigo restaurantes ja cadastrado\n");
                dados_encontrados=1;
            }}
        }while(dados_encontrados == 1);

    }
return;
}

int pedidosCadastro(pedido dados_pedidos[],int qtd_novos_pedidos,int qtd_total_pedidos,cliente dados_cliente[],int qtd_clientes,restaurante dados_restaurantes[],int qtd_restaurantes){
    int x = qtd_novos_pedidos+qtd_total_pedidos;
    int opc_forma_pagamento;
    char forma[20];
    int y;
    int dados_encontrados;

    printf("\ndigite os seguintes dados do(s) pedido(s):");
    for(qtd_total_pedidos;qtd_total_pedidos<x;qtd_total_pedidos++){
        printf("\npedido numero %i\n",qtd_total_pedidos+1);


        y=0;
        dados_encontrados=0;
        printf("codigo cliente cadastrado:\n");
        scanf("%i%*c",&dados_pedidos[qtd_total_pedidos].cod_cliente);
        for(y;y<qtd_clientes;y++){
            if(dados_pedidos[qtd_total_pedidos].cod_cliente==dados_cliente[y].cod_cliente){
                dados_encontrados=1;}}
        if(dados_encontrados==0){printf("cliente nao cadastrado\n"); return;}

        y=0;
        dados_encontrados=0;
        printf("codigo restaurante:\n");
        scanf("%i%*c",&dados_pedidos[qtd_total_pedidos].cod_restaurante);
        for(y;y<qtd_restaurantes;y++){
            if(dados_pedidos[qtd_total_pedidos].cod_restaurante==dados_restaurantes[y].cod_restaurante){
                dados_encontrados=1;}}
        if(dados_encontrados==0){printf("restaurante nao cadastrado\n"); return;}


        printf("descricao:\n");
        scanf(" %[^\n]s%*c",dados_pedidos[qtd_total_pedidos].descricao);


        do{
        printf("forma de pagamento [0] dinheiro [1] cartao credito [2] cartao debito:\n");
        scanf("%i",&opc_forma_pagamento);
        formaPagamento(forma,opc_forma_pagamento);
        }while(strcmp(forma,"invalido")==0);

        strcpy(dados_pedidos[qtd_total_pedidos].forma_pagamento,forma);

        printf("valor:\n");
        scanf("%f%*c",&dados_pedidos[qtd_total_pedidos].valor);
        do{
        dados_encontrados=0;
        y=0;
        printf("codigo pedido:\n");
        scanf("%i%*c",&dados_pedidos[qtd_total_pedidos].cod_pedido);
        for(y;y<qtd_total_pedidos;y++){
            if(dados_pedidos[y].cod_restaurante == dados_pedidos[qtd_total_pedidos].cod_restaurante){
                printf("codigo pedido ja cadastrado\n");
                dados_encontrados=1;
            }}

        }while(dados_encontrados == 1);
    }

return qtd_total_pedidos;
}


void clientesConsulta(cliente dados_clientes[],int qtd_total_clientes){
    int i = 0;
    int encontrou_dados=0;
    int opc_consulta = 0;
    int codigo_cliente = 0;
    char nome_cliente[50];
    char cidade_cliente[20];
    char cpf_cliente[20];

    printf("CONSULTA BASE CLIENTES.\n Opcoes:\n 1 - Consulta por codigo cliente 2 - consulta por nome 3 - consulta CPF 4 - consulta por cidade\n opcao:");
    scanf("%i",&opc_consulta);

    if(opc_consulta==1){
        printf("digite o codigo do cliente:\n");
        scanf("%i",&codigo_cliente);
        for(i;i<qtd_total_clientes;i++){
            if(dados_clientes[i].cod_cliente==codigo_cliente){
                printf("---------------------\n");
                printf("CLIENTE\ncodigo:%i\n",dados_clientes[i].cod_cliente);
                printf("Nome:%s\n",dados_clientes[i].nome);
                printf("Cpf:%s\n",dados_clientes[i].cpf);
                printf("Cidade:%s\n",dados_clientes[i].cidade);
                printf("Email:%s\n",dados_clientes[i].email);
                printf("Telefone:%s\n",dados_clientes[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==2){
        printf("digite o nome do cliente:\n");
        scanf("%s",nome_cliente);
        for(i;i<qtd_total_clientes;i++){
            if(strcmp(dados_clientes[i].nome,nome_cliente)== 0){
                printf("---------------------\n");
                printf("CLIENTE\ncodigo:%i\n",dados_clientes[i].cod_cliente);
                printf("Nome:%s\n",dados_clientes[i].nome);
                printf("Cpf:%s\n",dados_clientes[i].cpf);
                printf("Cidade:%s\n",dados_clientes[i].cidade);
                printf("Email:%s\n",dados_clientes[i].email);
                printf("Telefone:%s\n",dados_clientes[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return ;
    }else if(opc_consulta==3){
        printf("digite o cpf do cliente:\n");
        scanf("%s",cpf_cliente);
        for(i;i<qtd_total_clientes;i++){
            if(strcmp(dados_clientes[i].cpf,cpf_cliente)== 0){
                printf("---------------------\n");
                printf("CLIENTE\ncodigo:%i\n",dados_clientes[i].cod_cliente);
                printf("Nome:%s\n",dados_clientes[i].nome);
                printf("Cpf:%s\n",dados_clientes[i].cpf);
                printf("Cidade:%s\n",dados_clientes[i].cidade);
                printf("Email:%s\n",dados_clientes[i].email);
                printf("Telefone:%s\n",dados_clientes[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }

        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==4){
        printf("digite a cidade do cliente:\n");
        scanf("%s",cidade_cliente);
        for(i;i<qtd_total_clientes;i++){
            if(strcmp(dados_clientes[i].cidade,cidade_cliente)== 0){
                printf("---------------------\n");
                printf("CLIENTE\ncodigo:%i\n",dados_clientes[i].cod_cliente);
                printf("Nome:%s\n",dados_clientes[i].nome);
                printf("Cpf:%s\n",dados_clientes[i].cpf);
                printf("Cidade:%s\n",dados_clientes[i].cidade);
                printf("Email:%s\n",dados_clientes[i].email);
                printf("Telefone:%s\n",dados_clientes[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else{
        printf("opção invalida");
        return;
    }
}

void restaurantesConsulta(restaurante dados_restaurante[],int qtd_total_restaurantes){

    int i = 0;
    int encontrou_dados=0;
    int opc_consulta = 0;
    int codigo_restaurante = 0;
    char cnpj_restaurante[20];
    char nome_restaurante[50];
    char cidade_restaurante[20];

    printf("CONSULTA BASE RESTAURANTES.\n Opcoes:\n 1 - Consulta por codigo restaurante 2 - consulta por nome 3 - consulta CNPJ 4 - consulta por cidade\n opcao:");
    scanf("%i",&opc_consulta);

    if(opc_consulta==1){
        printf("digite o codigo do restaurante:\n");
        scanf("%i",&codigo_restaurante);
        for(i;i<qtd_total_restaurantes;i++){
            if(dados_restaurante[i].cod_restaurante == codigo_restaurante){
                printf("---------------------\n");
                printf("RESTAURANTE\ncodigo:%i\n",dados_restaurante[i].cod_restaurante);
                printf("Nome:%s\n",dados_restaurante[i].nome);
                printf("Cnpj:%s\n",dados_restaurante[i].cnpj);
                printf("Cidade:%s\n",dados_restaurante[i].cidade);
                printf("Email:%s\n",dados_restaurante[i].email);
                printf("Telefone:%s\n",dados_restaurante[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==2){
        printf("digite o nome do restaurante:\n");
        scanf(" %[^\n]s",nome_restaurante);
        for(i;i<qtd_total_restaurantes;i++){
            if(strcmp(dados_restaurante[i].nome,nome_restaurante)== 0){
                printf("---------------------\n");
                printf("RESTAURANTE\ncodigo:%i\n",dados_restaurante[i].cod_restaurante);
                printf("Nome:%s\n",dados_restaurante[i].nome);
                printf("Cnpj:%s\n",dados_restaurante[i].cnpj);
                printf("Cidade:%s\n",dados_restaurante[i].cidade);
                printf("Email:%s\n",dados_restaurante[i].email);
                printf("Telefone:%s\n",dados_restaurante[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==3){
        printf("digite o cnpj do restaurante:\n");
        scanf(" %s",cnpj_restaurante);
        for(i;i<qtd_total_restaurantes;i++){
            if(strcmp(dados_restaurante[i].cnpj,cnpj_restaurante)== 0){
                printf("---------------------\n");
                printf("RESTAURANTE\ncodigo:%i\n",dados_restaurante[i].cod_restaurante);
                printf("Nome:%s\n",dados_restaurante[i].nome);
                printf("Cnpj:%s\n",dados_restaurante[i].cnpj);
                printf("Cidade:%s\n",dados_restaurante[i].cidade);
                printf("Email:%s\n",dados_restaurante[i].email);
                printf("Telefone:%s\n",dados_restaurante[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==4){
        printf("digite a cidade restaurante:\n");
        scanf(" %s",cidade_restaurante);
        for(i;i<qtd_total_restaurantes;i++){
            if(strcmp(dados_restaurante[i].cidade,cidade_restaurante)== 0){
                printf("---------------------\n");
                printf("RESTAURANTE\ncodigo:%i\n",dados_restaurante[i].cod_restaurante);
                printf("Nome:%s\n",dados_restaurante[i].nome);
                printf("Cnpj:%s\n",dados_restaurante[i].cnpj);
                printf("Cidade:%s\n",dados_restaurante[i].cidade);
                printf("Email:%s\n",dados_restaurante[i].email);
                printf("Telefone:%s\n",dados_restaurante[i].telefone);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else{
        printf("opção invalida");
        return;
    }
}

void pedidosConsulta(pedido dados_pedidos[],int qtd_total_pedidos){

    int i = 0;
    int encontrou_dados=0;
    int opc_consulta = 0;
    int codigo_restaurante = 0;
    int codigo_pedido = 0;
    int codigo_cliente = 0;
    char forma_pagamento[2][20] = {"dinheiro","cartao credito","cartao dinheiro"};

    printf("CONSULTA BASE PEDIDOS.\n Opcoes:\n 1 - Consulta por codigo pedido 2 - consulta por codigo restaurante 3 - consulta codigo cliente 4 - consulta por forma de pagamento\n opcao:");
    scanf("%i",&opc_consulta);

    if(opc_consulta==1){
        printf("digite o codigo do pedido:\n");
        scanf("%i",&codigo_pedido);
        for(i;i<qtd_total_pedidos;i++){
            if(dados_pedidos[i].cod_pedido == codigo_pedido){
                printf("---------------------\n");
                printf("PEDIDO\ncodigo:%i\n",dados_pedidos[i].cod_pedido);
                printf("codigo cliente:%i\n",dados_pedidos[i].cod_cliente);
                printf("codigo restaurante:%i\n",dados_pedidos[i].cod_restaurante);
                printf("descricao:%s\n",dados_pedidos[i].descricao);
                printf("forma de pagamento:%s\n",dados_pedidos[i].forma_pagamento);
                printf("valor:%.2f\n",dados_pedidos[i].valor);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==2){
        printf("digite o codigo do restaurante:\n");
        scanf("%i",&codigo_restaurante);
        for(i;i<qtd_total_pedidos;i++){
            if(dados_pedidos[i].cod_restaurante==codigo_restaurante){
                printf("---------------------\n");
                printf("PEDIDO\ncodigo:%i\n",dados_pedidos[i].cod_pedido);
                printf("codigo cliente:%i\n",dados_pedidos[i].cod_cliente);
                printf("codigo restaurante:%i\n",dados_pedidos[i].cod_restaurante);
                printf("descricao:%s\n",dados_pedidos[i].descricao);
                printf("forma de pagamento:%s\n",dados_pedidos[i].forma_pagamento);
                printf("valor:%.2f\n",dados_pedidos[i].valor);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==3){
        printf("digite o codigo do cliente:\n");
        scanf("%i",&codigo_cliente);
        for(i;i<qtd_total_pedidos;i++){
            if(dados_pedidos[i].cod_cliente==codigo_cliente){
                printf("---------------------\n");
                printf("PEDIDO\ncodigo:%i\n",dados_pedidos[i].cod_pedido);
                printf("codigo cliente:%i\n",dados_pedidos[i].cod_cliente);
                printf("codigo restaurante:%i\n",dados_pedidos[i].cod_restaurante);
                printf("descricao:%s\n",dados_pedidos[i].descricao);
                printf("forma de pagamento:%s\n",dados_pedidos[i].forma_pagamento);
                printf("valor:%.2f\n",dados_pedidos[i].valor);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else if(opc_consulta==4){
        printf("digite a forma de pagamento:[0] dinheiro [1] cartao credito [2] cartao debito\n");
        scanf("%i",&opc_consulta);
        for(i;i<qtd_total_pedidos;i++){
            if(strcmp(dados_pedidos[i].forma_pagamento,forma_pagamento[opc_consulta])== 0){
                printf("---------------------\n");
                printf("PEDIDO\ncodigo:%i\n",dados_pedidos[i].cod_pedido);
                printf("codigo cliente:%i\n",dados_pedidos[i].cod_cliente);
                printf("codigo restaurante:%i\n",dados_pedidos[i].cod_restaurante);
                printf("descricao:%s\n",dados_pedidos[i].descricao);
                printf("forma de pagamento:%s\n",dados_pedidos[i].forma_pagamento);
                printf("valor:%.2f\n",dados_pedidos[i].valor);
                printf("---------------------\n");
                encontrou_dados=1;
            }
        }
        if(encontrou_dados==0){printf("sem dados encontrados\n");}
        return;
    }else{
        printf("opção invalida");
        return;
    }

}

void main()
{
int valor_tabelas;
int qtd_novos_clientes;
int qtd_novos_restaurantes;
int qtd_novos_pedidos;
int qtd_total_cliente = 0;
int qtd_total_restaurantes = 0;
int qtd_total_pedidos = 0;
int menu;
int x,i=0;

printf("Digite a seguir o valor de cadastros maximos para o sistema, o numero digitado\n\
sera o limite para todas as tabelas (clientes,restaurantes,pedidos).\nValor:");
scanf("%i",&valor_tabelas);

cliente dados_clientes[valor_tabelas];
restaurante dados_restaurantes[valor_tabelas];
pedido dados_pedidos[valor_tabelas];

do{
    printf("MENU\n 1 - CADASTRAR CLIENTES \n 2 - CADASTRAR RESTAURANTES \n 3 - CADASTRAR PEDIDOS \n 4 - CONSULTA CLIENTES \n 5 - CONSULTA RESTAURANTES \n 6 - CONSULTA PEDIDO \n 0 - SAIR\n Opcao:");
    scanf("%i",&menu);
    switch(menu){
        case 1:
            printf("Digite a quantidade de clientes a serem cadastrados:\n");
            scanf("%i",&qtd_novos_clientes);
            qtd_total_cliente = clientesCadastro(dados_clientes,qtd_novos_clientes,qtd_total_cliente);
            printf("o numero total de clientes cadastrados foi atualizado para: %i\n",qtd_total_cliente);
            break;
        case 2:
            printf("Digite a quantidade de restaurantes a serem cadastrados:\n");
            scanf("%i",&qtd_novos_restaurantes);
            qtd_total_restaurantes = restaurantesCadastro(dados_restaurantes,qtd_novos_restaurantes,qtd_total_restaurantes);
            printf("o numero total de restaurantes cadastrados foi atualizado para: %i\n",qtd_total_restaurantes);
            break;
        case 3:
            printf("Digite a quantidade de pedidos a serem cadastrados:\n");
            scanf("%i",&qtd_novos_pedidos);
            qtd_total_pedidos = pedidosCadastro(dados_pedidos,qtd_novos_pedidos,qtd_total_pedidos,dados_clientes,qtd_total_cliente,dados_restaurantes,qtd_total_restaurantes);
            printf("o numero total de pedidos cadastrados foi atualizado para: %i\n",qtd_total_pedidos);
            break;
        case 4:
            clientesConsulta(dados_clientes,qtd_total_cliente);
            break;
        case 5:
            restaurantesConsulta(dados_restaurantes,qtd_total_restaurantes);
            break;
        case 6:
            pedidosConsulta(dados_pedidos,qtd_novos_pedidos);
            break;
        default:
            printf("opcao invalida\n");

    }
       printf("==========================================================\n");
    if(menu==0){break;}

}while(menu != 0);

    return;
}
