grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : global_dec* function_dec* EOF ;

// global_dec
global_dec: variable_dec+;

variable_dec: VAR COLON variable_list SEMI;

variable_list: variable (COMMA variable)*;

variable: (scalar (EQ lit_type)?) | (composite (EQ array_literal)?);

scalar: ID;

composite: ID (LSB INTEGER_LITERAL RSB)+;

literal: lit_type | array_literal;


// function_dec
function_dec:
FUCNTION COLON ID
    (PARAMETER COLON parameter_list)?
    BODY COLON
        variable_declaration_stmt*
        statement_list*
    ENDBODY DOT ;


parameter_list: parameter (COMMA parameter)*;

parameter: scalar | composite;

// Statement
statement_list:
                    assignment_stmt
                    | if_stmt
                    | for_stmt
                    | while_stmt
                    | do_while_stmt
                    | break_stmt
                    | continue_stmt
                    | call_stmt
                    | return_stmt ;
variable_declaration_stmt: variable_dec;

//assignment_stmt: (scalar | composite_extend) EQ expression SEMI;
assignment_stmt: ((ID | ID LP (expression (COMMA expression)*)? RP) (LSB expression RSB)+ | ID ) EQ expression SEMI;

composite_extend:ID (LSB expression RSB)+;

if_stmt: IF expression THEN variable_declaration_stmt* statement_list*
         (ELSEIF expression THEN variable_declaration_stmt* statement_list*)*
         (ELSE variable_declaration_stmt* statement_list*)?
         ENDIF DOT;

for_stmt: FOR LP scalar EQ expression COMMA expression COMMA expression RP DO
                variable_declaration_stmt* statement_list*
          ENDFOR DOT;

while_stmt: WHILE expression DO variable_declaration_stmt* statement_list* ENDWHILE DOT;

do_while_stmt: DO variable_declaration_stmt* statement_list* WHILE expression ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

//CHECK CAREFULLY
// expression | composite  | function_call
call_stmt: ID LP (expression  (COMMA expression)*)? RP SEMI;

return_stmt: RETURN expression? SEMI;

// Expression
expression:  exp1
(EQUAL_OP | DIFF_OP | LT | GT | LTE | GTE | DIV_FRAC | LT_F | GT_F | LTE_F | GTE_F)
exp1 | exp1;

exp1: exp1 (AND_OP | OR_OP) exp2 | exp2;

exp2: exp2 (ADD | ADD_F | SUB | SUB_F) exp3 | exp3;

exp3: exp3 (MUL | MUL_F | DIV | DIV_F | MOD) exp4 | exp4 ;

exp4:  (NOT) exp4 | exp5;

exp5: (SUB | SUB_F) exp5 | exp6;

// CHECK Integer or expression ?
//exp6: exp6 (LSB expression RSB)+ | exp7 ;
exp6: (ID | ID LP (expression (COMMA expression)*)? RP) (LSB expression RSB)+ | exp7;
//CHECK
exp7:  ID LP (expression (COMMA expression)*)? RP | operands;

operands:     literal
            | parameter
            | ID LP (expression  (COMMA expression)*)? RP
            | LP expression RP;

ID: [a-z][_a-zA-Z0-9]* ;




// skip comment
BLOCK_COMMENT: '**' .*? '**' -> skip ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/* Reference Document:
1. http://0x100.club/projects/antlr-example.html
2. https://xuanthulab.net/bieu-thuc-chinh-quy-regexp.html
3. https://stackoverflow.com/questions/17844248/when-is-eof-needed-in-antlr-4#:~:text=If%20you%20do%20not%20include,means%20avoiding%20a%20syntax%20error.&text=For%20rules%20where%20you%20are,often%20works%2C%20but%20not%20always.

*/

/* ********************LITERAL**************************** */
/*
    Literal type: integer, boolean, float, string, array
    Integer: INTEGER_LITERAL
             INT_LIT_BASE10 : base 10 - Decimal
             INT_LIT_BASE16 : base 16 - Hexadecimal
             INT_LIT_BASE8  : base 8  - Octal
    Float:  FLOAT_LITERAL
            EXPONENT: exponent part
            DIGIT   : decimal part
            INT_LIT_BASE10 : integer part
    String: STRING_LITERAL
            STR_CHAR: String character
            ESC_SEQ : Escape Sequence - Visible
    Boolean: BOOLEAN_LITERAL
    Array:   ARRAY_LITERAL:
                ****** One-dimensional array
                        INT_COMMA_SEPARATED_LIST
                        STR_COMMA_SEPARATED_LIST
                        BOOL_COMMA_SEPARATED_LIST
                        FLOAT_COMMA_SEPARATED_LIST
                ******* Multi-dimensional array
                ARRAY_LITERAL
                GENERAL_TYPE : A GENERAL_TYPE can be either a nested array/struct or some optional type.

*/


fragment INT_LIT_BASE10: ('0'|[1-9][0-9]*);
fragment INT_LIT_BASE16: ('0x'[1-9A-F][0-9A-F]*) |('0X'[1-9A-F][0-9A-F]*);
fragment INT_LIT_BASE8:  ('0o'[1-7][0-7]*) | ('0O'[1-7][0-7]*);
//fragment INT_LIT_BASE16: ('0x'('0'|[1-9A-F][0-9A-F]*)) |('0X'('0'|[1-9A-F][0-9A-F]*));
//fragment INT_LIT_BASE8:  ('0o'('0'|[1-7][0-7]*)) | ('0O'('0'|[1-7][0-7]*));

