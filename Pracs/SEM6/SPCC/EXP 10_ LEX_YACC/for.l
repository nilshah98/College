%{
	#include "y.tab.h"
	void yyerror(char *);
%}

DIGIT [0-9]
LETTER [a-zA-Z]
ID {LETTER}({LETTER}|{DIGIT})*

%%

[ \t\n]+ ;

"while"	{ return WHILE; }

{ID}	{ return ID; }
{DIGIT}+	{ return INT; }

[=+-/*{}();]	{return *yytext;}

"&&"	{ return AND; }
"||"	{ return OR; }
"!="	{ return NTEQ; }
"=="	{ return EQ; }
"<" 	{ return LT; }
"<="	{ return LTEQ; }
">"	{ return GT; }
">="	{ return GTEQ; }


.	{ printf("Error"); }

%%


