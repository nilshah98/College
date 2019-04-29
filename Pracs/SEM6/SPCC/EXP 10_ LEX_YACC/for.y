%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *);
int yylex();
%}

%token WHILE AND OR NTEQ EQ LT LTEQ GT GTEQ ID INT
%%

S1 : S	{ printf("Input accepted.\n"); exit(0); }

S : WHILE '(' C ')' '{' E '}'

C :	A LT B
	| A GT B
	| A OR B
	| A AND B
	| A NTEQ B
	| A EQ B
	| A LTEQ B
	| A GTEQ B

A : 	ID
B : 	ID
	| INT

E :	E1 ';' E | E1 ';'

E1 : 	A '=' E2

E2 :	B '+' B
	| B '*' B
	| B '/' B
	| B '-' B
	| B

%%

void yyerror(char *s)
{
	printf("Error");
}

int main()
{
	printf("Enter your expression : ");
	yyparse();
	return 0;
}

