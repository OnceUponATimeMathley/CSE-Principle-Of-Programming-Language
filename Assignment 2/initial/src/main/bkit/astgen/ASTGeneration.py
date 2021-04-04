from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

import time

class ASTGeneration(BKITVisitor):
    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        list_decl = []
        if ctx.global_dec():
            for x in ctx.global_dec():
                list_decl.extend(x.accept(self))
        if ctx.function_dec():
            for x in ctx.function_dec():
                list_decl.append(x.accept(self))

        return Program(list_decl)


    # Visit a parse tree produced by BKITParser#global_dec.
    def visitGlobal_dec(self, ctx: BKITParser.Global_decContext):
        # List ( List( VarDecl) ) ) -> List ( VarDecl )
        global_decl = []
        for x in ctx.variable_dec():
            global_decl.extend(x.accept(self))
        return global_decl

    # Visit a parse tree produced by BKITParser#variable_dec.
    def visitVariable_dec(self, ctx: BKITParser.Variable_decContext):
        return ctx.variable_list().accept(self)

    # Visit a parse tree produced by BKITParser#variable_list.
    def visitVariable_list(self, ctx: BKITParser.Variable_listContext):
        # List VarDecl
        return [x.accept(self) for x in ctx.variable()]

    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx: BKITParser.VariableContext):
        #One value
        if ctx.scalar():
            variable, varDimen = ctx.scalar().accept(self)
            varInit = None
            if ctx.literal():
                varInit = ctx.literal().accept(self)

            return VarDecl(variable, varDimen,varInit)

        if ctx.composite():
            variable, varDimen = ctx.composite().accept(self)
            varInit = None
            if ctx.literal():
                varInit = ctx.literal().accept(self)

            return VarDecl(variable, varDimen, varInit)

    # Visit a parse tree produced by BKITParser#scalar.
    def visitScalar(self, ctx: BKITParser.ScalarContext):
        #One value
        variable = Id(ctx.ID().getText())
        varDimen = []
        return (variable,varDimen)

    # Visit a parse tree produced by BKITParser#composite.
    def visitComposite(self, ctx: BKITParser.CompositeContext):
        #One tuple value
        variable = Id(ctx.ID().getText())
        varDimen = []
        varDimen.extend([eval(x.getText()) for x in ctx.INTEGER_LITERAL()])

        return (variable, varDimen)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        # One value
        if ctx.lit_type():
            return ctx.lit_type().accept(self)

        if ctx.array_literal():
            return ctx.array_literal().accept(self)


    # Visit a parse tree produced by BKITParser#function_dec.
    def visitFunction_dec(self, ctx: BKITParser.Function_decContext):
        name = Id(ctx.ID().getText())

        param = []
        if ctx.parameter_list():
            param = ctx.parameter_list().accept(self)

        list_vardecl = []
        list_stmt = []
        if ctx.variable_declaration_stmt():
            for x in ctx.variable_declaration_stmt():
                list_vardecl.extend(x.accept(self))

        if ctx.statement_list():
            for x in ctx.statement_list():
                list_stmt.append(x.accept(self))
        body = (list_vardecl,list_stmt)
        return FuncDecl(name,param, body)

    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx: BKITParser.Parameter_listContext):
        # List VarDecl
        return [VarDecl(x.accept(self)[0], x.accept(self)[1], None) for x in ctx.parameter()]

    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx: BKITParser.ParameterContext):
        # One tuple
        if ctx.scalar():
            return ctx.scalar().accept(self)

        if ctx.composite():
            return ctx.composite().accept(self)

    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx: BKITParser.Statement_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKITParser#variable_declaration_stmt.
    def visitVariable_declaration_stmt(self, ctx: BKITParser.Variable_declaration_stmtContext):
        return ctx.variable_dec().accept(self)

    # Visit a parse tree produced by BKITParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx: BKITParser.Assignment_stmtContext):
        last_exp = (ctx.expression()[-1]).accept(self)

        lhs = None
        if ctx.getChildCount() == 4:
            lhs = Id(ctx.ID().getText())
        else:
            if ctx.LP():
                method = Id(ctx.ID().getText())
                idx = []
                num_function_call_exp = len(ctx.expression()) - 1 - len(ctx.LSB())
                funcall_exp = []
                for x in ctx.expression()[:num_function_call_exp]:
                    funcall_exp.append(x.accept(self))

                arr = CallExpr(method,funcall_exp)

                for x in ctx.expression()[num_function_call_exp:-1]:
                    idx.append(x.accept(self))

                lhs = ArrayCell(arr,idx)
            else:
                arr = Id(ctx.ID().getText())
                idx = []
                for x in ctx.expression()[:-1]:
                    idx.append(x.accept(self))

                lhs = ArrayCell(arr, idx)
        return Assign(lhs, last_exp)

    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        num = ctx.getChildCount()
        idx = 0
        ifthenStmt = []
        expr = None
        vardecl = []
        stmt = []
        while idx < num:
            variable = ctx.getChild(idx)
            if variable in ctx.expression():
                ifthenStmt.append((expr,vardecl,stmt))
                vardecl = []
                stmt = []
                expr = variable.accept(self)
            elif variable in ctx.variable_declaration_stmt():
                vardecl.extend(variable.accept(self))
            elif variable in ctx.statement_list():
                stmt.append(variable.accept(self))
            elif (variable is ctx.ELSE()) or (variable is ctx.ENDIF()):
                ifthenStmt.append((expr, vardecl, stmt))
                break

            idx = idx + 1

        idx = idx + 1
        ifthenStmt = ifthenStmt[1:]
        vardecl_else = []
        stmt_else = []
        elseStmt = (vardecl_else, stmt_else)
        if ctx.ELSE():
            while idx < num:
                variable = ctx.getChild(idx)
                if variable in ctx.variable_declaration_stmt():
                    vardecl_else.extend(variable.accept(self))
                elif variable in ctx.statement_list():
                    stmt_else.append(variable.accept(self))

                elif variable is ctx.ENDIF():
                    #elseStmt = (vardecl_else, stmt_else)
                    break

                idx = idx + 1
        else:
            elseStmt = (vardecl_else, stmt_else)
        return If(ifthenStmt,elseStmt)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        idx1 = (ctx.scalar().accept(self))[0]
        expr1 = ctx.expression(0).accept(self)
        expr2 = ctx.expression(1).accept(self)
        expr3 = ctx.expression(2).accept(self)

        vardecl = []
        stmt = []
        if ctx.variable_declaration_stmt():
            for x in ctx.variable_declaration_stmt():
                vardecl.extend(x.accept(self))

        if ctx.statement_list():
            for x in ctx.statement_list():
                stmt.append(x.accept(self))

        loop = (vardecl, stmt)
        return For(idx1,expr1,expr2,expr3,loop)



    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        exp = ctx.expression().accept(self)

        vardecl = []
        stmt = []
        if ctx.variable_declaration_stmt():
            for x in ctx.variable_declaration_stmt():
                vardecl.extend(x.accept(self))

        if ctx.statement_list():
            for x in ctx.statement_list():
                stmt.append(x.accept(self))

        sl = (vardecl, stmt)
        return While(exp,sl)

    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx: BKITParser.Do_while_stmtContext):
        vardecl = []
        stmt = []
        if ctx.variable_declaration_stmt():
            for x in ctx.variable_declaration_stmt():
                vardecl.extend(x.accept(self))

        if ctx.statement_list():
            for x in ctx.statement_list():
                stmt.append(x.accept(self))
        sl = (vardecl, stmt)

        exp = ctx.expression().accept(self)
        return Dowhile(sl, exp)

    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return Break()

    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx: BKITParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        param = []
        if ctx.expression():
            for x in ctx.expression():
                param.append(x.accept(self))

        return CallStmt(method, param)



    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        expr = None
        if ctx.expression():
            expr = ctx.expression().accept(self)
        return Return(expr)

    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return ctx.exp1(0).accept(self)

        left = ctx.exp1(0).accept(self)
        right = ctx.exp1(1).accept(self)
        op = ctx.getChild(1).getText()

        return BinaryOp(op, left, right)

    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return ctx.exp2().accept(self)

        left = ctx.exp1().accept(self)
        right = ctx.exp2().accept(self)
        op = ctx.getChild(1).getText()

        return BinaryOp(op, left, right)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return ctx.exp3().accept(self)

        left = ctx.exp2().accept(self)
        right = ctx.exp3().accept(self)
        op = ctx.getChild(1).getText()

        return BinaryOp(op, left, right)

    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return ctx.exp4().accept(self)

        left = ctx.exp3().accept(self)
        right = ctx.exp4().accept(self)
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return ctx.exp5().accept(self)

        op = ctx.getChild(0).getText()
        body = ctx.exp4().accept(self)
        return UnaryOp(op, body)

    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return ctx.exp6().accept(self)

        op = ctx.getChild(0).getText()
        body = ctx.exp5().accept(self)
        return UnaryOp(op, body)

    #Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return ctx.exp7().accept(self)

        if ctx.LP():
            method = Id(ctx.ID().getText())
            idx = []
            num_function_call_exp = len(ctx.expression()) - len(ctx.LSB())
            funcall_exp = []
            for x in ctx.expression()[:num_function_call_exp]:
                funcall_exp.append(x.accept(self))

            arr = CallExpr(method, funcall_exp)

            for x in ctx.expression()[num_function_call_exp:]:
                idx.append(x.accept(self))

            return ArrayCell(arr, idx)
        else:
            arr = Id(ctx.ID().getText())
            idx = []
            for x in ctx.expression():
                idx.append(x.accept(self))

            return ArrayCell(arr, idx)

    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx: BKITParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return ctx.operands().accept(self)

        method = Id(ctx.ID().getText())
        param = []

        if ctx.expression():
            for x in ctx.expression():
                param.append(x.accept(self))

        return CallExpr(method, param)

    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx: BKITParser.OperandsContext):
        if ctx.getChildCount() == 1:
            if ctx.literal():
                return ctx.literal().accept(self)
            if ctx.parameter():
                variable, varDimen = ctx.parameter().accept(self)
                return variable

        if ctx.ID():
            method = Id(ctx.ID().getText())
            param = []
            if ctx.expression():
                for x in ctx.expression():
                    param.append(x.accept(self))
            return CallExpr(method, param)
        else:
            return ctx.expression(0).accept(self)

    # Visit a parse tree produced by BKITParser#array_literal.
    def visitArray_literal(self, ctx: BKITParser.Array_literalContext):
        #One value

        if not ctx.general_type():
            return ArrayLiteral([])

        return ArrayLiteral([x.accept(self) for x in ctx.general_type()])

    # Visit a parse tree produced by BKITParser#general_type.
    def visitGeneral_type(self, ctx: BKITParser.General_typeContext):
        #One value

        if ctx.array_literal():
            return ctx.array_literal().accept(self)

        if ctx.lit_type():
            return ctx.lit_type().accept(self)

    # Visit a parse tree produced by BKITParser#lit_type.
    def visitLit_type(self, ctx: BKITParser.Lit_typeContext):
        #One value

        if ctx.INTEGER_LITERAL():
            return IntLiteral(eval(ctx.INTEGER_LITERAL().getText()))

        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())

        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(eval(ctx.BOOLEAN_LITERAL().getText()))

        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
    

