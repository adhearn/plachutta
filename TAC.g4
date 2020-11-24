grammar TAC;

tacFile: tacLine+ ;
tacLine: labeledInstruction '\n' ;

labeledInstruction: (label ':')* instruction ;

instruction: '<NO OP>' # NoOp
| lhs '=' rhs # Assignment
| 'if' relop jump # ConditionalJump
| jump # UnconditionalJump
;

jump: 'jump' label ;

label: ID ;

lhs: address ;

rhs: address # RhsAddress
| address binoperator address # RhsBinop
;

relop: address reloperator address ;

binoperator: '*' | '+' | '-' ;

reloperator: '==' | '!=' | '>' | '>=' | '<=' | '<' ;

address: ID # Identifier
| INT # Integer
;

ID: [a-z][a-zA-Z0-9]* ;
INT: [0-9]+ ;

WS: [ \t] -> skip ;