// Integer Literal
INTEGER_LITERAL: INT_LIT_BASE10|INT_LIT_BASE16|INT_LIT_BASE8;





fragment EXPONENT: [Ee] SIGN? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];

//Float literal
//FLOAT_LITERAL
//                :   INT_LIT_BASE10 EXPONENT
//                |   INT_LIT_BASE10 DOT (DIGIT+)? EXPONENT?
//                ;
FLOAT_LITERAL
                :   DIGIT+ EXPONENT
                |   DIGIT+ DOT (DIGIT+)? EXPONENT?
                ;

BOOLEAN_LITERAL: TRUE | FALSE;

/*
fragment INT_COMMA_SEPARATED_LIST:
                LCB WHITESPACE* INT_LIT_BASE10 (WHITESPACE* COMMA WHITESPACE* INT_LIT_BASE10)* WHITESPACE* RCB;
fragment STR_COMMA_SEPARATED_LIST:
                LCB WHITESPACE* STRING_LITERAL (WHITESPACE* COMMA WHITESPACE* STRING_LITERAL)* WHITESPACE* RCB;
fragment BOOL_COMMA_SEPARATED_LIST:
                LCB WHITESPACE* BOOLEAN_LITERAL (WHITESPACE* COMMA WHITESPACE* BOOLEAN_LITERAL)* WHITESPACE* RCB;
fragment FLOAT_COMMA_SEPARATED_LIST:
                LCB WHITESPACE* FLOAT_LITERAL (WHITESPACE* COMMA WHITESPACE* FLOAT_LITERAL)* WHITESPACE* RCB;
*/
array_literal:
                LCB  general_type? (COMMA  general_type)* RCB;

general_type: array_literal
                        | lit_type;
lit_type: INTEGER_LITERAL
                        | STRING_LITERAL
                        | BOOLEAN_LITERAL
                        | FLOAT_LITERAL
                        ;
/* ************************************************ */



/* ***********************KEYWORD************************* */
BODY:           'Body';
BREAK:          'Break';
CONTINUE:       'Continue';
DO:             'Do';
ELSE:           'Else';
ELSEIF:         'ElseIf';
ENDBODY:        'EndBody';
ENDIF:          'EndIf';
ENDFOR:         'EndFor';
ENDWHILE:       'EndWhile';
FOR:            'For';
FUCNTION:       'Function';
IF:             'If';
PARAMETER:      'Parameter';
RETURN:         'Return';
THEN:           'Then';
VAR:            'Var';
WHILE:          'While';
TRUE:           'True';
FALSE:          'False';
ENDDO:          'EndDo';



/* ************************************************ */


/* **********************OPERATOR************************** */
ADD:        '+'     ;
ADD_F:      '+.'    ;
SUB:        '-'     ;
SUB_F:      '-.'    ;
MUL:        '*'     ;
MUL_F:      '*.'    ;
DIV:        '\\'     ;
DIV_F:      '\\.'    ;
MOD:        '%'     ;
NOT:        '!'     ;
AND_OP:     '&&'    ;
OR_OP:      '||'    ;
EQUAL_OP:   '=='    ;
DIFF_OP:    '!='    ;
LT:         '<'     ;
GT:         '>'     ;
LTE:        '<='    ;
GTE:        '>='    ;
DIV_FRAC:   '=/='   ;
LT_F:       '<.'    ;
GT_F:       '>.'    ;
LTE_F:      '<=.'   ;
GTE_F:      '>=.'   ;
EQ:         '='     ;






/* ************************************************ */


/* **********************SEPARATOR************************** */

DOT:        '.';
COMMA:      ',';        // Comma
LP:         '(';        // Left Parenthesis
RP:         ')';        // Right Parenthesis
SEMI:       ';';        // Semicolon
COLON:      ':';        // Colon
LSB:        '[';        // Left Square Bracket
RSB:        ']';        // Right Square Bracket
LCB:        '{';        // Left Curly Bracket
RCB:        '}';        // Right Curly Bracket


/* ************************************************ */


/* ********************KEYWORD**************************** */



/* ************************************************ */

/* ********************UTILITY**************************** */
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~["];
fragment STR_CHAR: '\'"' | ~[\n"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfnrt'\\];
/* ************************************************ */


ERROR_CHAR: .;
// Unclose string có th? có \n ? cu?i ?
UNCLOSE_STRING: '"' STR_CHAR* ([\n] | EOF){
if self.text[-1] != '\n':
    self.text = self.text[1:]
else:
    self.text = self.text[1:-1]
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL STR_CHAR* '"'
{
num = [m for m, c in enumerate(self.text) if c == '\\' or c == '\'']
for ch in num:
    if (self.text[ch] == '\\') and (self.text[ch + 1] not in ['b','t','n','f','r','\'','\\']):
        self.text = self.text[1: (ch+2)]
        break
    elif (self.text[ch] == '\'') and (self.text[ch + 1] != '\"'):
        self.text = self.text[1: (ch+2)]
        break
};
UNTERMINATED_COMMENT: '**' .*? ([^*]'*'| '*'[^*])?;
//String Literal
STRING_LITERAL: '"'STR_CHAR*'"' {self.text = self.text[1:-1]};

