
"""
 * @author nhphung
"""

from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    def __str__(self):
        return "IntType"
class FloatType(Prim):
    def __str__(self):
        return "FloatType"
class StringType(Prim):
    def __str__(self):
        return "StringType"
class BoolType(Prim):
    def __str__(self):
        return "BoolType"
class VoidType(Type):
        def __str__(self):
            return "VoidType"
class Unknown(Type):
    def __str__(self):
        return "Unknown"

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

    def __str__(self):
        return "ArrayType(" + str(self.eletype) +"," + str(self.dimen) + ")"

@dataclass
class MType:
    intype:List[Type]
    restype:Type

    def __init__(self, intype, restype):
        self.intype = intype
        self.restype = restype

    def __str__(self):
        return 'Mtype([' + ','.join([str(i) for i in self.intype]) + '],' + str(self.restype) + ')'

    def setInOutType(self, intType, resType):
        self.intype = intType
        self.restype = resType
        return self

    def setIntType(self, index, typ):
        self.intype[index] = typ
        return self

@dataclass
class Symbol:
    """
        name: string
        mtype:Type : MType, ArrayType, PrimitiveType: IntType | FloatType | StringType | BoolType
        value: ?
        kind: Function(), Parameter(), Variable()
        isGlobal: boolean
    """
    def __init__(self, name, mtype, value = None, kind=Function(), isGlobal= False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ',' + str(self.kind) + ')'

    def toGlobal(self):
        self.isGlobal = True
        return self

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self

    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    def toTuple(self):
        return (self.name, type(self.getKind()))

    def toType(self, type):
        self.mtype = type
        return self

    #Static method
    @staticmethod
    def cmp(symbol):
        return symbol.name


    @staticmethod
    def fromVarDecl(decl):
        name = decl.variable.name
        info = decl.varInit if decl.varInit else None
        mtype = None
        value = None
        dimension = decl.varDimen
        if info:
            if type(info) is IntLiteral:
                mtype = IntType()
                value = info.value
            elif type(info) is FloatLiteral:
                mtype = FloatType()
                value = info.value
            elif type(info) is StringLiteral:
                mtype = StringType()
                value = info.value
            elif type(info) is BooleanLiteral:
                mtype = BoolType()
                value = info.value
            elif type(info) is ArrayLiteral:
                result, classType = Checker.checkValidArray(info)
                # dimension = decl.varDimen
                #dimension = Utils.getDimensionOfArray(info, dimension)
                eletype = None
                if classType is IntLiteral:
                    eletype = IntType()
                elif classType is FloatLiteral:
                    eletype = FloatType()
                elif classType is StringLiteral:
                    eletype = StringType()
                elif classType is BooleanLiteral:
                    eletype = BoolType()


                mtype = ArrayType(dimension, eletype)
                value = info.value
        else:
            if decl.varDimen:
                # dimension = decl.varDimen
                mtype = ArrayType(dimension, eletype=None)
                value = None



        return Symbol(name, mtype, value, kind = Variable())




    @staticmethod
    def fromFuncDecl(decl):
        name = decl.name.name
        paramType = [Symbol.fromVarDecl(x).mtype for x in decl.param]
        return Symbol(name, MType(paramType, None))

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

class Scope:
    @staticmethod
    def start(section):
        print("=======================" + section + "=======================")

    @staticmethod
    def end():
        print("=============================================================")

    @staticmethod
    def isExist(listSymbols, symbol):
        return len([x for x in listSymbols if x.name == symbol.name]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        return reduce(lambda lst,sym: lst if Scope.isExist(lst, sym) else lst + [sym],currentScope, comingScope)

class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    # @staticmethod
    # def getType(operation):
    #     if operation in ['-', '+', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
    #         return IntType
    #     elif operation in ['-.', '+.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.']:
    #         return FloatType
    #     elif operation in ['!', '&&', '||']:
    #         return BoolType

    @staticmethod
    def getDimensionOfArray(arrayLit, dimen):
        while (type(arrayLit) is ArrayLiteral and type(arrayLit.value[0]) is ArrayLiteral):
            dimen.append(len(arrayLit.value))
            arrayLit = arrayLit.value[0]
        dimen.append(len(arrayLit.value))
        return dimen

    @staticmethod
    def getTypeFromOperation(operation):
        if operation in ['-', '+', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']:
            return IntType()
        elif operation in ['-.', '+.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.']:
            return FloatType()
        elif operation in ['!', '&&', '||']:
            return BoolType()





class Checker:

    utils = Utils()

    @staticmethod
    def checkRedeclared(currentScope, listNewSymbols):
        newScope = currentScope.copy()

        for x in listNewSymbols:
            f = Checker.utils.lookup(Symbol.cmp(x), newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope

    @staticmethod
    def isTypeUnresolved(symbol):
        if len(symbol.mtype.intype) == 0:
            return True

        return all([x[1] is not None for x in symbol.mtype.intype])

    @staticmethod
    def checkUndeclared(visibleScope, name, kind, notGlobal=False):
        # Return Symbol declared in scope
        scope = visibleScope if not notGlobal else [x for x in visibleScope if not x.isGlobal]
        res = Checker.utils.lookup((name, type(kind)), scope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res

    @staticmethod
    def checkValidArray(arrayLit):
        if arrayLit.value:
            first = arrayLit.value[0]
            if (str(first).partition('('))[0] in ["IntLiteral", "FloatLiteral", "StringLiteral", "BooleanLiteral"]:
                ret = all([type(x) is type(first) for x in arrayLit.value])
                if not ret:
                    raise InvalidArrayLiteral(arrayLit)
                #Change type-> object
                return True, type(first)
            else:
                result = []
                comp = Checker.checkValidArray(arrayLit.value[0])
                for x in arrayLit.value:
                    result.append(Checker.checkValidArray(x)[0] and Checker.checkValidArray(x)[1] is comp[1])
                if all(result):
                    for ele in arrayLit.value:
                        if len(ele.value) != len(arrayLit.value[0].value):
                            raise InvalidArrayLiteral(arrayLit)
                    return True, comp[1]
                else:
                    raise InvalidArrayLiteral(arrayLit)
        else:
            raise InvalidArrayLiteral(arrayLit)

    @staticmethod
    def CheckAndCaculateValue(index):
        if type(index) is IntLiteral:
            return True

        elif type(index) is BinaryOp:
            if index.op not in ['-', '+', '*', '\\', '%']:
                return False

            return (Checker.CheckAndCaculateValue(index.left) and (Checker.CheckAndCaculateValue(index.right)))
        elif type(index) is UnaryOp:
            if index.op not in ['-']:
                return False

            return Checker.CheckAndCaculateValue(index.body)
        else:
            return False
    @staticmethod
    def getValueOfExp(index):
        if type(index) is IntLiteral:
            return int(index.value)
        elif type(index) is BinaryOp:
            op = index.op
            if op == '\\':
                op = '/'
            return int(eval(str(Checker.getValueOfExp(index.left)) + op + str(Checker.getValueOfExp(index.right))))
        elif type(index) is UnaryOp:
            return int(eval(str(index.op) + str(Checker.getValueOfExp(index.body))))

    @staticmethod
    def handleReturnStmts(stmts):
        # stmts: (stmt, type) with type: None, VoidType, (...)Type, Break
        for i in range(0, len(stmts) - 1):
            if Checker.isStopTypeStatment(stmts[i][1]):
                raise UnreachableStatement(stmts[i + 1][0])
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isReturnTypeFunction(retType):
        return type(retType) in [IntType, FloatType, BoolType, StringType, ArrayType, VoidType]

    @staticmethod
    def isReturnType(retType):
        return Checker.isReturnTypeFunction(retType)

    @staticmethod
    def isStopTypeStatment(retType):
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]



# Graph for Call Statements and Call Expression between Functions
class Graph:

    link = {} # { 'n1': ['n2', 'n3'], 'n2': [], 'n3': ['n1', 'n2'] }
    visited = {} # { 'n1': True, 'n2': False, 'n3': False }
    invoked = {} # { 'n1': True, 'n2': False, 'n3': False }

    @staticmethod
    def initialize():
        Graph.link.clear()
        Graph.visited.clear()
        Graph.invoked.clear()

    @staticmethod
    def add(u, v=None): # v is None when add new node, else u call v
        u = str(u).lower()
        if type(Graph.link.get(u)) != list:
            Graph.link[u] = []
            Graph.visited[u] = False
            Graph.invoked[u] = False
        if v is None: return
        v = str(v).lower()
        if v != u and v not in Graph.link[u]:
            Graph.link[u].append(v)
            Graph.invoked[v] = True # v is invoked by u

    @staticmethod
    def log():
        print('Number of nodes in graph: ', len(Graph.link))
        print(Graph.link)
        print(Graph.visited)

    @staticmethod
    def dfs(u):
        u = str(u).lower()
        Graph.visited[u] = True
        [Graph.dfs(v) for v in Graph.link[u] if not Graph.visited[v]]

    @staticmethod
    def getUnreachableNode():
        for u in Graph.link:
            if not Graph.visited[u] and not Graph.invoked[u]:
                return u
        for u in Graph.link:
            if not Graph.visited[u]: return u
        return None

    @staticmethod
    def setDefaultVisitedNodes(listNodes):
        for u in listNodes: Graph.visited[str(u).lower()] = True




class StaticChecker(BaseVisitor):
    #Random number:
    RANDOM = 98765
    #Store the name in index of parameter of function
    storeParam = {}

    #Store the type and name of parameter of function has parameter same name as function
    storeTemp = {}

    #Support for assignment stmt
    supportAssignment = None

    #Support raise statement error
    stmtErr = None

    #Check CallExp with ArrayCell
    callArrayCell = False

    #Value of [] of arraycell
    arrayCellValue = []

    #Current ArrayCell
    #currentArrayCell = None

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType())),
        Symbol("print", MType([StringType()], VoidType()))]
        StaticChecker.callArrayCell = False
        StaticChecker.arrayCellValue = []
        #StaticChecker.currentArrayCell = None

    def check(self):
        #StaticChecker.whenInfer = True
        Graph.initialize()
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast: Program, globalEnv):
        # Scope.start("Program")
        #Check Reclared variable/function
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        scope = Checker.checkRedeclared(globalEnv, symbols)
        # for x in scope:
        #     print(x)

        # Handle main function - Entry point
        entryPoint = Symbol('main', MType([],None), kind=Function())
        res = Checker.utils.lookup(entryPoint.toTuple(), symbols, lambda x: x.toTuple())

        if res is None:
            raise NoEntryPoint()

        #Get real main symbol
        # entryPoint = Checker.checkUndeclared(symbols, 'main', kind=Function())
        # print("+++++++++++++++++++++++++++++++++++++++",entryPoint)
        # for x in ast.decl:
        #     if type(x) is FuncDecl:
        #         print(Symbol.fromFuncDecl(x))

        #Init graph for unreachable functions
        listFuncDecl = globalEnv + [Symbol.fromFuncDecl(x) for x in ast.decl if type(x) is FuncDecl]

        for x in listFuncDecl:
            Graph.add(x.name)
        Graph.setDefaultVisitedNodes([u.name for u in globalEnv])


        result = [self.visit(x, scope) for x in ast.decl]
        # for x in result[-1]:
        #     print(x)


        Graph.dfs('main')
        u = Graph.getUnreachableNode()
        if u is not None:
            symbol = Checker.utils.lookup(u, listFuncDecl, Symbol.cmp)
            raise UnreachableFunction(symbol.name)
            #print(symbol)
        # print("*************************************")
        # print(Graph.link)
        # print(Graph.visited)
        # print(Graph.invoked)
        # print("######################################")

        # Scope.end()
        return []

    def visitFuncDecl(self, ast: FuncDecl, params = None):
        # Scope.start("Function "+ast.name.name)

        scope = params
        # print("*************************************")
        # for x in scope:
        #     print(x)

        listParams = [self.visit(x, scope).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, scope).toVar() for x in ast.body[0]]

        #Store name of parameter and index:
        StaticChecker.storeParam = {}
        for i in range(len(ast.param)):
            StaticChecker.storeParam[ast.param[i].variable.name] = i

        # print(storeParam)

        listNewSymbols = listParams + listLocalVar

        #Check Redeclared parameter/variable
        localScope = Checker.checkRedeclared([], listNewSymbols)

        symbol = Checker.utils.lookup(ast.name.name, scope, Symbol.cmp)
        # print(symbol)

        #Visit statements with params: scope, retType, inLoop, funcName
        newScope = Scope.merge(scope, localScope)


        refType = None
        if symbol.mtype:
            refType = symbol.mtype.restype


        #Update parameter before go to handle next function
        lst = []
        for x in newScope:
            if type(x.kind) is Parameter:
                lst.append(x)
        index = 0
        for x in symbol.mtype.intype:
            if x:
                if not lst[index].mtype:
                    lst[index].mtype = x

        refParams = [newScope, refType, False, ast.name.name]
        stmts = [self.visit(x, refParams) for x in ast.body[1]]


        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # for x in stmts:
        #     print("Stmt", x[0])
        #     print("Type", x[1])
        #Type of return result
        retType = Checker.handleReturnStmts(stmts)

        # if not Checker.isReturnTypeFunction(retType):
        #     raise FunctionNotReturn(ast.name.name)


        if not symbol.mtype.restype:
            symbol.mtype.restype = VoidType()

        # print("Hello", symbol)
        # print("CCCCCCCCCCCC", retType, symbol.mtype.restype)
        if type(symbol.mtype.restype) is not VoidType:
            if not Checker.isReturnTypeFunction(retType):
                raise FunctionNotReturn(ast.name.name)
        # if not Checker.isReturnTypeFunction(retType):
        #     raise FunctionNotReturn(ast.name.name)

        # Scope.end()
        # print("END FUNCTION**************")
        # for x in scope:
        #     print(x)
        return scope

    def visitVarDecl(self, ast: VarDecl, params = None):
        return Symbol.fromVarDecl(ast)


    def visitAssign(self, ast:Assign, params):
        # Scope.start("Assign")
        StaticChecker.stmtErr = ast
        scope, retType, inLoop, funcName = params

        #Param: scope, funcName, listOperation   ------> Change to scope, funcName,updateParam ,listOperation
        refParams = [scope, funcName, [], []]

        # print("??", ast)

        lhsType, refParams = self.visit(ast.lhs, refParams)

        # print("zo", lhsType)
        rhsType, refParams = self.visit(ast.rhs, refParams)
        # print("Result:")




        if not lhsType:
            if not rhsType:
                # print("Error 31")
                raise TypeCannotBeInferred(ast)
            elif type(rhsType) is not ArrayType:
                if type(rhsType) is VoidType:
                    # print("Error 32")
                    raise TypeMismatchInStatement(ast)
                # print("Help 1")
                refParams[-2] = []
                refParams[-2].append(rhsType)
                _, refParams = self.visit(ast.lhs, refParams)
            else:
                if rhsType.eletype:
                    refParams[-2] = []
                    refParams[-2].append(rhsType)
                    # print("Help 2")
                    _, refParams = self.visit(ast.lhs, refParams)
                else:
                    # print("Error 33")
                    raise TypeCannotBeInferred(ast)
        elif type(lhsType) is not ArrayType:
            if type(lhsType) is VoidType:
                # print("Error 34")
                raise TypeMismatchInStatement(ast)

            if not rhsType:
                # print("Help 3")
                refParams[-2] = []
                refParams[-2].append(lhsType)
                _, refParams = self.visit(ast.rhs, refParams)
            elif type(rhsType) is not ArrayType:
                if type(rhsType) is VoidType:
                    # print("Error 35")
                    raise TypeMismatchInStatement(ast)

                if type(rhsType) is not type(lhsType):
                    # print("Error 36")
                    raise TypeMismatchInStatement(ast)
            else:
                # print("Error 37")
                raise TypeMismatchInStatement(ast)
        else:
            if not rhsType:
                if lhsType.eletype:
                    refParams[-2] = []
                    refParams[-2].append(lhsType)
                    # print("Help 4")
                    _, refParams = self.visit(ast.rhs, refParams)
                else:
                    # print("Error 38")
                    raise TypeCannotBeInferred(ast)
            elif type(rhsType) is not ArrayType:
                # print("Error 39")
                raise TypeMismatchInStatement(ast)
            else:
                #Check len and same dimension first
                first = lhsType.dimen
                second = rhsType.dimen
                if len(first) != len(second):
                    # print("Error 41")
                    raise TypeMismatchInStatement(ast)
                else:
                    if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
                        # print("Help 5")
                        pass
                    else:
                        # print("Error 42")
                        raise TypeMismatchInStatement(ast)

                if lhsType.eletype and rhsType.eletype:
                    if type(lhsType.eletype) is not type(rhsType.eletype):
                        # print("Error 40")
                        raise TypeMismatchInStatement(ast)
                elif lhsType.eletype:
                    refParams[-2] = []
                    refParams[-2].append(lhsType)
                    # print("Help 6")
                    _, refParams = self.visit(ast.rhs, refParams)
                elif rhsType.eletype:
                    refParams[-2] = []
                    refParams[-2].append(rhsType)
                    # print("Help 7")
                    _, refParams = self.visit(ast.lhs, refParams)
                else:
                    # print("Error 43")
                    raise TypeCannotBeInferred(ast)

        # for x in refParams[0]:
        #     print(x)


        # print("Info:")
        # print(StaticChecker.storeTemp)
        return [ast, None, refParams[0]]

    def visitArrayCell(self, ast: ArrayCell, params):
        # Change: add updateParam
        # print("GO there")
        scope, funcName, updateParam, listOp = params
        print(ast)
        retType = None
        # print("Good Job", type(ast.arr))
        #StaticChecker.currentArrayCell = ast
        lstCheckValid = []
        for x in ast.idx:
            if Checker.CheckAndCaculateValue(x):
                lstCheckValid.append(Checker.getValueOfExp(x))
            else:
                lstCheckValid.append(StaticChecker.RANDOM)  #Random Number

        StaticChecker.arrayCellValue = lstCheckValid
        # if listOp:
        #     print("Hello world")
        #     # retType = Utils.getTypeFromOperation(listOp[-1])
        #     # temp = listOp.copy()
        #     # params[-1] = []
        #     # if len(params[-2]) > 0:
        #     #     print("Loi cmnr")
        #     # else:
        #     #     params[-2].append(retType)
        #     # _, params = self.visit(ast, params)
        #     # params[-1] = temp
        #     retType = Utils.getTypeFromOperation(listOp[-1])
        #
        #     leftType, params = self.visit(ast.arr, params)
        #
        #     if leftType:
        #         if type(leftType) is not ArrayType:
        #             print("Error 15")
        #             raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #         else:
        #             if type(ast.arr) is Id:
        #                 print("Hello 1")
        #                 subSymbol = Checker.utils.lookup(ast.arr.name, scope, Symbol.cmp)
        #                 if type(subSymbol.mtype) is not ArrayType:
        #                     print("Error 30")
        #                     raise TypeMismatchInExpression(ast)
        #                 else:
        #                     if len(subSymbol.mtype.dimen) != len(ast.idx):
        #                         print("Error 31")
        #                         raise TypeMismatchInExpression(ast)
        #                     else:
        #                         print("Hello 2")
        #                         if subSymbol.mtype.eletype:
        #                             if type(subSymbol.mtype.eletype) is not type(retType):
        #                                 #Can raise error here?
        #                                 retType = subSymbol.mtype.eletype
        #                                 print("Error 32")
        #                         else:
        #                             print("Hello 3")
        #                             # subSymbol.mtype.eletype = retType
        #                             # print("Haha", subSymbol)
        #                             params[-2] = []
        #                             params[-2].append(ArrayType(subSymbol.mtype.dimen, retType))
        #                             _, params = self.visit(ast.arr, params)
        #             elif type(ast.arr) is CallExpr:
        #                 subSymbol = Checker.utils.lookup(ast.arr.method.name, scope, Symbol.cmp)
        #
        #                 print("HAHHA")
        #                 if len(subSymbol.mtype.dimen) != len(ast.idx):
        #                     print("Error 18")
        #                     raise TypeMismatchInExpression(ast)
        #                 else:
        #                     if subSymbol.mtype.restype:
        #                         if type(subSymbol.mtype.restype) is not type(retType):
        #                             print("Error 17")
        #                             # Can raise error here?
        #                             retType = subSymbol.mtype.restype
        #                     else:
        #                         print("Hello 5")
        #                         # subSymbol.mtype.restype = retType
        #                         params[-2] = []
        #                         params[-2].append(retType)
        #                         _, params = self.visit(ast.arr, params)
        #     else:
        #         print("Error 14")
        #         raise TypeCannotBeInferred(StaticChecker.stmtErr)
        # else:
        #     print("First", params[-2])
        #     leftType, params = self.visit(ast.arr, params)
        #     # if not updateParam:
        #     #     params[-2].append(ArrayType([3], BoolType()))
        #
        #     print("type",leftType)
        #     #Make sure params[-2][-1] has full info of type. Example, IntType, ArrayType([1,4,6,3],FloatType())
        #     if leftType:
        #         if type(leftType) is not ArrayType:
        #             print("Error 19")
        #             raise TypeMismatchInExpression(ast)
        #         else:
        #             if params[-2]:
        #                 if type(ast.arr) is Id:
        #                     print("Epsilon")
        #                     subSymbol = Checker.utils.lookup(ast.arr.name, scope, Symbol.cmp)
        #
        #                     if type(params[-2][-1]) is not ArrayType:
        #
        #                         if len(subSymbol.mtype.dimen) != len(ast.idx):
        #                             raise TypeMismatchInExpression(ast)
        #
        #                         if params[0][params[0].index(subSymbol)].mtype.eletype:
        #                             if type(params[0][params[0].index(subSymbol)].mtype.eletype) is not type(
        #                                     params[-2][-1]):
        #                                 raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #                         else:
        #                             _, params = self.visit(ast.arr, params)
        #                     else:
        #                         if len(params[-2][-1].dimen) + len(ast.idx) != len(subSymbol.mtype.dimen):
        #                             print("YEEEEEEG")
        #                             raise TypeMismatchInExpression(ast)
        #
        #                         first = subSymbol.mtype.dimen[len(ast.idx):]
        #                         print(first)
        #                         second = params[-2][-1].dimen
        #                         print(second)
        #                         if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
        #                             if params[0][params[0].index(subSymbol)].mtype.eletype:
        #                                 if type(params[0][params[0].index(subSymbol)].mtype.eletype) is not type(
        #                                         params[-2][-1].eletype):
        #                                     print("OK luon")
        #                                     raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #                             else:
        #                                 print("ep 2")
        #                                 # params[0][params[0].index(subSymbol)].mtype.eletype = params[-2][-1].eletype
        #                                 params[-2][-1].dimen = subSymbol.mtype.dimen
        #
        #                                 _, params = self.visit(ast.arr, params)
        #                         else:
        #                             raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #
        #                 elif type(ast.arr) is CallExpr:
        #                     subSymbol = Checker.utils.lookup(ast.arr.method.name, scope, Symbol.cmp)
        #
        #                     if params[-2]:
        #                         if type(params[-2][-1]) is not ArrayType:
        #                             if len(subSymbol.mtype.dimen) != len(ast.idx):
        #                                 print(8.1)
        #                                 raise TypeMismatchInExpression(ast)
        #
        #                             if subSymbol.mtype.restype:
        #                                 if type(subSymbol.mtype.restype) is not type(params[-2][-1]):
        #                                     raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #                             else:
        #                                 subSymbol.mtype.restype = params[-2][-1]
        #                                 params[-2][-1] = []
        #                         else:
        #                             if len(subSymbol.mtype.dimen) - len(ast.idx) != len(params[-2][-1].dimen):
        #                                 raise TypeMismatchInExpression(ast)
        #
        #                             first = subSymbol.mtype.dimen[len(ast.idx):]
        #                             second = params[-2][-1].dimen
        #
        #                             if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
        #                                 if subSymbol.mtype.restype:
        #                                     if type(subSymbol.mtype.restype) is not type(params[-2][-1].eletype):
        #                                         raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #                             else:
        #                                 raise TypeMismatchInStatement(StaticChecker.stmtErr)
        #             else:
        #                 print("Case 10")
        #                 if len(leftType.dimen) == len(ast.idx):
        #                     if leftType.eletype:
        #                         retType = leftType.eletype
        #                 else:
        #                     if len(leftType.dimen) < len(ast.idx):
        #                         print("Error 21")
        #                         raise TypeMismatchInExpression(ast)
        #                     else:
        #                         retType = ArrayType(leftType.dimen[len(ast.idx):], leftType.eletype)
        #     else:
        #         # print("111111")
        #         # if params[-2]:
        #         #     if type(params[-2][-1]) is not ArrayType:
        #         #         print("?", params[-2])
        #         #         _, params = self.visit(ast.arr, params)
        #         #         # for x in scope:
        #         #         #     print(x)
        #         # else:
        #         #     pass
        #         if type(ast.arr) is Id:
        #             print("case 7.0")
        #             raise TypeCannotBeInferred(StaticChecker.stmtErr)
        #         else:
        #             subSymbol = Checker.utils.lookup(ast.arr.method.name, scope, Symbol.cmp)
        #             if subSymbol.mtype.restype:
        #                 if type(subSymbol.mtype.restype) is not ArrayType:
        #                     raise TypeMismatchInExpression(ast)
        #                 if params[-2]:
        #                     if type(subSymbol.mtype.restype) is not ArrayType:
        #                         raise TypeMismatchInExpression(ast)
        #                     else:
        #                         if type(params[-2][-1]) is not ArrayType:
        #                             if len(subSymbol.mtype.restype.dimen) != len(ast.idx):
        #                                 raise TypeMismatchInExpression(ast)
        #
        #                         else:
        #                             if len(subSymbol.mtype.restype.dimen) - len(ast.idx) != len(params[-2][-1].dimen):
        #                                 raise TypeMismatchInExpression(ast)
        #             else:
        #                 if params[-2]:
        #                     if type(params[-2][-1]) is not ArrayType:
        #                         print("Case 6.1")
        #                         raise TypeCannotBeInferred(StaticChecker.stmtErr)
        #                     else:
        #                         print("Case 6.2")
        #                         raise TypeCannotBeInferred(StaticChecker.stmtErr)
        #                 #else ????
        #
        #     # for x in ast.idx:
        #     #     returnType, params = self.visit(x, params)
        #     #
        #     #     if returnType:
        #     #         if type(returnType) is not IntType:
        #     #             raise TypeMismatchInExpression(ast)
        #     #     else:
        #     #         params[-2].append(IntType())
        #     #         _, params = self.visit(x, params)

        if listOp:

            retType = Utils.getTypeFromOperation(listOp[-1])

            if type(ast.arr) is CallExpr:
                StaticChecker.callArrayCell = True

            leftType, params = self.visit(ast.arr, params)

            if leftType:
                if type(leftType) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
                else:
                    # Handle index out of range
                    if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue)==len(leftType.dimen):
                        for i in range(len(leftType.dimen)):
                            if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                    raise IndexOutOfRange(ast)
                    #print("Tai sao lai sai", leftType.dimen, StaticChecker.arrayCellValue)
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    if type(ast.arr) is Id:
                        subSymbol = Checker.utils.lookup(ast.arr.name, scope, Symbol.cmp)

                        if type(subSymbol.mtype) is not ArrayType:
                            raise TypeMismatchInExpression(ast)

                        if len(subSymbol.mtype.dimen) != len(ast.idx):
                            print(">>>>")
                            raise TypeMismatchInExpression(ast)

                        if subSymbol.mtype.eletype:
                            # print("vl", retType, subSymbol.mtype.eletype)
                            if type(subSymbol.mtype.eletype) is not type(retType):
                                retType = subSymbol.mtype.eletype
                        else:
                            params[-2] = []
                            params[-2].append(ArrayType(subSymbol.mtype.dimen, retType))
                            leftType, params = self.visit(ast.arr, params)
                            # print("Tai sao lai sai", leftType.dimen, StaticChecker.arrayCellValue)
                            if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue) == len(leftType.dimen):
                                for i in range(len(leftType.dimen)):
                                    if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                        if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                            raise IndexOutOfRange(ast)

                    elif type(ast.arr) is CallExpr:
                        subSymbol = Checker.utils.lookup(ast.arr.method.name, scope, Symbol.cmp)

                        if type(subSymbol.mtype.restype) is not ArrayType:
                            raise TypeMismatchInExpression(ast)
                        else:
                            if len(subSymbol.mtype.restype.dimen) != len(ast.idx):
                                raise TypeMismatchInExpression(ast)

                            if subSymbol.mtype.restype.eletype:
                                if type(subSymbol.mtype.restype.eletype) is not type(retType):
                                    retType = subSymbol.mtype.restype.eletype
                            else:
                                params[-2] = []
                                params[-2].append(retType)
                                leftType, params = self.visit(ast.arr, params)
                                # print("Tai sao lai sai", leftType.dimen, StaticChecker.arrayCellValue)
                                if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue) == len(leftType.dimen):
                                    for i in range(len(leftType.dimen)):
                                        if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                            if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                                raise IndexOutOfRange(ast)

        else:
            # print("Hello")
            # print(params[-2])

            if type(ast.arr) is CallExpr:
                StaticChecker.callArrayCell = True

            leftType, params = self.visit(ast.arr, params)


            # print("Complete", leftType)
            # print(ast)
            if leftType:
                if type(leftType) is not ArrayType:
                    # print("F1")
                    raise TypeMismatchInExpression(ast)
                else:
                    #print("....1")
                    # print(params[-2])
                    # Handle index out of range
                    # print("Tai sao sai", leftType.dimen, StaticChecker.arrayCellValue)
                    if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue)==len(leftType.dimen):
                        for i in range(len(leftType.dimen)):
                            if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                    raise IndexOutOfRange(ast)

                    # print("Tai sao sai", leftType.dimen, StaticChecker.arrayCellValue)
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    #print(">", params[-2])
                    if params[-2]:
                        if type(ast.arr) is Id:
                            subSymbol = Checker.utils.lookup(ast.arr.name, scope, Symbol.cmp)

                            if type(params[-2][-1]) is ArrayType:
                                # print("F2")
                                raise TypeMismatchInExpression(ast)
                            else:
                                if len(subSymbol.mtype.dimen) != len(ast.idx):
                                    # print("F3")
                                    raise TypeMismatchInExpression(ast)

                                if params[0][params[0].index(subSymbol)].mtype.eletype:
                                    if type(params[0][params[0].index(subSymbol)].mtype.eletype) is not type(params[-2][-1]):
                                        # print("F4")
                                        raise TypeMismatchInExpression(ast)
                                else:
                                    # print("F+1")
                                    typ = params[-2][-1]
                                    params[-2] = []
                                    params[-2].append(ArrayType(subSymbol.mtype.dimen,typ))
                                    leftType, params = self.visit(ast.arr, params)
                                    # print("Tai sao lai sai", leftType.dimen, StaticChecker.arrayCellValue)
                                    if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue) == len(leftType.dimen):
                                        for i in range(len(leftType.dimen)):
                                            if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                                if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                                    raise IndexOutOfRange(ast)

                        elif type(ast.arr) is CallExpr:
                            subSymbol = Checker.utils.lookup(ast.arr.method.name, scope, Symbol.cmp)

                            if type(params[-2][-1]) is ArrayType:
                                # print("F6")
                                raise TypeMismatchInExpression(ast)
                            else:
                                if type(subSymbol.mtype.restype) is not ArrayType:
                                    # print("F7")
                                    raise TypeMismatchInExpression(ast)
                                else:
                                    if len(subSymbol.mtype.restype.dimen) != len(ast.idx):
                                        # print("F8")
                                        raise TypeMismatchInExpression(ast)

                                    if subSymbol.mtype.restype.eletype:
                                        if type(subSymbol.mtype.restype.eletype) is not type(params[-2][-1]):
                                            # print("F9")
                                            raise TypeMismatchInExpression(ast)
                                    else:
                                        # print("F+2")
                                        leftType, params = self.visit(ast.arr, params)
                                        # print("Tai sao lai sai", leftType.dimen, StaticChecker.arrayCellValue)
                                        if StaticChecker.arrayCellValue and leftType.dimen and len(StaticChecker.arrayCellValue) == len(leftType.dimen):
                                            for i in range(len(leftType.dimen)):
                                                if StaticChecker.arrayCellValue[i] != StaticChecker.RANDOM:
                                                    if StaticChecker.arrayCellValue[i] < 0 or StaticChecker.arrayCellValue[i] >= leftType.dimen[i]:
                                                        raise IndexOutOfRange(ast)
                                # if len(subSymbol.mtype.dimen) != len(ast.idx):
                                #     raise TypeMismatchInExpression(ast)
                                #
                                # if subSymbol.mtype.restype:
                                #     if type(subSymbol.mtype.restype) is not type(params[-2][-1]):
                                #         raise TypeMismatchInExpression(ast)
                                # else:
                                #     _, params = self.visit(ast.arr, params)



                    else:
                        # print("Hu hon")
                        # print("cas,",leftType)
                        if len(leftType.dimen) == len(ast.idx):
                            if leftType.eletype:
                                retType = leftType.eletype
                        else:
                            # print("F10")
                            raise TypeMismatchInExpression(ast)
            else:
                if type(ast.arr) is Id:
                    subSymbol = Checker.utils.lookup(ast.arr.name, scope, Symbol.cmp)
                    if type(subSymbol.mtype) is not ArrayType:
                        # print("F11")
                        raise TypeMismatchInExpression(ast)
                    # print("F12")
                raise TypeCannotBeInferred(StaticChecker.stmtErr)


        # Handle Index out of range here
        for x in ast.idx:
            # print("Bieu thuc:", x)

            returnType, params = self.visit(x, params)

            if returnType:
                if type(returnType) is not IntType:
                    # print("F13")
                    raise TypeMismatchInExpression(ast)
            else:
                # print("F+3")
                params[-2].append(IntType())
                _, params = self.visit(x, params)


        # print("Index Out Of Range", lstCheckValid)
        params[-2] = []
        print("Chan vai", retType)
        StaticChecker.arrayCellValue = []
        return [retType, params]


    def visitIf(self, ast:If, params):
        StaticChecker.stmtErr = ast
        # Scope.start("If")
        # print("Here AST IF")
        # print(ast)
        scope, retType, inLoop, funcName = params
        newScope = None
        refParams = [scope, funcName, [], []]
        listReturn = []
        stmts = None
        #IfThenStmt
        for x in ast.ifthenStmt:
            exp, listVar, listStmt = x
            returnType, refParams = self.visit(exp, refParams)
            # print("Return Type Ne", returnType)
            if returnType:
                if type(returnType) is not BoolType:
                    # print("G1")
                    raise TypeMismatchInStatement(ast)
            else:
                refParams[-2] = []
                refParams[-2].append(BoolType())
                typ, refParams = self.visit(exp, refParams)
                if type(typ) is not BoolType:
                    # print("G2")
                    raise TypeMismatchInStatement(ast)

            listLocalVar = [self.visit(x, refParams[0]).toVar() for x in listVar]

            newScope = Scope.merge(refParams[0],listLocalVar)

            subParam = [newScope, retType, False or inLoop, funcName]
            stmts = [self.visit(x, subParam) for x in listStmt]
            # print("*****Stmt*****")
            # for x in stmts:
            #     print(x[0])
            #     print(x[1])

            #Handle Unreachable statement
            listReturn.append(Checker.handleReturnStmts(stmts))
            # print("Win ", Checker.handleReturnStmts(stmts) )

        #elseStmt

        if ast.elseStmt:
            # print("Why", ast.elseStmt)
            listVar = ast.elseStmt[0]
            listStmt = ast.elseStmt[1]
            listLocalVar = [self.visit(x, refParams[0]).toVar() for x in listVar]

            newScope = Scope.merge(refParams[0], listLocalVar)

            subParam = [newScope, retType, False or inLoop, funcName]
            stmts = [self.visit(x, subParam) for x in listStmt]
            # print("*****Stmt*****")
            # for x in stmts:
            #     print(x)

            # Handle Unreachable statement
            listReturn.append(Checker.handleReturnStmts(stmts))
            # print("Win ", Checker.handleReturnStmts(stmts))

        # Scope.end()

        if list(filter(lambda x: x is None, listReturn)):
            # print("RIP1")
            return [ast, None, scope]

        ret = None
        symbol = Checker.utils.lookup(funcName, newScope, Symbol.cmp)
        if symbol:
            if type(symbol.kind) is Function:
                ret = symbol.mtype.restype
        # print("HELLO WORLD", ret)
        if all([x not in [type(y) for y in listReturn] for x in [Break, Continue]]):
            # print("RIP2")
            return [ast, ret, scope]


        return  [ast, Break(), scope]

    def visitFor(self, ast:For, params):
        StaticChecker.stmtErr = ast
        # Scope.start("For")

        scope, retType, inLoop, funcName = params
        refParams = [scope, funcName, [], []]

        idx1 = ast.idx1
        expr1 = ast.expr1
        expr2 = ast.expr2
        expr3 = ast.expr3

        idSymbol = Checker.checkUndeclared(scope,idx1.name,kind=Identifier())

        idType, refParams = self.visit(idx1, refParams)

        exp1Type, refParams = self.visit(expr1, refParams)

        if exp1Type:
            if type(exp1Type) is not IntType:
                # print("Error A1")
                raise TypeMismatchInStatement(ast)

            if idType:
                if type(idType) is not IntType:
                    # print("Error A2")
                    raise TypeMismatchInStatement(ast)
            else:
                # print("Visit A2")
                refParams[-2] = []
                refParams[-2].append(IntType())
                _, refParams = self.visit(idx1, refParams)
        else:
            if idType:
                if type(idType) is not IntType:
                    # print("Error A2")
                    raise TypeMismatchInStatement(ast)
                else:
                    # print("Visit A1")
                    refParams[-2] = []
                    refParams[-2].append(IntType())
                    _, refParams = self.visit(expr1, refParams)
            else:
                raise TypeCannotBeInferred(ast)

        exp2Type, refParams = self.visit(expr2, refParams)

        if exp2Type:
            if type(exp2Type) is not BoolType:
                raise TypeMismatchInStatement(ast)
        else:
            refParams[-2] = []
            refParams[-2].append(BoolType())
            _, refParams = self.visit(expr2, refParams)

        exp3Type, refParams = self.visit(expr3, refParams)

        if exp3Type:
            if type(exp3Type) is not IntType:
                raise TypeMismatchInStatement(ast)
        else:
            refParams[-2] = []
            refParams[-2].append(IntType())
            _, refParams = self.visit(expr3, refParams)

        stmts = None

        if ast.loop:
            listVar = ast.loop[0]
            listStmt = ast.loop[1]
            listLocalVar = [self.visit(x, refParams[0]).toVar() for x in listVar]

            newScope = Scope.merge(refParams[0], listLocalVar)

            subParam = [newScope, retType, True, funcName]
            stmts = [self.visit(x, subParam) for x in listStmt]
            # print("*****Stmt*****")
            # for x in stmts:
            #     print(x)

        ret = Checker.handleReturnStmts(stmts)

        return  [ast, None, scope]

    def visitBreak(self, ast:Break, params):
        # Scope.start("Break")
        scope, retType, inLoop, funcName = params
        if not inLoop:
            raise BreakNotInLoop()
        # Scope.end()
        return  [ast, Break(), scope]

    def visitContinue(self, ast:Continue, params):
        # Scope.start("Continue")
        scope, retType, inLoop, funcName = params
        if not inLoop:
            raise ContinueNotInLoop()
        # Scope.end()
        return [ast, Continue(), scope]

    def visitReturn(self, ast: Return, params):
        StaticChecker.stmtErr = ast
        # Scope.start("Return statement, function " + params[-1])
        scope, retType, inLoop, funcName = params
        # Change little in here to solve main declare in parameter
        symbol = None
        # print("??????? aucajca")
        subTemp = Checker.utils.lookup(funcName, scope, Symbol.cmp)
        # print("Me,", subTemp)
        refParams = [scope, funcName, [], []]
        ret = None
        if subTemp and type(subTemp.kind) is not Function:
            # StaticChecker.storeTemp[funcName]["return"] =

            if ast.expr:
                ret, refParams = self.visit(ast.expr, refParams)

                if ret:
                    if type(ret) is not ArrayType:
                        if type(ret) is VoidType:
                            # print("E1")
                            raise TypeMismatchInStatement(ast)

                        # if symbol.mtype.restype:
                        #     if type(symbol.mtype.restype) is not type(ret):
                        #         print("E2")
                        #         raise TypeMismatchInStatement(ast)
                        # else:
                        #     symbol.mtype.restype = ret
                        StaticChecker.storeTemp[funcName]["return"] = ret
                        retType = ret
                    else:
                        # if symbol.mtype.restype:
                        #     if type(symbol.mtype.restype) is not ArrayType:
                        #         print("E3")
                        #         raise TypeMismatchInStatement(ast)
                        #     else:
                        #         if ret.eletype and symbol.mtype.restype.eletype:
                        #             if type(ret.eletype) is not type(symbol.mtype.restype.eletype):
                        #                 print("E4")
                        #                 raise TypeMismatchInStatement(ast)
                        #         elif ret.eletype:
                        #             symbol.mtype.restype.eletype = ret.eletype
                        #         elif symbol.mtype.restype.eletype:
                        #             ret.eletype = symbol.mtype.restype.eletype
                        #         else:
                        #             print("E5")
                        #             raise TypeMismatchInStatement(ast)
                        # else:
                        #     if not ret.eletype:
                        #         print("E6")
                        #         raise TypeCannotBeInferred(ast)
                        #     else:
                        #         symbol.mtype.restype = ret
                        if not ret.eletype:
                            # print("E11")
                            raise TypeCannotBeInferred(ast)
                        else:
                            StaticChecker.storeTemp[funcName]["return"] = ret
                            retType = ret
                else:
                    # if symbol.mtype.restype:
                    #     if type(symbol.mtype.restype) is VoidType:
                    #         print("E7")
                    #         raise TypeMismatchInStatement(ast)
                    #
                    #     if type(symbol.mtype.restype) is ArrayType:
                    #         if not symbol.mtype.restype.eletype:
                    #             print("E8")
                    #             raise TypeMismatchInStatement(ast)
                    #
                    # else:
                    #     print("E9")
                    #     raise TypeMismatchInStatement(ast)
                    # print("E12687")
                    if StaticChecker.storeTemp[funcName]["return"]:
                        refParams[-2] = []
                        refParams[-2].append(StaticChecker.storeTemp[funcName]["return"])
                        ret, refParams = self.visit(ast.expr, refParams)
                        retType = ret
                    else:
                        raise TypeMismatchInStatement(ast)


            else:
                if symbol.mtype.restype:
                    if type(symbol.mtype.restype) is not VoidType:
                        # print("E10")
                        raise TypeMismatchInStatement(ast)
                else:
                    symbol.mtype.restype = VoidType()
                    retType = VoidType()
        else:
            # print("GGGGG")
            symbol = Checker.checkUndeclared(scope, funcName, kind=Function())

            if type(symbol.mtype.restype) is VoidType and ast.expr:
                raise TypeMismatchInStatement(ast)

            if ast.expr:
                ret, refParams = self.visit(ast.expr, refParams)

                if ret:
                    if type(ret) is not ArrayType:
                        if type(ret) is VoidType:
                            # print("E1")
                            raise TypeMismatchInStatement(ast)

                        if symbol.mtype.restype:
                            if type(symbol.mtype.restype) is not type(ret):
                                # print("E2")
                                raise TypeMismatchInStatement(ast)
                        else:
                            symbol.mtype.restype = ret
                            retType = ret
                    else:
                        if symbol.mtype.restype:
                            if type(symbol.mtype.restype) is not ArrayType:
                                # print("E3")
                                raise TypeMismatchInStatement(ast)
                            else:
                                if ret.eletype and symbol.mtype.restype.eletype:
                                    if type(ret.eletype) is not type(symbol.mtype.restype.eletype):
                                        # print("E4")
                                        raise TypeMismatchInStatement(ast)
                                elif ret.eletype:
                                    symbol.mtype.restype.eletype = ret.eletype
                                    retType = ret
                                elif symbol.mtype.restype.eletype:
                                    ret.eletype = symbol.mtype.restype.eletype
                                    retType = ret
                                else:
                                    # print("E5")
                                    raise TypeMismatchInStatement(ast)
                        else:
                            if not ret.eletype:
                                # print("E6")
                                raise TypeCannotBeInferred(ast)
                            else:
                                symbol.mtype.restype = ret
                                retType = ret
                else:
                    if symbol.mtype.restype:
                        if type(symbol.mtype.restype) is VoidType:
                            # print("E7")
                            raise TypeMismatchInStatement(ast)

                        if type(symbol.mtype.restype) is ArrayType:
                            if not symbol.mtype.restype.eletype:
                                # print("E8")
                                raise TypeMismatchInStatement(ast)

                    else:
                        # print("E9")
                        raise TypeMismatchInStatement(ast)


            else:
                if symbol.mtype.restype:
                    if type(symbol.mtype.restype) is not VoidType:
                        # print("E10")
                        raise TypeMismatchInStatement(ast)
                else:
                    symbol.mtype.restype = VoidType()
                    retType = VoidType()

        # print(StaticChecker.storeTemp)



        # print("WWWWWWWWW", retType)
        # for x in refParams[0]:
        #     print(x)
        # Scope.end()
        return [ast, ret, scope]


    def visitDowhile(self, ast: Dowhile, params):
        StaticChecker.stmtErr = ast
        # Scope.start("Do-While")
        scope, retType, inLoop, funcName = params

        refParams = [scope, funcName, [], []]
        # print("*********************** Scope before ****************************")
        # for x in refParams[0]:
        #     print(x)

        stmts = None
        if ast.sl:
            listVar = ast.sl[0]
            listStmt = ast.sl[1]

            listLocalVar = [self.visit(x, refParams[0]).toVar() for x in listVar]
            newScope = Scope.merge(refParams[0], listLocalVar)

            # Visit statements
            subParam = [newScope, retType, True, funcName]
            stmts = [self.visit(x, subParam) for x in listStmt]
            # print("*****Stmt*****")
            # for x in stmts:
            #     print(x)
        # print("*********************** Scope after ****************************")
        if stmts:
            # for x in stmts[-1][-1]:
            #     print(x)

            for x in stmts[-1][-1]:
                tmp = Checker.utils.lookup((x.name, type(x.kind)), scope, lambda m: (m.name, type(m.kind)))
                if tmp:
                    scope[scope.index(tmp)] = x
        # print("*********************** Scope after change ****************************")
        # for x in scope:
        #     print(x)
        StaticChecker.stmtErr = ast

        returnType, refParams = self.visit(ast.exp, refParams)

        if returnType:
            if type(returnType) is not BoolType:
                # print("Q1")
                raise TypeMismatchInStatement(ast)
        else:
            refParams[-2] = []
            refParams[-2].append(BoolType())
            typ, refParams = self.visit(ast.exp, refParams)

            if type(typ) is not BoolType:
                # print("Q2")
                raise TypeMismatchInStatement(ast)

        # Scope.end()

        ret = Checker.handleReturnStmts(stmts)
        return [ast, None, scope]

    def visitWhile(self, ast:While, params):

        StaticChecker.stmtErr = ast
        # Scope.start("While")
        scope, retType, inLoop, funcName = params

        refParams = [scope, funcName, [], []]

        returnType, refParams = self.visit(ast.exp, refParams)
        if returnType:
            if type(returnType) is not BoolType:
                # print("R1")
                raise TypeMismatchInStatement(ast)
        else:
            refParams[-2] = []
            refParams[-2].append(BoolType())
            typ, refParams = self.visit(ast.exp, refParams)
            if type(typ) is not BoolType:
                # print("R2")
                raise TypeMismatchInStatement(ast)

        stmts = None

        if ast.sl:
            listVar = ast.sl[0]
            listStmt = ast.sl[1]

            listLocalVar = [self.visit(x, refParams[0]).toVar() for x in listVar]
            newScope = Scope.merge(refParams[0], listLocalVar)

            # Visit statements
            subParam = [newScope, retType, True, funcName]
            stmts = [self.visit(x, subParam) for x in listStmt]
            # print("*****Stmt*****")
            # for x in stmts:
            #     print(x)
        # Scope.end()

        ret = Checker.handleReturnStmts(stmts)

        return [ast, None, scope]

    def visitCallStmt(self, ast: CallStmt, params):
        StaticChecker.stmtErr = ast


        scope, retType, inLoop, funcName = params

        # Update graph
        Graph.add(funcName, ast.method.name)

        #Params to visit
        refParams = [scope, funcName, [], []]

        symbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())

        retType = None
        if len(symbol.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        if symbol.mtype.restype:
            if type(symbol.mtype.restype) is not VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            symbol.mtype.restype = VoidType()
            retType = VoidType()


        index = 0
        for x in ast.param:
            returnType, refParams = self.visit(x, refParams)

            # print("HUHUHUHU", returnType)
            # If exist return type
            if returnType:
                #Change
                if type(returnType) is VoidType:
                    raise TypeMismatchInStatement(StaticChecker.stmtErr)
                # print("Here: ", symbol)
                paramArr = symbol.mtype.intype[index]
                # If type is not ArrayType
                if type(returnType) is not ArrayType:
                    if paramArr:
                        if type(paramArr) is not type(returnType):
                            # print("1")
                            raise TypeMismatchInStatement(ast)
                    else:
                        # print("Index :", index)
                        symbol.mtype.setIntType(index, returnType)
                else:
                    if type(paramArr) is not ArrayType:
                        # print("2")
                        raise TypeMismatchInStatement(ast)

                    # Array dimension
                    first = paramArr.dimen
                    second = returnType.dimen

                    # Check if two dimension are same
                    if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
                        temp1 = returnType.eletype
                        temp2 = paramArr.eletype
                        if temp1 is not None and temp2 is not None:
                            if type(temp1) is not type(temp2):
                                # print("3")
                                raise TypeMismatchInStatement(ast)
                        elif temp1 is not None:
                            paramArr.eletype = returnType.eletype
                            # print("Index: ", paramArr)
                        elif temp2 is not None:
                            # Add updateParam in params with corresponding parameter
                            refParams[-2].append(paramArr)
                            #print("GO there")
                            # print("4")
                            _, refParams = self.visit(ast.param[index], refParams)
                        else:
                            # print("5")
                            raise TypeCannotBeInferred(ast)
                    else:
                        # print("6")
                        raise TypeMismatchInExpression(ast)

            # else: ?????????
            else:
                # for x in scope:
                #     print(x)
                # print("Param dau")
                subSymbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())
                # print("SUb,", subSymbol)

                # if subSymbol.mtype.intype[index]:
                #     refParams[-2].append(subSymbol.mtype.intype[index])
                #     #Change
                #     _, refParams = self.visit(ast.param[index], refParams)
                # else:
                #     raise TypeCannotBeInferred(StaticChecker.stmtErr)

                temp = subSymbol.mtype.intype[index]
                if temp:
                    if type(temp) is not ArrayType:
                        # print("Chan",temp, params[-2])
                        refParams[-2].append(subSymbol.mtype.intype[index])
                        # Change
                        _, refParams = self.visit(ast.param[index], refParams)
                    else:
                        if temp.eletype:
                            # print("Case 2")
                            refParams[-2].append(temp)
                            # Change
                            _, refParams = self.visit(ast.param[index], refParams)
                        else:
                            raise TypeCannotBeInferred(StaticChecker.stmtErr)

                else:
                    raise TypeCannotBeInferred(StaticChecker.stmtErr)

            index = index + 1


        # for x in scope:
        #     print(x)
        # print("Xong r", symbol)



        return [ast, None, scope]


    def visitBinaryOp(self, ast: BinaryOp, params):
        # Change: add updateParam
        scope, funcName, updateParam, listOp = params
        op = ast.op

        actualType = Utils.getTypeFromOperation(op)
        #print(actualType)
        #Add operation and visit left and update params
        params[-1].append(op)
        lType , params = self.visit(ast.left, params)
        print(params[-1])

        #Check left type must has the same type of operation:
        #Example : y = (3 + 5) *. (5.3 + 2)

        if type(lType) is not type(actualType):
            raise TypeMismatchInExpression(ast)

        #Add operation and visit right and update params
        params[-1].append(op)
        print(params[-1])
        print(type(ast.right))
        rType, params = self.visit(ast.right, params)


        #Update listOp of params
        params[-1] = params[-1][:-1]

        if op in ['-', '+', '*', '\\', '%']:
            if type(lType) is IntType and type(rType) is IntType:
                return [IntType(), params]
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(lType) is IntType and type(rType) is IntType:
                return [BoolType(), params]
        elif op in ['-.', '+.', '*.', '\\.']:
            if type(lType) is FloatType and type(rType) is FloatType:
                return [FloatType(), params]
        elif op in ['!', '&&', '||']:
            if type(lType) is BoolType and type(rType) is BoolType:
                return [BoolType(), params]
        elif op in ['=/=', '<.', '>.', '<=.', '>=.']:
            if type(lType) is FloatType and type(rType) is FloatType:
                return [BoolType(), params]

        raise TypeMismatchInExpression(ast)




    def visitUnaryOp(self, ast: UnaryOp, params):
        # Change: add updateParam
        scope, funcName, updateParam, listOp = params

        op = ast.op


        actualType = Utils.getTypeFromOperation(op)
        #print(actualType)

        # Add operation and visit left and update params
        params[-1].append(op)
        print(params[-1])

        rType, params = self.visit(ast.body, params)
        print(params[-1])
        # Update listOp of params
        params[-1] = params[-1][:-1]


        #Continue here........................................
        if op in ['!']:
            if type(rType) is BoolType:
                return [BoolType(), params]
        elif op in ['-']:
            if type(rType) is IntType:
                return [IntType(), params]
        elif op in ['-.']:
            if type(rType) is FloatType:
                return [FloatType(), params]

        raise TypeMismatchInExpression(ast)


    def visitId(self, ast: Id, params):
        #Change: add updateParam
        scope, funcName, updateParam, listOp = params
        # print(ast, listOp)
        # print("I here, ", ast, params[-2])
        #Check Undeclared of Id and get the symbol
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        # print(ast.name)
        # for x in scope:
        #     print(x)
        print(symbol)
        retType = None

        if listOp:
            operation = listOp[-1]
            retType = Utils.getTypeFromOperation(operation)
            # print(ast, retType)
            #If symbol doesn't has type, infer base on operation
            if not symbol.mtype:
                # print("Test: ", symbol)
                params[0][params[0].index(symbol)].toType(retType)
                #Update parameter of this function
                if type(symbol.kind) is Parameter:
                    # print(symbol.name, funcName)
                    if symbol.name != funcName:
                        funcSymbol = Checker.utils.lookup(funcName, scope, Symbol.cmp)
                        if type(funcSymbol.kind) is Function:
                            indexToUpdate = StaticChecker.storeParam[ast.name]
                            params[0][params[0].index(funcSymbol)].mtype.setIntType(indexToUpdate, symbol.mtype)

                        else:
                            if not StaticChecker.storeTemp:
                                StaticChecker.storeTemp[funcName] = {}

                            indexUpdate = StaticChecker.storeParam[symbol.name]
                            StaticChecker.storeTemp[funcName][indexUpdate] = retType
                    else:
                        if not StaticChecker.storeTemp:
                            StaticChecker.storeTemp[funcName] = {}

                        indexUpdate = StaticChecker.storeParam[funcName]
                        StaticChecker.storeTemp[funcName][indexUpdate] = retType


            else:
                if type(symbol.mtype) is ArrayType:
                    if symbol.mtype.eletype:
                        # if type(symbol.mtype.eletype) != type(retType):
                        retType = symbol.mtype
                    else:
                        symbol.mtype.eletype = retType
                        retType = symbol.mtype
                else:

                    retType = symbol.mtype

            #Update listOp of params
            params[-1] = params[-1][:-1]
        else:
            # print(updateParam)
            # print(symbol)
            # print("I am")
            # print("UUUU", updateParam)
            if updateParam:
                # print("IIII")
                if type(updateParam[-1]) is not ArrayType:
                    # print("???Kaka")

                    subSymbol = params[0][params[0].index(symbol)]
                    # print(subSymbol)
                    # params[0][params[0].index(symbol)].toType(updateParam[-1])
                    if type(subSymbol.mtype) is not ArrayType:
                        subSymbol.mtype = updateParam[-1]
                    else:
                        subSymbol.mtype.eletype = updateParam[-1]
                        # print(subSymbol)
                else:
                    # print("Herrr", symbol)
                    if type(symbol.mtype) is ArrayType:
                        # print("Case 2.")
                        first = symbol.mtype.dimen
                        second = updateParam[-1].dimen
                        # print(first, second)

                        if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
                            params[0][params[0].index(symbol)].toType(updateParam[-1])
                        else:
                            raise TypeCannotBeInferred(StaticChecker.stmtErr)

                    else:
                        # print("Case 1.")
                        raise TypeCannotBeInferred(StaticChecker.stmtErr)


                # print("Handle", updateParam[-1])
            # print("Symbol: ", symbol)
                # Update parameter of this function
                if type(symbol.kind) is Parameter:
                    # print(symbol.name, funcName)
                    if symbol.name != funcName:
                        funcSymbol = Checker.utils.lookup(funcName, scope, Symbol.cmp)
                        if type(funcSymbol.kind) is Function:
                            indexToUpdate = StaticChecker.storeParam[ast.name]
                            #retType = updateParam[-1]
                            params[0][params[0].index(funcSymbol)].mtype.setIntType(indexToUpdate, symbol.mtype)
                        #else ???
                        else:
                            if not StaticChecker.storeTemp:
                                StaticChecker.storeTemp[funcName] = {}

                            indexUpdate = StaticChecker.storeParam[symbol.name]
                            StaticChecker.storeTemp[funcName][indexUpdate] = retType
                    else:
                        if not StaticChecker.storeTemp:
                            StaticChecker.storeTemp[funcName] = {}

                        indexUpdate = StaticChecker.storeParam[funcName]
                        StaticChecker.storeTemp[funcName][indexUpdate] = retType

            else:
                funcSymbol = Checker.utils.lookup(funcName,  scope, Symbol.cmp)

                if funcSymbol and type(funcSymbol.kind) is Function:

                    lst = []
                    for x in scope:
                        if type(x.kind) is Parameter:
                            lst.append(x)

                    index = 0
                    for x in funcSymbol.mtype.intype:
                        if x:
                            if not lst[index].mtype:
                                lst[index].mtype = x
                        index = index + 1


            #Initial the updateParam to empty
            params[-2] = []


            retType = symbol.mtype
        # print("CHan dowif", retType)

        return [retType, params]




    def visitCallExpr(self, ast: CallExpr, params):
        # StaticChecker.callArrayCell = False
        # Change: add updateParam

        scope, funcName, updateParam, listOp = params

        # Update graph
        Graph.add(funcName, ast.method.name)
        # print("I am here")
        # for x in scope:
        #     print(x)
        symbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())

        retType = None

        if len(symbol.mtype.intype) != len(ast.param):
            # print("Error 1")
            raise TypeMismatchInExpression(ast)

        if listOp:
            operation = listOp[-1]
            retType = Utils.getTypeFromOperation(operation)
            # print(operation, retType, symbol)
            # print("Hello", symbol)
            if symbol.mtype.restype is None:
                if StaticChecker.callArrayCell == False:
                    # print("m2")
                    temp = params[0][params[0].index(symbol)]
                    temp.toType(temp.mtype.setInOutType(temp.mtype.intype, retType))
                    # print("Yeah", temp)
                else:
                    # print("M1")
                    raise TypeCannotBeInferred(StaticChecker.stmtErr)
                # print(temp)
            else:
                # print("CCCCCCCCCC")
                #Check return type of function
                print(retType, symbol.mtype.restype)
                if type(retType) is not type(symbol.mtype.restype):
                    # print("Hlalala")
                    retType = symbol.mtype.restype
                    return [retType, params]

                # print("Param *****************", symbol)
                # for x in scope:
                #     if type(x.kind) is Parameter:
                #         print(x)
                # lst = []
                # for m in scope:
                #     if type(m.kind) is Parameter:
                #         lst.append(m)
                #         print(m)
                # print("End **************")
                # index = 0
                # for x in symbol.mtype.intype:
                #     if x:
                #         if lst[index].mtype:
                #             if type(lst[index].mtype) is not type(x):
                #                 print("Handle For")
                #                 raise TypeMismatchInStatement(StaticChecker.stmtErr)
                #     index = index + 1




            #Update params and param of function after each loop
            index = 0
            for x in ast.param:
                # print("Visit ne", x)
                if symbol.mtype.intype[index]:
                    print("chan v", symbol.mtype.intype[index])
                    params[-2] = []
                    params[-2].append(symbol.mtype.intype[index])
                returnType, params = self.visit(x, params)

                #If exist return type
                if returnType:
                    paramArr = symbol.mtype.intype[index]
                    #If type is not ArrayType
                    if type(returnType) is not ArrayType:
                        if paramArr:
                            if type(paramArr) is not type(returnType):
                                # print("Error 2")
                                raise TypeMismatchInExpression(ast)
                        else:
                            symbol.mtype.setIntType(index, returnType)
                    else:
                        if type(paramArr) is not ArrayType:
                            # print("Error 3")
                            raise TypeMismatchInExpression(ast)

                        #Array dimension
                        first = paramArr.dimen
                        second = returnType.dimen

                        #Check if two dimension are same
                        if reduce(lambda x,y: x and y, map(lambda p,q: p == q, first, second), True):
                            temp1 = returnType.eletype
                            temp2 = paramArr.eletype
                            if temp1 is not None and temp2 is not None:
                                if type(temp1) is not type(temp2):
                                    # print("Error 4")
                                    raise TypeMismatchInExpression(ast)
                            elif temp1 is not None:
                                paramArr.eletype = returnType.eletype
                            elif temp2 is not None:
                                # Add updateParam in params with corresponding parameter
                                params[-2].append(paramArr)
                                # print("GO there")
                                self.visit(ast.param[index], params)
                            else:
                                # print("Error 5")
                                raise TypeCannotBeInferred(StaticChecker.stmtErr)
                        else:
                            # print("Error 6")
                            raise TypeMismatchInExpression(ast)

                #else: ?????????
                else:
                    # print("Handle")
                    subSymbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())
                    if subSymbol.mtype.intype[index]:
                        params[-2].append(subSymbol.mtype.intype[index])
                        # Change
                        _, params = self.visit(ast.param[index], params)
                    else:
                        raise TypeCannotBeInferred(StaticChecker.stmtErr)

                index = index + 1
        else:
            # print("f3")
            subSymbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())
            #print("<<",subSymbol)
            if subSymbol.mtype.restype:
                if StaticChecker.callArrayCell == False:
                    retType = subSymbol.mtype.restype
                else:
                    # print("WOWOWOWOWO")
                    StaticChecker.callArrayCell = False
                    if type(subSymbol.mtype.restype) is not ArrayType:
                        # print("Error 55")
                        raise TypeCannotBeInferred(StaticChecker.stmtErr)
                    retType = subSymbol.mtype.restype
            else:
                if StaticChecker.callArrayCell == False:
                    # print("MMMMMMMMMMMMMMMMM")
                    if params[-2]:
                        # print("CMCMCM", params[-2])
                        subSymbol.mtype.restype = params[-2][-1]
                        # print("Hello", subSymbol)
                        retType = params[-2][-1]
                        # print("Quai la")
                else:
                    # print("11111111111111111111111111")
                    StaticChecker.callArrayCell = False
                    if params[-2]:
                        if type(params[-2][-1]) is not ArrayType:
                            raise TypeCannotBeInferred(StaticChecker.stmtErr)
                        else:
                            subSymbol.mtype.restype = params[-2][-1]
                            retType = params[-2][-1]

                    else:
                        raise TypeCannotBeInferred(StaticChecker.stmtErr)

            # print("kl")
            index = 0
            for x in ast.param:
                if params[-2]:
                    params[-2] = []
                returnType, params = self.visit(x, params)

                # If exist return type
                if returnType:
                    paramArr = symbol.mtype.intype[index]
                    # If type is not ArrayType
                    if type(returnType) is not ArrayType:
                        if paramArr:
                            if type(paramArr) is not type(returnType):
                                print("Error 7")
                                raise TypeMismatchInExpression(ast)
                        else:
                            symbol.mtype.setIntType(index, returnType)
                    else:
                        if type(paramArr) is not ArrayType:
                            print("Error 8")
                            raise TypeMismatchInExpression(ast)

                        # Array dimension
                        first = paramArr.dimen
                        second = returnType.dimen

                        # Check if two dimension are same
                        if reduce(lambda x, y: x and y, map(lambda p, q: p == q, first, second), True):
                            temp1 = returnType.eletype
                            temp2 = paramArr.eletype
                            if temp1 is not None and temp2 is not None:
                                if type(temp1) is not type(temp2):
                                    print("Error 9")
                                    raise TypeMismatchInExpression(ast)
                            elif temp1 is not None:
                                paramArr.eletype = returnType.eletype
                            elif temp2 is not None:
                                # Add updateParam in params with corresponding parameter
                                params[-2].append(paramArr)
                                print("GO there")
                                #Change
                                _, params = self.visit(ast.param[index], params)
                            else:
                                print("Error 10")
                                raise TypeCannotBeInferred(StaticChecker.stmtErr)
                        else:
                            print("Error 11")
                            raise TypeMismatchInExpression(ast)

                # else: ?????????
                else:
                    # print("Handle")
                    subSymbol = Checker.checkUndeclared(scope, ast.method.name, kind=Function())
                    temp = subSymbol.mtype.intype[index]
                    if temp:
                        if type(temp) is not ArrayType:
                            params[-2].append(subSymbol.mtype.intype[index])
                            # Change
                            _, params = self.visit(ast.param[index], params)
                        else:
                            if temp.eletype:
                                # print("Case 2")
                                params[-2].append(temp)
                                #Change
                                _, params = self.visit(ast.param[index], params)
                            else:
                                # print("f2")
                                raise TypeCannotBeInferred(StaticChecker.stmtErr)

                    else:
                        # print("f1")
                        raise TypeCannotBeInferred(StaticChecker.stmtErr)

                index = index + 1
        # print("CLGT")
        # print(retType)
        params[-2] = []
        StaticChecker.callArrayCell = False
        # print("WOw", retType)
        return [retType, params]



    def visitIntLiteral(self, ast, params):
        if params[-1]:
            params[-1] = params[-1][:-1]
        return [IntType(), params]

    def visitFloatLiteral(self, ast, params):
        if params[-1]:
            params[-1] = params[-1][:-1]
        return [FloatType(), params]

    def visitBooleanLiteral(self, ast, params):
        if params[-1]:
            params[-1] = params[-1][:-1]
        return [BoolType(), params]

    def visitStringLiteral(self, ast, params):
        if params[-1]:
            params[-1] = params[-1][:-1]
        return [StringType(), params]

    def visitArrayLiteral(self, ast, params):
        if params[-1]:
            params[-1] = params[-1][:-1]
            return [StringType(), params]


        # print("Yeah, i know")
        _, lit = Checker.checkValidArray(ast)
        retType = None
        dimen = []
        dimen = Utils.getDimensionOfArray(ast, dimen)

        if lit is IntLiteral:
            retType = IntType()
        elif lit is StringLiteral:
            retType = StringType()
        elif lit is FloatLiteral:
            retType = FloatType()
        elif lit is BooleanLiteral:
            retType = BoolType()



        return [ArrayType(dimen, retType), params]


        
