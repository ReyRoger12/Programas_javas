%%
%class Lexer
%unicode
%cup
%line
%column

%{
  import java_cup.runtime.Symbol;
%}

%%

[ \t\r\n]+                { /* Ignorar espacios */ }
"("                      { return new Symbol(sym.PARENIZQ); }
")"                      { return new Symbol(sym.PARENDER); }
[\+\-\*/]                { return new Symbol(sym.OPERADOR); }
[0-9]+\.[0-9]+           { return new Symbol(sym.FLOTANTE, Double.parseDouble(yytext())); }
[0-9]+                   { return new Symbol(sym.ENTERO, Integer.parseInt(yytext())); }
E[\+\-]?[0-9]{1,2}       { return new Symbol(sym.EXPONENTE, yytext()); }

.                        { System.err.println("Carácter ilegal: " + yytext()); return null; }
