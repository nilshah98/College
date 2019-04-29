%{
    #include<stdio.h>
    #include<stdlib.h>
    void yyerror(char *);
    int yylex();
%}

%token SELECT FROM ID INT
%%

S1 : S { printf("Input accepted \n"); exit(0); }

S : SELECT A FROM B

A : ID
    | '*'

B : ID

%%

void yyerror(char *s)
{
    printf("Error\n");
}

int main()
{
    printf("Enter your expression:");
    yyparse();
    return 0;
}