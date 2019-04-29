%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *);
int yylex();
%}

%token UPDATE SET WHERE AND OR NTEQ EQ LT LTEQ GT GTEQ ID INT
%%

S1 : S	{ printf("Input accepted.\n"); exit(0); }

S : 	UPDATE ID SET E3 WHERE C

A : 	ID
B : 	ID
	| INT

E3 :	E1

E1 :	A '=' B

C :	C1

C1 : 	A O B

O :	'='
	| LT
	| GT
	| LTEQ
	| GTEQ
	| NTEQ 


%%

#include "lex.yy.c"

void yyerror(char *s)
{
	printf("ErrorP");
}

int main()
{
	printf("Enter your expression : ");
	yyparse();
	return 0;
}

