%{
    #include "y.tab.h"
    void yyerror(char *);
%}

DIGIT [0-9]
LETTER [a-zA-Z]
ID {LETTER}({LETTER}|{DIGIT})*

%%

[ \t\n]+ ;

"select" { return SELECT;}
"from" {return FROM;}

{ID} {return ID;}
{DIGIT}+ {return INT;}

[=+-/*{}();]	{return *yytext;}

.	{ printf("Error"); }

%%
