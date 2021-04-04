import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    #
    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body:
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))
    #
    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    #
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))
    #
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))
    #
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))
    #
    # def test(self):
    #     """Complex program"""
    #     input = """
    #     Var: m[2][7] = {{1},{2}};
    #     Var: t = 7, f;
    #     Function: foo
    #     Parameter: x[2], y
    #     Body:
    #         Var: m = 3;
    #         y = y + goo(1,t,x);
    #     EndBody.
    #
    #     Function: goo
    #     Parameter: x,y,z[2]
    #     Body:
    #
    #     EndBody.
    #
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,400))
    #
    # def test(self):
    #
    #     #y = 3 + goo(1,t,r)
    #     """Complex program"""
    #     input = """
    #     Var: m[2][7] = {{1},{2}};
    #     Var: t = 7, x[2]={1,2}, r[2];
    #     Function: foo
    #         Parameter: f, y
    #         Body:
    #             Var: m = 3;
    #             goo(1,t,x);
    #             goo(1,f,r);
    #         EndBody.
    #
    #         Function: goo
    #         Parameter: x,y,z[2]
    #         Body:
    #
    #         EndBody.
    #
    #         """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    #
    # def test(self):
    #     # When update id -> update parameter
    #     """Complex program"""
    #     input = """
    #     Var: m[2][7] = {{1},{2}};
    #     Var: t = 7, x[2]={1,2}, r[2];
    #     Function: foo
    #         Parameter: foo, y
    #         Body:
    #             Var: m = 3;
    #             y = y + goo(1,2,x) + foo;
    #         EndBody.
    #
    #         Function: goo
    #         Parameter: x,y,z[2]
    #         Body:
    #
    #         EndBody.
    #
    #         """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    #
    #
    #
    # def test(self):
    #
    #     #y = 3 + goo(1,t,r)
    #     """Complex program"""
    #     input = """
    #     Var: m[2][7] = {{1},{2}};
    #     Var: t = 7, x[2]={1,2}, r[2][3];
    #     Function: foo
    #         Parameter: f, y[3][2]
    #         Body:
    #             Var: m = 3;
    #             goo(1,2,x);
    #         EndBody.
    #
    #         Function: goo
    #         Parameter: x,y,z[2]
    #         Body:
    #             Return;
    #         EndBody.
    #
    #         """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    #
    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body:
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """
                   Function: main
                   Body:
                       printStrLn(string_of_bool(1.0 =/= 1.0));
                       printStrLn(string_of_bool(-. 2.0 <=. -.2.0));
                       printStrLn(string_of_bool(2.0 <=. 1.0));
                       printStrLn(string_of_bool(1.0 >=. -. 1.0));
                       printStrLn(string_of_bool(1.0 >=. 1.0));
                       printStrLn(string_of_bool(-. 1.0 >. 1.0));
                       printStrLn(string_of_bool(1.0 >. 1.0));
                       printStrLn(string_of_bool(1.0 <. 1.0));
                       printStrLn(string_of_bool(1.0 <. -. 1.0));
                       printStrLn(string_of_bool(1.0 <. 2.0));
                       printStrLn(string_of_bool(1.0 >=. 2.0));
                   EndBody.
                   """
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 401))
    #
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    #
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"), [], ([], [
    #         CallExpr(Id("foo"), [])]))])
    #     expect = str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [
    #                 CallExpr(Id("read"), [IntLiteral(4)])
    #             ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    #
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    #
    #
    #
    #
    # def test_case_9(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x;
    #         x = test();
    #     EndBody.
    #     Function: test
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('x'), CallExpr(Id('test'), []))))
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    #
    # def test_case_10(self):
    #     input = """
    #     Function: main
    #     Body:
    #     EndBody.
    #     Function: test
    #     Parameter: x
    #     Body:
    #         x = 1;
    #         test(1.4);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('test'), [FloatLiteral(1.4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    #
    # def test_case_11(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: x;
    #         test(x);
    #     EndBody.
    #     Function: test
    #     Parameter: x
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id('test'), [Id('x')])))
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    #
    # def test_case_12(self):
    #     input = """
    #     Function: main
    #     Body:
    #         test(1, 2.2);
    #         test(1, 2);
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('test'), [IntLiteral(1), IntLiteral(2)])))
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    #
    # def test_case_14(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         x[0] = 1;
    #         x[1] = "s";
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(1)]),StringLiteral("""s"""))))
    #     self.assertTrue(TestChecker.test(input,expect,413))
    #
    # def test_case_15(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         test()[0] = 1;
    #         test()[1] = "s";
    #     EndBody.
    #     Function: test
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(0)]),IntLiteral(1))))
    #     self.assertTrue(TestChecker.test(input,expect,414))
    #
    # def test_case_16(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: x;
    #         If x Then
    #             Return 1;
    #         EndIf.
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('x'))))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    #
    # def test_case_16(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: x;
    #         If x Then
    #             Return 1;
    #         EndIf.
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('x'))))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    #
    # def test_case_21(self):
    #     input = """
    #     Var: x[10][10];
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         Var: v;
    #         v = f(flag);
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         Return foo();
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('v'),CallExpr(Id('f'),[Id('flag')]))))
    #     self.assertTrue(TestChecker.test(input,expect,420))
    #
    # def test_case_22(self):
    #     input = """
    #     Var: x[10][10], m, k;
    #     Function: test
    #     Body:
    #         Return m + k;
    #     EndBody.
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         test();
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[])))
    #     self.assertTrue(TestChecker.test(input,expect,421))
    #
    # def test_case_23(self):
    #     input = """
    #     Var: x[10][10], m, k;
    #     Function: test
    #     Body:
    #         Return m + k + x[0][1];
    #     EndBody.
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         flag = test();
    #         x[3][2] = 1.2;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(3),IntLiteral(2)]),FloatLiteral(1.2))))
    #     self.assertTrue(TestChecker.test(input,expect,422))
    #
    # def test_case_25(self):
    #     input = """
    #     Function: f1
    #     Parameter: x
    #     Body:
    #         Return {0};
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[1];
    #         Var: n;
    #         f1(f2(f3(n)))[0] = a[f3(f2(n))];
    #     EndBody.
    #     Function: f2
    #     Parameter: x
    #     Body:
    #         Return 0;
    #     EndBody.
    #     Function: f3
    #     Parameter: x
    #     Body:
    #         Return 0;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f1'),[CallExpr(Id('f2'),[CallExpr(Id('f3'),[Id('n')])])]),[IntLiteral(0)]),ArrayCell(Id('a'),[CallExpr(Id('f3'),[CallExpr(Id('f2'),[Id('n')])])]))))
    #     self.assertTrue(TestChecker.test(input,expect,424))
    #
    # def test_case_26(self):
    #     input = """
    #     Var: x, y;
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t;
    #         t = 10 + foo(2);
    #         t = t +. factorial(t);
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),CallExpr(Id('factorial'),[Id('t')]))))
    #     self.assertTrue(TestChecker.test(input,expect,425))
    #
    #
    #
    # def test_case_28(self):
    #     input = """
    #     Var: x, y, arr[5];
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t, a;
    #         t = 10 + foo(2);
    #         t = factorial(get_arr()[2]);
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     Function: get_arr
    #     Body:
    #         arr = {1, 2, 3, 4, 5};
    #         Return arr;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('t'),CallExpr(Id('factorial'),[ArrayCell(CallExpr(Id('get_arr'),[]),[IntLiteral(2)])]))))
    #     self.assertTrue(TestChecker.test(input,expect,427))
    #
    # def test_case_29(self):
    #     input = """
    #     Var: x, y, arr[5];
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t, a;
    #         t = 10 + foo(2);
    #         t = factorial(t);
    #         arr = get_arr();
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     Function: get_arr
    #     Body:
    #         Var: arr = {1, 2, 3, 4, 5, 6};
    #         Return arr;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('arr'),CallExpr(Id('get_arr'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,428))
    #
    # def test_case_30(self):
    #     input = """
    #     Var: x, y, arr[5];
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: get_arr
    #     Body:
    #         arr = {1, 2, 3, 4, 5};
    #         Return arr;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t;
    #         t = 10 + foo(2);
    #         arr[0] = t;
    #         t = factorial(foo(factorial(foo(arr[3])))) + t + foo(2) + foo(get_arr()[foo(t)]);
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input,expect,429))
    #
    # def test_case_31(self):
    #     input = """
    #     Var: a, b[4][12], c;
    #     Function: test
    #     Body:
    #         func()[2][1] = 14;
    #     EndBody.
    #     Function: func
    #     Body:
    #         Return b;
    #     EndBody.
    #     Function: main
    #     Body:
    #         func()[3][1] = 0;
    #         b[0][0] = c;
    #         test();
    #         func()[c][2 + 1 * 1] = b[0][c];
    #         If False Then
    #             While True Do
    #             EndWhile.
    #             Break;
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('func'),[]),[IntLiteral(2),IntLiteral(1)]),IntLiteral(14))))
    #     self.assertTrue(TestChecker.test(input, expect, 430))
    #
    # def test_case_32(self):
    #     input = """
    #     Var: a, b[4][2], c;
    #     Function: test
    #     Body:
    #         func()[2][1] = 14;
    #     EndBody.
    #     Function: func
    #     Body:
    #         Return b;
    #     EndBody.
    #     Function: main
    #     Body:
    #         func()[3][1] = 0;
    #         b[0][0] = "s";
    #         test();
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('func'),[]),[IntLiteral(2),IntLiteral(1)]),IntLiteral(14))))
    #     self.assertTrue(TestChecker.test(input, expect, 431))
    #
    # def test_case_34(self):
    #     input = """
    #     Var: a, b[2][4][2];
    #     Function: main
    #     Body:
    #         Var: temp;
    #        printStrLn(a);
    #        test(temp);
    #     EndBody.
    #     Function: test
    #     Parameter: p
    #     Body:
    #         printStr(read());
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[Id('temp')])))
    #     self.assertTrue(TestChecker.test(input, expect, 433))
    #
    # def test_case_35(self):
    #     input = """
    #     Var: a, b[2][2], c;
    #     Function: main
    #     Body:
    #        b[f()][f()] = 123;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: c[2][3];
    #         b = c;
    #         Return 1;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('b'),Id('c'))))
    #     self.assertTrue(TestChecker.test(input, expect, 434))
    #
    # def test_case_37(self):
    #     input = """
    #     Var: a, b;
    #     Function: main
    #     Parameter: x, y, k, t, a, x
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(Redeclared(Parameter(), 'x'))
    #     self.assertTrue(TestChecker.test(input, expect, 436))
    #
    # def test_case_38(self):
    #     input = """
    #     Var: a, b;
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     Function: a
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(Redeclared(Function(), 'a'))
    #     self.assertTrue(TestChecker.test(input, expect, 437))
    #
    #
    # def test_case_40(self):
    #     input = """
    #     Var: a, b;
    #     Function: f
    #     Parameter: a, b
    #     Body:
    #         Var: flags[2][4];
    #         flags[0][0] = (9. =/= t()) || f(a * b, a)[1][2];
    #         Return flags;
    #     EndBody.
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         Do
    #             a = x + y;
    #             b = float_of_int(a);
    #         While f(x, y)[1][2] EndDo.
    #     EndBody.
    #     Function: t
    #     Body:
    #         Return t() *. 0.1;
    #     EndBody.
    #     Function: mm
    #     Body:
    #         a = int_of_float(b);
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('flags'),[IntLiteral(0),IntLiteral(0)]),BinaryOp('||',BinaryOp('=/=',FloatLiteral(9.0),CallExpr(Id('t'),[])),ArrayCell(CallExpr(Id('f'),[BinaryOp('*',Id('a'),Id('b')),Id('a')]),[IntLiteral(1),IntLiteral(2)])))))
    #     self.assertTrue(TestChecker.test(input, expect, 439))
    #
    # def test_case_42(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         f()[2][3] = a * 2;
    #         arr[0][2] = "PPL!!! hard!!!";
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return arr;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2),IntLiteral(3)]),BinaryOp('*',Id('a'),IntLiteral(2)))))
    #     self.assertTrue(TestChecker.test(input, expect, 441))
    #
    # def test_case_43(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         reaD()[2][3] = a * 2;
    #         arr[0][2] = "PPL!!! hard!!!";
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Function(), 'reaD'))
    #     self.assertTrue(TestChecker.test(input, expect, 442))
    #
    # def test_case_42(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         f()[2][3] = a * 2;
    #         arr[0][2] = "PPL!!! hard!!!";
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return arr;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2),IntLiteral(3)]),BinaryOp('*',Id('a'),IntLiteral(2)))))
    #     self.assertTrue(TestChecker.test(input, expect, 441))
    #
    # def test_case_43(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         reaD()[2][3] = a * 2;
    #         arr[0][2] = "PPL!!! hard!!!";
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Function(), 'reaD'))
    #     self.assertTrue(TestChecker.test(input, expect, 442))
    #
    # def test_case_44(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * c[2][3];
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'c'))
    #     self.assertTrue(TestChecker.test(input, expect, 443))
    #
    # def test_case_45(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * int_of_string(arr[1][2]);
    #     EndBody.
    #     Function: test
    #     Parameter: m
    #     Body:
    #         Return arr[a + b];
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('arr'),[BinaryOp('+',Id('a'),Id('b'))])))
    #     self.assertTrue(TestChecker.test(input, expect, 444))
    #
    #
    # def test_case_47(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * int_of_string(arr[1][2]);
    #         foo();
    #         arr[1][0] = test(2);
    #     EndBody.
    #     Function: test
    #     Parameter: m
    #     Body:
    #         Return arr[a + b][int_of_float(float_of_string(arr[1][0]))];
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return;
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 446))
    #
    # def test_case_8(self):
    #     input = """
    #     Function: test
    #     Body:
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: x = 1;
    #         x = test();
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('test'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,407))
    #
    # def test_case_48(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * int_of_string(arr[1][2]);
    #         foo();
    #     EndBody.
    #     Function: test
    #     Parameter: m
    #     Body:
    #         test(int_of_float(float_of_int(m)));
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return test(b);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(CallExpr(Id('test'),[Id('b')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 447))
    #
    # def test_case_90(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         Do
    #             printStrLn(b[2]);
    #         While f()[2] EndDo.
    #     EndBody.
    #     Function: f
    #     Body:
    #         b[1] = "dasd";
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Dowhile(([],[CallStmt(Id('printStrLn'),[ArrayCell(Id('b'),[IntLiteral(2)])])]),ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 489))
    #
    # def test_case_91(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         Do
    #             printStrLn(b[2]);
    #         While f(a[7]) EndDo.
    #     EndBody.
    #     Function: f
    #     Parameter: k
    #     Body:
    #         b[1] = "dasd";
    #         Return True;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Dowhile(([],[CallStmt(Id('printStrLn'),[ArrayCell(Id('b'),[IntLiteral(2)])])]),CallExpr(Id('f'),[ArrayCell(Id('a'),[IntLiteral(7)])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 490))
    #
    # def test_case_94(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo()[2] == x Then
    #         ElseIf b[2] && (b[0] || b[4]) Then
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(If([(BinaryOp('==',ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),Id('x')),[],[]),(BinaryOp('&&',ArrayCell(Id('b'),[IntLiteral(2)]),BinaryOp('||',ArrayCell(Id('b'),[IntLiteral(0)]),ArrayCell(Id('b'),[IntLiteral(4)]))),[],[])], ([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 493))
    #
    # def test_case_95(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If b[2] == 2 Then
    #         ElseIf b[2] && (b[0] || b[4]) Then
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp('&&',ArrayCell(Id('b'),[IntLiteral(2)]),BinaryOp('||',ArrayCell(Id('b'),[IntLiteral(0)]),ArrayCell(Id('b'),[IntLiteral(4)])))))
    #     self.assertTrue(TestChecker.test(input, expect, 494))
    #
    # def test_case_96(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         Var: i;
    #         If b[2] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #             a = foo(i);
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('a'),CallExpr(Id('foo'),[Id('i')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 495))
    #
    # def test_case_97(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         Var: i;
    #         If b[2] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #             f();
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: f
    #     Body:
    #         foo(float_to_int(x))[2] = string_of_int(b[x]);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[CallExpr(Id('float_to_int'),[Id('x')])]),[IntLiteral(2)]),CallExpr(Id('string_of_int'),[ArrayCell(Id('b'),[Id('x')])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 496))
    #
    # def test_case_98(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo(float_of_int(x))[3] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #         EndIf.
    #         foo(0e-2)[9] = b[x + 2]*b[x + foo(1e-2)[9]] - a[a[a[a[x]]]];
    #     EndBody.
    #
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 497))
    #
    # def test_case_99(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo(float_of_int(x))[3] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #         EndIf.
    #         foo(0e-2)[9] = b[x + 2]*b[x + foo(1e-2)[2 + foo(2.0202)[0 * foo(1.2)[x \ 2]]]] - a[a[a[a[x]]]];
    #     EndBody.
    #
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 498))
    #
    # def test_case_101(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo(float_of_int(x))[3] == 2 Then
    #             Return 0;
    #         ElseIf b[x] != b[0] Then
    #         EndIf.
    #         foo(0e-2)[9] = b[x + 2]*b[x + foo(1e-2)[2 + foo(2.0202)[0 * foo(1.2)[foo(2.3)[4 % 2 + 6 % 3 + 2 * 4] * x \ 2]]]] - a[a[a[a[x]]]];
    #         If True Then
    #             Return x;
    #         Else
    #             Return a[0];
    #         EndIf.
    #     EndBody.
    #
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 500))
    #
    # def test_case_113(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: main
    #     Body:
    #         Var: k;
    #         k = -x[foo(x[0])];
    #         x = f();
    #     EndBody.
    #     Function: foo
    #     Parameter: y
    #     Body:
    #         Return y;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: k[10];
    #         If k[2] Then
    #             Return k;
    #         EndIf.
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('k'))))
    #     self.assertTrue(TestChecker.test(input, expect, 512))
    #
    #
    #
    # def test_case_36(self):
    #     input = """
    #     Var: a, b[2][2], c;
    #     Function: test
    #     Parameter: k
    #     Body:
    #         Do
    #             test(1);
    #         While k EndDo.
    #     EndBody.
    #     Function: main
    #     Body:
    #        b[f()][f()] = 123;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: c[2][3];
    #         Return 1;
    #     EndBody.
    #     """
    #     expect =  str(TypeMismatchInStatement(Dowhile(([],[CallStmt(Id('test'),[IntLiteral(1)])]),Id('k'))))
    #     self.assertTrue(TestChecker.test(input, expect, 435))
    #
    # def test_case_66(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         Var: y, z;
    #         x[2] = x[0o3] || (y > z);
    #         While x[2] && x[3] Do
    #             Do
    #                 printStrLn(string_of_int(y * z));
    #                 If x[0] Then
    #                     Return 1;
    #                 ElseIf x[1] Then
    #                     Return z;
    #                 Else
    #                     Var: k;
    #                     k = 10;
    #                 EndIf.
    #                 z = y;
    #             While x[4] EndDo.
    #         EndWhile.
    #         Return z % y;
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 465))
    #
    #
    # def test_case_92(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         For(x = a[9], f(x)[3], x) Do
    #             x = x * a[2] - f(a[2])[1];
    #         EndFor.
    #     EndBody.
    #     Function: f
    #     Parameter: k
    #     Body:
    #         b[1] = "dasd";
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(For(Id('x'),ArrayCell(Id('a'),[IntLiteral(9)]),ArrayCell(CallExpr(Id('f'),[Id('x')]),[IntLiteral(3)]),Id('x'), ([],[Assign(Id('x'),BinaryOp('-',BinaryOp('*',Id('x'),ArrayCell(Id('a'),[IntLiteral(2)])),ArrayCell(CallExpr(Id('f'),[ArrayCell(Id('a'),[IntLiteral(2)])]),[IntLiteral(1)])))]))))
    #     self.assertTrue(TestChecker.test(input, expect, 491))
    #
    # def test_case_24(self):
    #     input = """
    #     Var: x[10][10], m, k;
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         For(flag = 1, f("a"), foo()) Do
    #         EndFor.
    #         Return flag;
    #     EndBody.
    #     Function: f
    #     Parameter: p
    #     Body:
    #         Return main(p) == 1;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x[0][1] * m + k;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[Id('p')])))
    #     self.assertTrue(TestChecker.test(input,expect,423))
    #
    # def test_case_41(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         For(a = f()[1][2], c()[1 + 2][fe()][fe()][fe()], arr[1][1]) Do
    #         EndFor.
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return arr;
    #     EndBody.
    #     Function: c
    #     Body:
    #         Var: a[2][3][4][5];
    #         Return a;
    #     EndBody.
    #     Function: fe
    #     Body:
    #         Return float_of_int(b);
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(For(Id('a'),ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(1),IntLiteral(2)]),ArrayCell(CallExpr(Id('c'),[]),[BinaryOp('+',IntLiteral(1),IntLiteral(2)),CallExpr(Id('fe'),[]),CallExpr(Id('fe'),[]),CallExpr(Id('fe'),[])]),ArrayCell(Id('arr'),[IntLiteral(1),IntLiteral(1)]), ([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 440))
    #
    # def test_case_58(self):
    #     input = """
    #     Var: a, b[2][2], c;
    #     Function: test
    #     Parameter: k
    #     Body:
    #         Do
    #             test(1);
    #         While k EndDo.
    #     EndBody.
    #     Function: main
    #     Body:
    #        b[f()][f()] = 123;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: c[2][3];
    #         Return 1;
    #     EndBody.
    #     """
    #     expect =  str(TypeMismatchInStatement(Dowhile(([],[CallStmt(Id('test'),[IntLiteral(1)])]),Id('k'))))
    #     self.assertTrue(TestChecker.test(input, expect, 457))
    #
    # def test_case_68(self):
    #     input = """
    #     Var: x[10];
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         b = x[5] * b % 4;
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         t = 4;
    #         a = foo(t, 4);
    #         z = foo(a[2], t)[2];
    #         a[2] = float_to_int(z);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[IntLiteral(2)]),CallExpr(Id('float_to_int'),[Id('z')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 467))
    #
    #
    # def test_case_56(self):
    #     input = """
    #     Var: x[10];
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         b = x[5] * b % 4;
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         t = 4;
    #         a = foo(t, 4);
    #         z = foo(a[2], t)[2];
    #         a[2] = float_of_int(z);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(ArrayCell(Id('a'), [IntLiteral(2)]), CallExpr(Id('float_of_int'), [Id('z')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 455))
    #
    #
    # def test_case_59(self):
    #     input = """
    #     Var: x, y, arr[5];
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t, a;
    #         t = 10 + foo(2);
    #         t = factorial(t);
    #         arr = get_arr();
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     Function: get_arr
    #     Body:
    #         Var: arr = {1, 2, 3, 4, 5};
    #         Return arr;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('arr'),CallExpr(Id('get_arr'),[]))))
    #     self.assertTrue(TestChecker.test(input,expect,458))
    #
    # def test_case_60(self):
    #     input = """
    #     Var: x[10][10];
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         Var: v;
    #         v = f(flag);
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         Return foo();
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('v'),CallExpr(Id('f'),[Id('flag')]))))
    #     self.assertTrue(TestChecker.test(input,expect,459))
    #
    # def test_case_62(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         Var: s, x, y, t;
    #         s = read();
    #         x = length(s) * 2;
    #         t = length(x);
    #     EndBody.
    #     Function: length
    #     Parameter: s
    #     Body:
    #         Return 100;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('length'),[Id('x')])))
    #     self.assertTrue(TestChecker.test(input, expect, 461))
    #
    # def test_case_63(self):
    #     input = """
    #     Var: x[10];
    #     Function: test
    #     Parameter: flag
    #     Body:
    #         Var: s, x, y, t;
    #         s = read();
    #         x = length(s) * 2;
    #         t = length(flag);
    #         Return flag;
    #     EndBody.
    #     Function: length
    #     Parameter: s
    #     Body:
    #         Return 100;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: z;
    #         z = test(x[0]);
    #         x[0] = t;
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 't'))
    #     self.assertTrue(TestChecker.test(input, expect, 462))
    #
    # def test_case_65(self):
    #     input = """
    #     Var: x[10];
    #     Function: test
    #     Parameter: flag
    #     Body:
    #         Var: s, x, y, t;
    #         s = read();
    #         x = length(s) * 2;
    #         t = length(flag);
    #         Return flag;
    #     EndBody.
    #     Function: length
    #     Parameter: s
    #     Body:
    #         Return 100;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: z;
    #         z = test(x[0]);
    #         x[1] = z;
    #         printStrLn(string_of_int(length(z)));
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 464))
    #
    #
    # def test_case_27(self):
    #     input = """
    #     Var: x, y, arr[5];
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: get_arr
    #     Body:
    #         arr = {1, 2, 3, 4, 5};
    #         Return arr;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: t, a[5];
    #         t = 10 + foo(2);
    #         a = get_arr();
    #         t = a[4] - factorial(t);
    #     EndBody.
    #     Function: factorial
    #     Parameter: n
    #     Body:
    #         If (n == 0) || (n == 1) Then
    #             Return 1;
    #         EndIf.
    #         Return n * factorial(n - 1);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input,expect,426))
    #
    # def test_case_67(self):
    #     input = """
    #     Var: x[10];
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         t = 4;
    #         a[0] = t;
    #         a = foo(t, 4);
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Return(Id('x'))))
    #     self.assertTrue(TestChecker.test(input, expect, 466))
    #
    #
    #
    # def test_case_69(self):
    #     input = """
    #     Var: x[10];
    #     Function: foo
    #     Parameter: a, b
    #     Body:
    #         b = x[5] * b % 4;
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         t = 4;
    #         foo(t, t)[2] = a[2];
    #         a[int_of_float(4.3 *. 2.4 \. 0.1)] = z || (t > x[1]);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[CallExpr(Id('int_of_float'),[BinaryOp('\.',BinaryOp('*.',FloatLiteral(4.3),FloatLiteral(2.4)),FloatLiteral(0.1))])]),BinaryOp('||',Id('z'),BinaryOp('>',Id('t'),ArrayCell(Id('x'),[IntLiteral(1)]))))))
    #     self.assertTrue(TestChecker.test(input, expect, 468))
    #
    # def test_case_70(self):
    #     input = """
    #     Var: x[10];
    #     Function: foo
    #     Body:
    #         x[2] = 2;
    #         Return x;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         a[9] = t * z % x[1];
    #         a[2] = foo()[2];
    #         foo()[4] = 4.3;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(4)]),FloatLiteral(4.3))))
    #     self.assertTrue(TestChecker.test(input, expect, 469))
    #
    # def test_case_71(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         a[9] = t * z;
    #         a = foo();
    #         foo()[2] = 3.4;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),FloatLiteral(3.4))))
    #     self.assertTrue(TestChecker.test(input, expect, 470))
    #
    # def test_case_72(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         Var: a[10], t, z;
    #         a[t] = t +. 2.;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),FloatLiteral(2.0))))
    #     self.assertTrue(TestChecker.test(input, expect, 471))
    #
    # def test_case_73(self):
    #     input = """
    #     Function: main
    #     Parameter: x
    #     Body:
    #         Var: y, z;
    #         y = x && (x == z);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp('==',Id('x'),Id('z'))))
    #     self.assertTrue(TestChecker.test(input, expect, 472))
    #
    # def test_case_74(self):
    #     input = """
    #     Var: a[2] = {0, 1};
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Return a;
    #     EndBody.
    #
    #     Function: main
    #         Body:
    #             foo(0)[0] = foo(0.0)[1 * a[1]];
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[FloatLiteral(0.0)])))
    #     self.assertTrue(TestChecker.test(input, expect, 473))
    #
    # def test_case_75(self):
    #     input = """
    #     Var: a[2] = {0, 1};
    #     Function: foo
    #     Parameter: x
    #     Body:
    #     EndBody.
    #
    #     Function: main
    #         Body:
    #             foo(0);
    #             foo("a");
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[StringLiteral("""a""")])))
    #     self.assertTrue(TestChecker.test(input, expect, 474))
    #
    # def test_case_76(self):
    #     input = """
    #     Function: foo
    #     Body:
    #     EndBody.
    #
    #     Function: main
    #     Parameter: x
    #     Body:
    #         main(foo());
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[CallExpr(Id('foo'),[])])))
    #     self.assertTrue(TestChecker.test(input, expect, 475))
    #
    # def test_case_77(self):
    #     input = """
    #     Var: arr[2][3] = {{2, 3, 1}, {3, 1, 0}};
    #     Function: main
    #     Parameter: x
    #     Body:
    #         arr = {{2, 1}, {7, 3}, {2, 5}};
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('arr'),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(1)]),ArrayLiteral([IntLiteral(7),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(5)])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 476))
    #
    #
    #
    # def test_case_81(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         x = x + test(x, 1);
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #         Return x + y;
    #     EndBody.
    #     """
    #     expect =  str()
    #     self.assertTrue(TestChecker.test(input, expect, 480))
    #
    # def test_case_83(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: test
    #     Body:
    #         a[0] = a[5] * b[2];
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         test();
    #         a[2][3] = 10;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(2),IntLiteral(3)])))
    #     self.assertTrue(TestChecker.test(input, expect, 482))
    #
    # def test_case_84(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         test(foo() * x, f(2, 4)[2] - b[2]);
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id('test'),[BinaryOp('*',CallExpr(Id('foo'),[]),Id('x')),BinaryOp('-',ArrayCell(CallExpr(Id('f'),[IntLiteral(2),IntLiteral(4)]),[IntLiteral(2)]),ArrayCell(Id('b'),[IntLiteral(2)]))])))
    #     self.assertTrue(TestChecker.test(input, expect, 483))
    #
    # def test_case_88(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         a[0] = test() * b[2];
    #     EndBody.
    #     Function: test
    #     Body:
    #         Return f(2, x);
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         a[0] = 10;
    #         Return 1;
    #     EndBody.
    #     """
    #     expect =  str(TypeCannotBeInferred(Return(CallExpr(Id('f'),[IntLiteral(2),Id('x')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 487))
    #
    # def test_case_89(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         a[0] = test() * b[2];
    #     EndBody.
    #     Function: test
    #     Body:
    #         Return f(2, 5)[x];
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         a[0] = 10;
    #         Return 1;
    #     EndBody.
    #     """
    #     expect =  str(TypeCannotBeInferred(Return(ArrayCell(CallExpr(Id('f'),[IntLiteral(2),IntLiteral(5)]),[Id('x')]))))
    #     self.assertTrue(TestChecker.test(input, expect, 488))
    #
    # def test_case_93(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         x = f(f(b[2])[2] * x \ 10)[2] * a[1];
    #     EndBody.
    #     Function: f
    #     Parameter: k
    #     Body:
    #         b[1] = "dasd";
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('x'),BinaryOp('*',ArrayCell(CallExpr(Id('f'),[BinaryOp('\\',BinaryOp('*',ArrayCell(CallExpr(Id('f'),[ArrayCell(Id('b'),[IntLiteral(2)])]),[IntLiteral(2)]),Id('x')),IntLiteral(10))]),[IntLiteral(2)]),ArrayCell(Id('a'),[IntLiteral(1)])))))
    #     self.assertTrue(TestChecker.test(input, expect, 492))
    #
    # def test_case_104(self):
    #     input = """
    #     Function: print
    #     Parameter: x
    #     Body:
    #         Return;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Var: value = 12345;
    #         Return value;
    #     EndBody.
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         print(foo);
    #         x = foo();
    #         Return 0;
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'foo'))
    #     self.assertTrue(TestChecker.test(input, expect, 503))
    #
    # def test_case_105(self):
    #     input = """
    #     Var: a;
    #     Function: main
    #     Body:
    #         foo();
    #         a = 1;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         a = 1.1;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('a'),FloatLiteral(1.1))))
    #     self.assertTrue(TestChecker.test(input, expect, 504))
    # def test_case_106(self):
    #     input = """
    #     Function: main
    #     Parameter: a,b,c
    #     Body:
    #         Var: d, e;
    #         e = main(b, main(d, a, c), a + d);
    #         e = 3.0;
    #         Return 3;
    #
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('e'),CallExpr(Id('main'),[Id('b'),CallExpr(Id('main'),[Id('d'),Id('a'),Id('c')]),BinaryOp('+',Id('a'),Id('d'))]))))
    #     self.assertTrue(TestChecker.test(input, expect, 505))
    #
    #
    # def test_case_49(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: foo
    #     Body:
    #         Return;
    #     EndBody.
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         Var: k;
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * int_of_string(arr[1][2]);
    #         foo();
    #         k = foo();
    #     EndBody.
    #     Function: test
    #     Parameter: m
    #     Body:
    #         test(int_of_float(float_of_int(m)));
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('k'),CallExpr(Id('foo'),[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 448))
    #
    # def test_case_50(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         foo(a + b);
    #     EndBody.
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #         foo(1, 2.2);
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[BinaryOp('+',Id('a'),Id('b'))])))
    #     self.assertTrue(TestChecker.test(input, expect, 449))
    #
    # def test_case_53(self):
    #     input = """
    #     Var: a, b, arr[10][10], array[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         arr = array;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('arr'),Id('array'))))
    #     self.assertTrue(TestChecker.test(input, expect, 452))
    #
    # def test_case_54(self):
    #     input = """
    #     Var: a, b, arr[3][2];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         a[2][3] = b * y - x % main;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(2),IntLiteral(3)])))
    #     self.assertTrue(TestChecker.test(input, expect, 453))
    #
    # def test_case_55(self):
    #     input = """
    #     Var: x[10];
    #     Function: test
    #     Parameter: flag
    #     Body:
    #         Var: s, x, y, t;
    #         s = read();
    #         x = length(s) * 2;
    #         t = length(flag);
    #         Return flag;
    #     EndBody.
    #     Function: length
    #     Parameter: s
    #     Body:
    #         Return 100;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: z;
    #         z = test(x[0]);
    #         x[1] = z;
    #         printStrLn(string_of_int(length(z)));
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 454))
    #
    # def test_case_107(self):
    #     input = """
    #     Function: foo
    #     Body:
    #         Return;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: a;
    #         a = foo;
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'foo'))
    #     self.assertTrue(TestChecker.test(input, expect, 506))
    # def test_case_108(self):
    #     input = """
    #     Function: main
    #     Body:
    #         Var: a;
    #         a = foo;
    #         foo(2.4);
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         x = 10.0;
    #         Return;
    #     EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), 'foo'))
    #     self.assertTrue(TestChecker.test(input, expect, 507))
    #
    # def test_case_109(self):
    #     input = """
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         Return x + main(y, x);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 508))
    # def test_case_110(self):
    #     input = """
    #     Function: main
    #     Parameter: x, y
    #     Body:
    #         Return x + main(y, x);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 509))
    #
    # def test_case_114(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: main
    #     Body:
    #
    #         foo(x);
    #     EndBody.
    #     Function: foo
    #     Parameter: y
    #     Body:
    #
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [Id('x')])))
    #     self.assertTrue(TestChecker.test(input, expect, 513))
    #
    # def test_case_115(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y[10]
    #     Body:
    #
    #     EndBody.
    #     Function: main
    #     Body:
    #         foo(x);
    #     EndBody.
    #
    #     """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id('foo'), [Id('x')])))
    #     self.assertTrue(TestChecker.test(input, expect, 514))
    #
    # def test_case_116(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y
    #     Body:
    #     EndBody.
    #     Function: main
    #     Body:
    #         foo(1);
    #         foo(x[0]);
    #         x[0] = "s";
    #     EndBody.
    #
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(0)]), StringLiteral("""s"""))))
    #     self.assertTrue(TestChecker.test(input, expect, 515))
    #
    # def test_case_117(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y
    #     Body:
    #         Return 1;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         m = foo(x[0]);
    #     EndBody.
    #
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id('m'), CallExpr(Id('foo'), [ArrayCell(Id('x'), [IntLiteral(0)])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 516))
    #
    # def test_case_118(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y
    #     Body:
    #         Return 1;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         m = foo(x);
    #     EndBody.
    #
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [Id('x')])))
    #     self.assertTrue(TestChecker.test(input, expect, 517))
    #
    # def test_case_119(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y
    #     Body:
    #         Return 1 + y;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         m = foo(x[0]);
    #         x[1] = 2.2;
    #     EndBody.
    #
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(1)]), FloatLiteral(2.2))))
    #     self.assertTrue(TestChecker.test(input, expect, 518))
    #
    # def test_case_120(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y[10]
    #     Body:
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         foo(f());
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return x;
    #     EndBody.
    #
    #
    #     """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id('foo'), [CallExpr(Id('f'), [])])))
    #     self.assertTrue(TestChecker.test(input, expect, 519))
    #
    # def test_case_121(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y[10]
    #     Body:
    #         y[0] = 1;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         foo(f());
    #         x[1] = 2.2;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('x'))))
    #     self.assertTrue(TestChecker.test(input, expect, 520))
    #
    # def test_case_122(self):
    #     input = """
    #     Var: x[10], y;
    #     Function: foo
    #     Parameter: y
    #     Body:
    #         y = y * 10;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: m;
    #         foo(f());
    #         x[1] = 2.2;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(Id('x'))))
    #     self.assertTrue(TestChecker.test(input, expect, 521))
    #
    # def test_case_7(self):
    #     input = """
    #     Function: test
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input,expect,406))
    #
    # def test_case_46(self):
    #     input = """
    #     Var: a, b, arr[10][10], main;
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #         arr[0][2] = "PPL!!! hard!!!";
    #         b = a * int_of_string(arr[1][2]);
    #     EndBody.
    #     Function: test
    #     Parameter: m
    #     Body:
    #         Return arr[a + b][int_of_float(float_of_string(arr[1][0]))];
    #     EndBody.
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 445))
    #
    # def test_case_64(self):
    #     input = """
    #     Var: x[10];
    #     Function: test
    #     Parameter: flag
    #     Body:
    #         Var: s, x, y, t;
    #         s = read();
    #         x = length(s) * 2;
    #         t = length(flag);
    #         Return flag;
    #     EndBody.
    #     Function: length
    #     Parameter: s
    #     Body:
    #         Return 100;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Var: z;
    #         z = test(x[0]);
    #         x[1] = z;
    #     EndBody.
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 463))
    #
    # def test_case_16(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: x, y;
    #         If foo()[1] Then
    #             Return 1;
    #         EndIf.
    #         Return y;
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return 1;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(If([(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),[],[Return(IntLiteral(1))])], ([],[]))))
    #     self.assertTrue(TestChecker.test(input,expect,415))
    #
    # def test_case_17(self):
    #     input = """
    #     Var: x[10];
    #     Function: test
    #     Parameter: y
    #     Body:
    #         Var: x;
    #         If foo()[1] Then
    #             Return 1;
    #         ElseIf f(1) Then
    #         EndIf.
    #         Return y;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: k;
    #         k = test(1.5);
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return {True, False, True};
    #     EndBody.
    #     Function: f
    #     Parameter: k
    #     Body:
    #         Return k == 1;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(If([(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),[],[Return(IntLiteral(1))]),(CallExpr(Id('f'),[IntLiteral(1)]),[],[])], ([],[]))))
    #     self.assertTrue(TestChecker.test(input,expect,416))
    #
    # def test_case_79(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         test();
    #     EndBody.
    #     Function: test
    #     Body:
    #         If x Then
    #             foo();
    #         Else
    #             test();
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 478))
    #
    # def test_case_18(self):
    #     input = """
    #     Var: x[10][10];
    #     Function: main
    #     Body:
    #         Var: k;
    #         If 1 == f()[1][2] Then
    #         ElseIf x[0][0] Then
    #         EndIf.
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: x[10][10];
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(If([(BinaryOp('==',IntLiteral(1),ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(1),IntLiteral(2)])),[],[]),(ArrayCell(Id('x'),[IntLiteral(0),IntLiteral(0)]),[],[])], ([],[]))))
    #     self.assertTrue(TestChecker.test(input,expect,417))
    #
    # def test_case_19(self):
    #     input = """
    #     Var: x[10][10];
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         If flag == f(1)[0][1] Then
    #         EndIf.
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         Return foo();
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(If([(BinaryOp('==',Id('flag'),ArrayCell(CallExpr(Id('f'),[IntLiteral(1)]),[IntLiteral(0),IntLiteral(1)])),[],[])], ([],[]))))
    #     self.assertTrue(TestChecker.test(input,expect,418))
    #
    #
    # def test_case_20(self):
    #     input = """
    #     Var: x[10][10];
    #     Function: main
    #     Parameter: flag
    #     Body:
    #         f("s")[2][3] = 100;
    #         If f("a")[0][1] == foo()[1][2] Then
    #             f(flag)[1][3] = 0o10;
    #         EndIf.
    #         flag = 12;
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         Return foo();
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'),[StringLiteral("""s""")]),[IntLiteral(2),IntLiteral(3)]),IntLiteral(100))))
    #     self.assertTrue(TestChecker.test(input,expect,419))
    #
    #
    # def test_case_33(self):
    #     input = """
    #     Var: x, y = "s", t, arr[10];
    #     Function: main
    #     Body:
    #
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Var: arr[2];
    #         If x Then
    #             Return int_of_string(string_of_bool(x));
    #         ElseIf f(x) Then
    #             Return foo(bool_of_string(arr[0]));
    #         EndIf.
    #         Return 0;
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         If bool_of_string(string_of_bool(x)) Then
    #             Return x;
    #         EndIf.
    #         Return;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(None)))
    #     self.assertTrue(TestChecker.test(input, expect, 432))
    #
    # def test_case_51(self):
    #     input = """
    #     Var: a, b, arr[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         If main && x Then
    #             Return y + 1;
    #         EndIf.
    #         Return arr[0][0];
    #     EndBody.
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #         arr[0][1] = "s";
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('arr'),[IntLiteral(0),IntLiteral(1)]),StringLiteral("""s"""))))
    #     self.assertTrue(TestChecker.test(input, expect, 450))
    #
    # def test_case_52(self):
    #     input = """
    #     Var: a, b, arr[10][10], array[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         If main && x Then
    #             Return y + 1;
    #         EndIf.
    #         Return arr[0][0];
    #     EndBody.
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #         array[2][3] = x =/= y;
    #         arr = array;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('arr'),Id('array'))))
    #     self.assertTrue(TestChecker.test(input, expect, 451))
    #
    # def test_case_57(self):
    #     input = """
    #     Var: a, b, arr[10][10], array[10][10];
    #     Function: main
    #     Parameter: x, y, main
    #     Body:
    #         If main && x Then
    #             Return y + 1;
    #         EndIf.
    #         Return arr[0][0];
    #     EndBody.
    #     Function: foo
    #     Parameter: x, y
    #     Body:
    #         array[2][3] = x =/= y;
    #         arr = array;
    #     EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(Id('arr'),Id('array'))))
    #     self.assertTrue(TestChecker.test(input, expect, 456))
    #
    # def test_case_78(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         foo();
    #         test();
    #     EndBody.
    #     Function: test
    #     Body:
    #         If x Then
    #             foo();
    #         Else
    #             test();
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 477))
    #
    # def test_case_100(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo(float_of_int(x))[3] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #         EndIf.
    #         Do
    #         While b[1] <= b[x] EndDo.
    #     EndBody.
    #
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(input, expect, 499))
    #
    # def test_case_80(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If x Then
    #             While x Do
    #                 If x Then
    #                     Break;
    #                 ElseIf False Then
    #                     Continue;
    #                 EndIf.
    #             EndWhile.
    #         Else
    #         EndIf.
    #     EndBody.
    #     """
    #     expect =  str()
    #     self.assertTrue(TestChecker.test(input, expect, 479))
    #
    # def test_case_85(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         While f(2, 3)[4] Do
    #         EndWhile.
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(While(ArrayCell(CallExpr(Id('f'),[IntLiteral(2),IntLiteral(3)]),[IntLiteral(4)]),([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 484))
    #
    # def test_case_86(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         While f(2, x) Do
    #         EndWhile.
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(While(CallExpr(Id('f'),[IntLiteral(2),Id('x')]),([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 485))
    #
    # def test_case_87(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: main
    #     Parameter: x
    #     Body:
    #         While f(2, x) Do
    #         EndWhile.
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     Function: foo
    #     Body:
    #         Return x;
    #     EndBody.
    #     Function: f
    #     Parameter: z, t
    #     Body:
    #         Return a;
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(While(CallExpr(Id('f'),[IntLiteral(2),Id('x')]),([],[]))))
    #     self.assertTrue(TestChecker.test(input, expect, 486))
    #
    #
    # def test_case_32(self):
    #     input = """
    #     Var: a, b[4][2], c;
    #     Function: func
    #     Body:
    #         b[0][1] = 2;
    #         Return b;
    #     EndBody.
    #     Function: test
    #     Body:
    #         func()[2][1] = 14;
    #     EndBody.
    #     Function: main
    #     Body:
    #         func()[3][1] = 0;
    #         b[0][0] = c;
    #         test();
    #         func()[c][2 + 2 * 1] = b[0][c];
    #     EndBody.
    #     """
    #     expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('func'),[]),[Id('c'),BinaryOp('+',IntLiteral(2),BinaryOp('*',IntLiteral(2),IntLiteral(1)))])))
    #     self.assertTrue(TestChecker.test(input, expect, 25))
    #
    # def test_case_24(self):
    #     """
    #     Var: x, y;
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         n = 10 * 2 - 1;
    #         Return n;
    #     EndBody.
    #     Function: main
    #     Body:
    #         Var: x[10][10][10][5];
    #         Var: n;
    #         Var: k = 0x12;
    #         x[n + 2][foo(k) + 2][2 + 15][8 \ 2] = 20;
    #     EndBody.
    #     """
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [VarDecl(Id('n'), [], None)],([],[Assign(Id('n'),BinaryOp('-',BinaryOp('*',IntLiteral(10),IntLiteral(2)),IntLiteral(1))),Return(Id('n'))])),FuncDecl(Id('main'), [],([VarDecl(Id('x'), [10,10,10,5], None),VarDecl(Id('n'), [], None),VarDecl(Id('k'), [],IntLiteral(18))],[Assign(ArrayCell(Id('x'),[BinaryOp('+',Id('n'),IntLiteral(2)),BinaryOp('+',CallExpr(Id('foo'),[Id('k')]),IntLiteral(2)),BinaryOp('+',IntLiteral(2),IntLiteral(15)),BinaryOp('\\',IntLiteral(8),IntLiteral(2))]),IntLiteral(20))]))])
    #     expect = str(IndexOutOfRange(ArrayCell(Id('x'),[BinaryOp('+',Id('n'),IntLiteral(2)),BinaryOp('+',CallExpr(Id('foo'),[Id('k')]),IntLiteral(2)),BinaryOp('+',IntLiteral(2),IntLiteral(15)),BinaryOp('\\',IntLiteral(8),IntLiteral(2))])))
    #     self.assertTrue(TestChecker.test(input, expect, 24))
    #
    # def test_case_38(self):
    #     input = """
    #     Var: a, b[2][12], c[2][12];
    #     Function: foo
    #     Body:
    #         c[0][1] = "s";
    #         Return c;
    #     EndBody.
    #     Function: f
    #     Body:
    #         Var: flag, c;
    #         If c Then
    #             Return 1;
    #         ElseIf c Then
    #             Return b[0][2 + 9];
    #         EndIf.
    #         Return foo()[2+3][1];
    #     EndBody.
    #     Function: main
    #     Body:
    #        a = f();
    #     EndBody.
    #
    #     Function: t
    #     Body:
    #         c[0][11] = "string";
    #     EndBody.
    #     """
    #     expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('foo'),[]),[BinaryOp('+',IntLiteral(2),IntLiteral(3)),IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input, expect, 23))
    #
    # def test_case_39(self):
    #     input = """
    #     Var: a, b[2][4][2];
    #     Function: f
    #     Body:
    #         b[0][0][0] = 22;
    #         Return b;
    #     EndBody.
    #     Function: main
    #     Body:
    #        f()[2][3][3] = 123;
    #        a = test(f()[0][0][1]) \ 9 ;
    #     EndBody.
    #     Function: test
    #     Parameter: k
    #     Body:
    #         Return k * f()[0][2][1];
    #     EndBody.
    #     """
    #     expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('f'),[]),[IntLiteral(2),IntLiteral(3),IntLiteral(3)])))
    #     self.assertTrue(TestChecker.test(input, expect, 22))
    #
    # def test_case_56(self):
    #     input = """
    #     Var: x, a[4][5][2][5][6];
    #     Function: main
    #     Parameter: y
    #     Body:
    #         x = foo(5) * y;
    #         y = a[x][0 + x][0 + 2][y * 3 - x][y];
    #     EndBody.
    #
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         Var: k, arr[10];
    #         If n < foo(x) Then
    #             Return k;
    #         ElseIf k == arr[1] Then
    #             Return k * 2 - arr[foo(k)];
    #         EndIf.
    #         Return arr[5 + 2];
    #     EndBody.
    #     """
    #     expect = str(IndexOutOfRange(ArrayCell(Id('a'),[Id('x'),BinaryOp('+',IntLiteral(0),Id('x')),BinaryOp('+',IntLiteral(0),IntLiteral(2)),BinaryOp('-',BinaryOp('*',Id('y'),IntLiteral(3)),Id('x')),Id('y')])))
    #     self.assertTrue(TestChecker.test(input, expect, 21))
    #
    # def test_case_100(self):
    #     input = """
    #     Var: x, a[10], b[5];
    #     Function: foo
    #     Parameter: k
    #     Body:
    #         a[0] = 1;
    #         Return a;
    #     EndBody.
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If foo(float_of_int(x))[3] == 2 Then
    #         ElseIf b[x] != b[0] Then
    #         EndIf.
    #         foo(0e-2)[9] = b[x + 2]*b[x + foo(1e-2)[2 + foo(2.0202)[0 * foo(1.2)[foo(2.3)[4 \ 2 + 6 % 3 + 2 * 4] * x \ 2]]]] - a[a[a[a[x]]]];
    #     EndBody.
    #
    #     """
    #     expect = str(IndexOutOfRange(ArrayCell(CallExpr(Id('foo'),[FloatLiteral(2.3)]),[BinaryOp('+',BinaryOp('+',BinaryOp('\\',IntLiteral(4),IntLiteral(2)),BinaryOp('%',IntLiteral(6),IntLiteral(3))),BinaryOp('*',IntLiteral(2),IntLiteral(4)))])))
    #     self.assertTrue(TestChecker.test(input, expect, 20))
    #
    # def test_case_33(self):
    #     input = """
    #     Var: a, b[4][12], c;
    #     Function: func
    #     Body:
    #         b[3][0] = 123;
    #         Return b;
    #     EndBody.
    #     Function: test
    #     Body:
    #         func()[2][1] = 14;
    #     EndBody.
    #     Function: main
    #     Body:
    #         func()[3][1] = 0;
    #         b[0][0] = c;
    #         test();
    #         func()[c][2 + 1 * 1] = b[0][c];
    #         If False Then
    #             While True Do
    #             EndWhile.
    #             Break;
    #         EndIf.
    #     EndBody.
    #     """
    #     expect = str("Break Not In Loop")
    #     self.assertTrue(TestChecker.test(input, expect, 19))
    #
    # def test_case_80(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         If x Then
    #             While x Do
    #                 If x Then
    #                     Break;
    #                 ElseIf False Then
    #                     Continue;
    #                 EndIf.
    #             EndWhile.
    #         Else
    #             Break;
    #         EndIf.
    #     EndBody.
    #     """
    #     expect =  str("Break Not In Loop")
    #     self.assertTrue(TestChecker.test(input, expect, 18))
    #
    # def test_case_15(self):
    #     input = """
    #     Var: x, y;
    #     Function: foo
    #     Body:
    #     EndBody.
    #     Function: main
    #     Body:
    #         x = 2 - 3 * y \ 5;
    #         While (y == 0o23) Do
    #             Var: k = "string";
    #             Continue;
    #         EndWhile.
    #     EndBody.
    #     """
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('foo'), [],([],[])),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('\\',BinaryOp('*',IntLiteral(3),Id('y')),IntLiteral(5)))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[Continue()]))]))])
    #     expect = str(UnreachableFunction('foo'))
    #     self.assertTrue(TestChecker.test(input, expect, 17))
    #
    # def test_case_29(self):
    #     input = """
    #     Var: a, b[5], c;
    #     Function: test
    #     Body:
    #         a = 10;
    #         b = {1, 2, 6, 10, 3};
    #         c = b[2];
    #     EndBody.
    #     Function: main
    #     Body:
    #         test();
    #     EndBody.
    #     Function: f
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(UnreachableFunction('f'))
    #     self.assertTrue(TestChecker.test(input, expect, 16))
    #
    # def test_case_51(self):
    #     input = """
    #     Var: x[10], y, m;
    #     Function: main
    #     Body:
    #         x[0] = y + 10;
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: a, b, c;
    #         If x[2] == a Then
    #             printStrLn(b);
    #         EndIf.
    #         For(a = 0, c < m, m \ 10) Do
    #             printStr(string_of_int(a * c - m));
    #         EndFor.
    #     EndBody.
    #     """
    #     expect = str(UnreachableFunction('test'))
    #     self.assertTrue(TestChecker.test(input, expect, 15))
    #
    # def test_case_78(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #
    #     EndBody.
    #     Function: test
    #     Body:
    #         If x Then
    #             foo();
    #         Else
    #             test();
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(UnreachableFunction('test'))
    #     self.assertTrue(TestChecker.test(input, expect, 14))
    #
    # def test_case_79(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #
    #     EndBody.
    #     Function: test
    #     Body:
    #         If x Then
    #             foo();
    #         Else
    #             test();
    #         EndIf.
    #     EndBody.
    #     Function: foo
    #     Body:
    #     EndBody.
    #     """
    #     expect = str(UnreachableFunction('test'))
    #     self.assertTrue(TestChecker.test(input, expect, 13))
    #
    # def test_case_16(self):
    #     """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         x = 2 - 3 * y;
    #         While (y == 0o23) Do
    #             Var: k = "string";
    #             If x == y Then
    #                 If x == 3 Then
    #                 ElseIf y == 4 Then
    #                     Break;
    #                     x = y;
    #                 EndIf.
    #             EndIf.
    #         EndWhile.
    #     EndBody.
    #     """
    #     input = Program([VarDecl(Id('x'), [], None),VarDecl(Id('y'), [], None),FuncDecl(Id('main'), [],([],[Assign(Id('x'),BinaryOp('-',IntLiteral(2),BinaryOp('*',IntLiteral(3),Id('y')))),While(BinaryOp('==',Id('y'),IntLiteral(19)),([VarDecl(Id('k'), [],StringLiteral("""string"""))],[If([(BinaryOp('==',Id('x'),Id('y')),[],[If([(BinaryOp('==',Id('x'),IntLiteral(3)),[],[]),(BinaryOp('==',Id('y'),IntLiteral(4)),[],[Break(),Assign(Id('x'),Id('y'))])], ([],[]))])], ([],[]))]))]))])
    #     expect = str(UnreachableStatement(Assign(Id('x'),Id('y'))))
    #     self.assertTrue(TestChecker.test(input, expect, 12))
    #
    # def test_case_42(self):
    #     input = """
    #     Var: a, b[2][4][2];
    #     Function: main
    #     Body:
    #         Var: temp;
    #        printStrLn(a);
    #        Do
    #             If bool_of_string(a) Then
    #                 Break;
    #                 test(a);
    #             EndIf.
    #         While b[0][1][1] EndDo.
    #     EndBody.
    #     Function: test
    #     Parameter: p
    #     Body:
    #         printStr(read());
    #         Return;
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id('test'),[Id('a')])))
    #     self.assertTrue(TestChecker.test(input, expect, 11))
    #
    # def test_case_43(self):
    #     input = """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         If x Then
    #             If x Then
    #                 Return 0;
    #             EndIf.
    #             If x Then
    #                 Return y;
    #             ElseIf x Then
    #                 If x Then
    #                     Return 1;
    #                 Else
    #                     Return 0;
    #                 EndIf.
    #                 y = 10;
    #             EndIf.
    #         Else
    #             Return 1;
    #         EndIf.
    #         y = 1;
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Assign(Id('y'),IntLiteral(10))))
    #     self.assertTrue(TestChecker.test(input, expect, 9))
    #
    # def test_case_45(self):
    #     input = """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         Var: k, t, z;
    #         While x Do
    #             If x Then
    #                 y = 2;
    #                 Break;
    #             ElseIf k == t Then
    #                 z = 20;
    #                 Continue;
    #             Else
    #                 Break;
    #             EndIf.
    #             t = y + z;
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Assign(Id('t'),BinaryOp('+',Id('y'),Id('z')))))
    #     self.assertTrue(TestChecker.test(input, expect, 8))
    #
    # def test_case_48(self):
    #     input = """
    #     Var: x[10], y, m;
    #     Function: main
    #     Body:
    #         x[0] = test() +. y;
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: a, b, c;
    #         For (a = int_of_float(test()), b && c, m) Do
    #             Var: z, y, x;
    #             If z == y Then
    #                 Break;
    #             ElseIf x Then
    #                 Continue;
    #             ElseIf c Then
    #                 Return float_to_int(a);
    #             Else
    #                 Return 1.2;
    #             EndIf.
    #             b = True;
    #         EndFor.
    #         Return float_to_int(m);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Assign(Id('b'),BooleanLiteral(True))))
    #     self.assertTrue(TestChecker.test(input, expect, 7))
    #
    # def test_case_50(self):
    #     input = """
    #     Var: x[10], y, m;
    #     Function: main
    #     Body:
    #         x[0] = test() + y;
    #     EndBody.
    #     Function: test
    #     Body:
    #         Var: a, b, c;
    #         Do
    #             If c Then
    #                 If c Then
    #                 ElseIf False Then
    #                     If a > b Then
    #                         Break;
    #                     Else
    #                         Return 0;
    #                     EndIf.
    #                     a = b;
    #                 EndIf.
    #             EndIf.
    #         While a == b EndDo.
    #         Return a * b;
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Assign(Id('a'),Id('b'))))
    #     self.assertTrue(TestChecker.test(input, expect,6))
    #
    # def test_case_55(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: y
    #     Body:
    #         x = foo(5) * y;
    #     EndBody.
    #
    #     Function: foo
    #     Parameter: n
    #     Body:
    #         Var: k, arr[10];
    #         If n < foo(x) Then
    #             Return k * 2 - arr[foo(k)];
    #         ElseIf k == arr[1] Then
    #             Return k;
    #         Else
    #             Return x;
    #         EndIf.
    #         Return arr[5];
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(Return(ArrayCell(Id('arr'),[IntLiteral(5)]))))
    #     self.assertTrue(TestChecker.test(input, expect, 5))
    #
    # def test_case_66(self):
    #     input = """
    #     Var: x[10];
    #     Function: main
    #     Body:
    #         Var: y, z;
    #         x[2] = x[0o3] || (y > z);
    #         While x[2] && x[3] Do
    #             Do
    #                 printStrLn(string_of_int(y * z));
    #                 If x[0] Then
    #                     Return 1;
    #                 ElseIf x[1] Then
    #                     Return z;
    #                 Else
    #                     Var: k;
    #                     k = 10;
    #                 EndIf.
    #                 z = y;
    #             While x[4] EndDo.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = str(FunctionNotReturn('main'))
    #     self.assertTrue(TestChecker.test(input, expect, 4))
    #
    # def test_case_81(self):
    #     input = """
    #     Var: x;
    #     Function: main
    #     Parameter: x
    #     Body:
    #         x = x + test(x, 1);
    #     EndBody.
    #     Function: test
    #     Parameter: x, y
    #     Body:
    #     EndBody.
    #     """
    #     expect =  str(FunctionNotReturn('test'))
    #     self.assertTrue(TestChecker.test(input, expect, 3))
    #
    # def test_case_27(self):
    #     input = """
    #     Var: x, y = "s", t, arr[10];
    #     Function: main
    #     Body:
    #
    #     EndBody.
    #     Function: foo
    #     Parameter: x
    #     Body:
    #         Var: arr[2];
    #         If x Then
    #             Return int_of_string(string_of_bool(x));
    #         ElseIf f(x) Then
    #             Return foo(bool_of_string(arr[0]));
    #         EndIf.
    #     EndBody.
    #     Function: f
    #     Parameter: x
    #     Body:
    #         If bool_of_string(string_of_bool(x)) Then
    #             Return x;
    #         EndIf.
    #         Return True;
    #     EndBody.
    #     """
    #     expect = str(FunctionNotReturn('foo'))
    #     self.assertTrue(TestChecker.test(input, expect, 2))
    #
    # def test_case_44(self):
    #     input = """
    #     Var: x, y;
    #     Function: main
    #     Body:
    #         If x Then
    #             If x Then
    #                 Return 0;
    #             EndIf.
    #             If x Then
    #                 Return y;
    #             ElseIf x Then
    #                 If x Then
    #                     Return y;
    #                 Else
    #                     Return 0;
    #                 EndIf.
    #             EndIf.
    #         Else
    #             Return 1;
    #         EndIf.
    #         y = y * 2;
    #     EndBody.
    #     """
    #     expect = str(FunctionNotReturn('main'))
    #     self.assertTrue(TestChecker.test(input, expect, 1))
    #
    # def test_checker_032(self):
    #     input = """
    # 	Function: main
    # 	Body:
    # 		Var: arr[5] = {1,2,3,4,5},x;
    # 		** test index operator **
    # 		x = arr[-10];
    # 	EndBody.
    # 	"""
    #     expect = str(IndexOutOfRange(ArrayCell(Id("arr"), [UnaryOp('-', IntLiteral(10))])))
    #     self.assertTrue(TestChecker.test(input, expect, 32))
    #
    # def test_checker_033(self):
    #     input = """
    # 	Function: main
    # 	Body:
    # 		Var: arr[5] = {1,2,3,4,5},x;
    # 		** test index operator **
    # 		x = arr[-----10];
    # 	EndBody.
    # 	"""
    #     expect = str(IndexOutOfRange(ArrayCell(Id("arr"), [
    #         UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', IntLiteral(10))))))])))
    #     self.assertTrue(TestChecker.test(input, expect, 33))
    #
    # def test_checker_034(self):
    #     input = """
    # 	Function: main
    # 	Body:
    # 		**do something with array**
    # 		Var: a[2][3] = {{1,2,3},{4,5,6}};
    # 		Var: key = 2;
    # 		a[1][1] = 1;
    #
    # 		If (a[2][4] < key)
    # 			Then printStrLn("2-4");
    # 		ElseIf (a[1-1][0] < key) Then
    # 			printStrLn("0-0");
    # 		ElseIf (a[1][key*2 - 1] < key) Then
    # 			printStrLn("1-2");
    # 		Else
    # 			printStrLn("NOT FOUND");
    # 		EndIf.
    #
    # 	EndBody.
    # 	"""
    #     expect = str(IndexOutOfRange(ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 34))
    #
    #
    #



