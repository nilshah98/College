%{
	void yyerror(char *);
%}

DIGIT [0-9]
LETTER [a-zA-Z_]
ID {LETTER}({LETTER}|{DIGIT})*

%%

[ \t\n]+ 

"update"	{ return UPDATE; }
"set"	{ return SET; }
"where"	{ return WHERE; }

{ID}	{ return ID; }
{DIGIT}+	{ return INT; }

[=+-/*;s]	{return *yytext;}

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


