grammar TAC;

tacFile: tacLine+ ;
tacLine: labeledInstruction '\n' ;

labeledInstruction: (label ':')* instruction ;

instruction: '<NO OP>' # NoOp
| lhs '=' rhs # Assignment
| 'if' relop jump # ConditionalJump
| 'return' address # InstructionReturn
| 'param' address # InstructionParam
| jump # UnconditionalJump
;

jump: 'jump' label ;

label: LABEL ;

lhs: address # LhsSimple
| address '[' address ']' # LhsIndexed
;

rhs: 'call' label address # RhsCall
| address # RhsAddress
| address binoperator address # RhsBinop
| unoperator address # RhsUnop
| address '[' address ']' # RhsIndexed
//| '&' ID # RhsAddressOf
;

relop: address reloperator address ;

binoperator: '*' | '+' | '-' ;

reloperator: '==' | '!=' | '>' | '>=' | '<=' | '<' ;

unoperator: 'memrequest'
| 'param'
;

address: GLOBAL # AddressGlobal
| LOCAL # AddressLocal
| INT # AddressInteger
;

LOCAL: '%'ID ;
LABEL: '@'ID ;
GLOBAL: '$'ID ;
ID: [a-z][a-zA-Z0-9]* ;
INT: [0-9]+ ;

WS: [ \t] -> skip ;