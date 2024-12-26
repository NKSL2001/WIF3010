grammar TypeChecker;
Whitespace: [ \t\r\n] -> skip;

program          : statement*;
statement        : variableDeclaration | assignment | showStatement | classDeclaration | templateDeclaration ;
showStatement    : 'show' expression '!' ;
returnStatement  : 'return' expression '!' ;
createClassStatement  : 'new' className parametersCall ;

variableSignature : type variableName ;
variableDeclaration : variableSignature ':=' (expression | createClassStatement ) '!' ;
assignment       : variableName ':=' (expression | createClassStatement ) '!' ;

parametersInit : '(' ( type variableName ( ',' type variableName )* | ) ')';
methodSignature   : 'method' type methodName parametersInit;
methodDeclaration : methodSignature methodBlock ;
methodBlock      : '{' ( statement )* ( returnStatement | ) '}' ;

classDeclaration : 'class' className ('inherit' className | )  '{' 
                     ( variableSignature '!' )*
                     ( variableDeclaration )*
                     ( methodDeclaration )*
                     '}' ;
templateDeclaration : 'template' className  '{' 
                     ( variableSignature '!' )*
                     ( methodSignature '!' )*
                     '}' ;

parametersCall : '(' ( expression ( ',' expression )* | ) ')';
classVariableAccess : (className | variableName) '.' variableName;
classMethodAccess : (className | variableName) '.' methodName parametersCall;

expression       : additiveExpression;
/* for operation precedence */
additiveExpression : multiplicativeExpression (('+' | '-') multiplicativeExpression)*;
multiplicativeExpression : term  ( ('*' | '/' ) term )*;
term             : variableName | literal | classVariableAccess | classMethodAccess | '(' expression ')' ;

type             : 'chunk' | 'fraction' | 'string' | 'none' | className ;
variableName     : '$' identifier ;
className        : identifier ;
methodName       : identifier ;
identifier       : Letter ( Letter | Digit | '_' )* ;
literal          : ChunkLiteral | FractionLiteral | StringLiteral ;
ChunkLiteral     : NonZeroDigit ( Digit )* ;
FractionLiteral  : ChunkLiteral '.' ( Digit )* ;
StringLiteral    : '"' ( CharacterExceptQuote )* '"' ;

Letter           : 'A'..'Z' | 'a'..'z' ;
NonZeroDigit     : '1'..'9' ;
Digit            : '0' | NonZeroDigit;
CharacterExceptQuote : '\u0020' | '\u0021' | '\u0023'..'\u007F' ;
Character : CharacterExceptQuote | '"';

/* skipped items */
BlockComment
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;
LineComment
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;