import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_case_1(self):
        input = r""" """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_case_2(self):
        input = """
                Function: main
        Body:
            print(string_of_int(foo({100, 42, 4, 2, 63, 42, 53, 22, 731, 431})));
        EndBody.
                """
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None),
            FuncDecl(Id("fxxoo"), [], ([], [])),
            FuncDecl(Id("main"), [], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 2))

    """ Variable declaration """

    def test_case_3(self):
        input = r"""
    Var: b;
    """
        expect = Program([VarDecl(Id("b"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_case_4(self):
        input = r"""
    Var: a11;
    Var: b0, b2;
    Var: c1, c2, c4;
    """
        expect = Program([
            VarDecl(Id("a11"), [], None),
            VarDecl(Id("b0"), [], None),
            VarDecl(Id("b2"), [], None),
            VarDecl(Id("c1"), [], None),
            VarDecl(Id("c2"), [], None),
            VarDecl(Id("c4"), [], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_case_5(self):
        input = r"""
    Var: a12[0];
    Var: a1[1], a2[1][2], a3[1][2][3], a33[1][2][3][4];
    """
        expect = Program([
            VarDecl(Id("a12"), [0], None),
            VarDecl(Id("a1"), [1], None),
            VarDecl(Id("a2"), [1, 2], None),
            VarDecl(Id("a3"), [1, 2, 3], None),
            VarDecl(Id("a33"), [1, 2, 3, 4], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_case_6(self):
        input = r"""
    Var: a1[0o1][0o2][0o3][0o4][0o5][0o6][0o7];
    Var: a1[0O1][0O2][0O3][0O4][0O5][0O6][0O7];
    Var: a1[0o1000000000], a1[0O76543210];
    """
        expect = Program([
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [134217728], None),
            VarDecl(Id("a1"), [16434824], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_case_7(self):
        input = r"""
    Var: x[0x1][0x2][0x3][0x4][0x5][0x6][0x7][0x8][0x9];
    Var: b[0xA][0xB][0xC][0xD][0xE][0xF];
    Var: c[0X1][0X2][0X3][0X4][0X5][0X6][0X7][0X8][0X9];
    Var: f[0XA][0XB][0XC][0XD][0XE][0XF];
    Var: c[0x10000000], d[0XABCDEF];
    Var: r[0x1234], e[0X8765];
    """
        expect = Program([
            VarDecl(Id("x"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("b"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("f"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [268435456], None),
            VarDecl(Id("d"), [11259375], None),
            VarDecl(Id("r"), [4660], None),
            VarDecl(Id("e"), [34661], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_case_8(self):
        input = r"""
    Var: a = 1;
    Var: a[1] = {1};
    Var: a[1][2] = {{1}, {2}};
    """
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(1)),
            VarDecl(Id("a"), [1], ArrayLiteral([IntLiteral(1)])),
            VarDecl(Id("a"), [1, 2],
                    ArrayLiteral([ArrayLiteral([IntLiteral(1)]),
                                  ArrayLiteral([IntLiteral(2)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    """ Function declaration """

    def test_case_9(self):
        input = r"""
    Function: main
        Body:
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_case_10(self):
        input = """
        Function: m
        Body:
            Do
                arr[31 + food(2.0)] = a[f[2][32]] + 5;
             i == False EWhilendDo.

        EndBody.
        """
        f = Dowhile(([], [
            Assign(ArrayCell(Id('arr'), [BinaryOp('+', IntLiteral(31), CallExpr(Id('food'), [FloatLiteral(2.0)]))]),
                   BinaryOp('+', ArrayCell(Id('a'), [ArrayCell(Id('f'), [IntLiteral(2), IntLiteral(32)])]),
                            IntLiteral(5)))]), BinaryOp('==', Id('i'), BooleanLiteral(False)))
        fn = FuncDecl(Id('m'), [], ([], [f]))
        expect = Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_case_11(self):
        input = """
        Function: main
        Parameter: a[10], b
        Body:
            Var: i = 0;
            While x > 0 Do
                If i == 0 Then
                    Var: k = 0.;
                    main(i);
                EndIf.
            EndWhile.

        EndBody.
        """
        f = While(BinaryOp('>', Id('x'), IntLiteral(0)), ([], [If([(BinaryOp('==', Id('i'), IntLiteral(0)),
                                                                    [VarDecl(Id('k'), [], FloatLiteral(0.))],
                                                                    [CallStmt(Id('main'), [Id('i')])])], ([], []))]))
        fn = FuncDecl(Id('main'), [VarDecl(Id('a'), [10], None), VarDecl(Id('b'), [], None)],
                      ([VarDecl(Id('i'), [], IntLiteral(0))], [f]))
        expect = Program([fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_case_12(self):
        input = """
        Var: a = 5, n[10], s = False;
        Var: bb[2][3] = {{2, 3, 4}, {4, 5, 6}};
        Function: main
        Body:
            flag = 2;
            a = !!!!True || dkd;
            Return fool() + uuuuu(2 + 3, f[2][4]) && dk;

        EndBody.
        """
        stmts = [Assign(Id('flag'), IntLiteral(2)), Assign(Id('a'), BinaryOp('||', UnaryOp('!', UnaryOp('!',
                                                                                                        UnaryOp('!',
                                                                                                                UnaryOp(
                                                                                                                    '!',
                                                                                                                    BooleanLiteral(
                                                                                                                        True))))),
                                                                             Id('dkd'))), \
                 Return(BinaryOp('&&', BinaryOp('+', CallExpr(Id('fool'), []), CallExpr(Id('uuuuu'), [
                     BinaryOp('+', IntLiteral(2), IntLiteral(3)), ArrayCell(Id('f'), [IntLiteral(2), IntLiteral(4)])])),
                                 Id('dk')))]
        fn = FuncDecl(Id('main'), [], ([], stmts))
        expect = Program([VarDecl(Id('a'), [], IntLiteral(5)), VarDecl(Id('n'), [10], None),
                          VarDecl(Id('s'), [], BooleanLiteral(False)), \
                          VarDecl(Id('bb'), [2, 3], ArrayLiteral(
                              [ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
                               ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])),
                          fn])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_case_13(self):
        input = """
        Var: s = "daofjsdg";
        Function: main
        Body:
            Var: arr[26];
            f = fact(n) % 0O10;
            While (i < length(s)) Do
                arr[lower(s[i]) - 97] =  arr[lower(s[i]) - 97] +. 1.e0;
            EndWhile.
            max_length = max(arr);
        EndBody.
        Function: sum
        Parameter: n
        Body:
            p = 1.;
            For (i = 1, i < n, 1) Do
                p = p *. i;
            EndFor.
            Return i;
        EndBody.
        """
        f1 = FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [26], None)], [
            Assign(Id('f'), BinaryOp('%', CallExpr(Id('fact'), [Id('n')]), IntLiteral(0o10))), \
            While(BinaryOp('<', Id('i'), CallExpr(Id('length'), [Id('s')])), ([], [Assign(ArrayCell(Id('arr'), [
                BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), BinaryOp('+.',
                                                                                                                  ArrayCell(
                                                                                                                      Id(
                                                                                                                          'arr'),
                                                                                                                      [
                                                                                                                          BinaryOp(
                                                                                                                              '-',
                                                                                                                              CallExpr(
                                                                                                                                  Id(
                                                                                                                                      'lower'),
                                                                                                                                  [
                                                                                                                                      ArrayCell(
                                                                                                                                          Id(
                                                                                                                                              's'),
                                                                                                                                          [
                                                                                                                                              Id(
                                                                                                                                                  'i')])]),
                                                                                                                              IntLiteral(
                                                                                                                                  97))]),
                                                                                                                  FloatLiteral(
                                                                                                                      1.0)))])), \
            Assign(Id('max_length'), CallExpr(Id('max'), [Id('arr')]))]))
        f2 = FuncDecl(Id('sum'), [VarDecl(Id('n'), [], None)], ([], [Assign(Id('p'), FloatLiteral(1.)),
                                                                     For(Id('i'), IntLiteral(1),
                                                                         BinaryOp('<', Id('i'), Id('n')), IntLiteral(1),
                                                                         ([], [Assign(Id('p'), BinaryOp('*.', Id('p'),
                                                                                                        Id('i')))])),
                                                                     Return(Id('i'))]))
        expect = Program([VarDecl(Id('s'), [], StringLiteral("daofjsdg")), f1, f2])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_case_14(self):
        input = """
        Var: s = "daofjsdg";
        Function: main
        Body:
            Var: arr[26];
            f = fact(n) % 0O10;
            While (i < length(s)) Do
                arr[lower(s[i]) - 97] =  arr[lower(s[i]) - 97] +. 1.e0;
            EndWhile.
            max_length = max(arr);
        EndBody.
        Function: sum
        Parameter: n
        Body:
            p = 1.;
            For (i = 1, i < n, 1) Do
                p = p *. i;
            EndFor.
            Return i;
        EndBody.
        """
        f1 = FuncDecl(Id('main'), [], ([VarDecl(Id('arr'), [26], None)], [
            Assign(Id('f'), BinaryOp('%', CallExpr(Id('fact'), [Id('n')]), IntLiteral(0o10))), \
            While(BinaryOp('<', Id('i'), CallExpr(Id('length'), [Id('s')])), ([], [Assign(ArrayCell(Id('arr'), [
                BinaryOp('-', CallExpr(Id('lower'), [ArrayCell(Id('s'), [Id('i')])]), IntLiteral(97))]), BinaryOp('+.',
                                                                                                                  ArrayCell(
                                                                                                                      Id(
                                                                                                                          'arr'),
                                                                                                                      [
                                                                                                                          BinaryOp(
                                                                                                                              '-',
                                                                                                                              CallExpr(
                                                                                                                                  Id(
                                                                                                                                      'lower'),
                                                                                                                                  [
                                                                                                                                      ArrayCell(
                                                                                                                                          Id(
                                                                                                                                              's'),
                                                                                                                                          [
                                                                                                                                              Id(
                                                                                                                                                  'i')])]),
                                                                                                                              IntLiteral(
                                                                                                                                  97))]),
                                                                                                                  FloatLiteral(
                                                                                                                      1.0)))])), \
            Assign(Id('max_length'), CallExpr(Id('max'), [Id('arr')]))]))
        f2 = FuncDecl(Id('sum'), [VarDecl(Id('n'), [], None)], ([], [Assign(Id('p'), FloatLiteral(1.)),
                                                                     For(Id('i'), IntLiteral(1),
                                                                         BinaryOp('<', Id('i'), Id('n')), IntLiteral(1),
                                                                         ([], [Assign(Id('p'), BinaryOp('*.', Id('p'),
                                                                                                        Id('i')))])),
                                                                     Return(Id('i'))]))
        expect = Program([VarDecl(Id('s'), [], StringLiteral("daofjsdg")), f1, f2])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_case_15(self):
        input = """
        Function: main
        Body:
            Var: x = 0x213ACF, s = 123e-3;
            v = 4 \. (3 *. 314e-2) * r * r * r;
            If x < 10 Then
                Break;
            Else
                x = x && d >. 1;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], (
        [VarDecl(Id('x'), [], IntLiteral(0x213ACF)), VarDecl(Id('s'), [], FloatLiteral(123e-3))], \
        [Assign(Id('v'), BinaryOp('*', BinaryOp('*', BinaryOp('*', BinaryOp('\\.', IntLiteral(4),
                                                                            BinaryOp('*.', IntLiteral(3),
                                                                                     FloatLiteral(314e-2))), Id('r')),
                                                Id('r')), Id('r'))), \
         If([(BinaryOp('<', Id('x'), IntLiteral(10)), [], [Break()])],
            ([], [Assign(Id('x'), BinaryOp('>.', BinaryOp('&&', Id('x'), Id('d')), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_case_16(self):
        input = """
        Function: mainMax
        Body:
            Do
                Var: r = 12;
                k = -.-k;
                a[2][3 + 3] = foo(2 + k, k, arr[0]);
                m = a[1][2 + f[2]];
            While x == 0 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('mainMax'), [], (
        [], [Dowhile(([VarDecl(Id('r'), [], IntLiteral(12))], [Assign(Id('k'), UnaryOp('-.', UnaryOp('-', Id('k')))), \
                                                               Assign(ArrayCell(Id('a'), [IntLiteral(2),
                                                                                          BinaryOp('+', IntLiteral(3),
                                                                                                   IntLiteral(3))]), \
                                                                      CallExpr(Id('foo'),
                                                                               [BinaryOp('+', IntLiteral(2), Id('k')),
                                                                                Id('k'), ArrayCell(Id('arr'),
                                                                                                   [IntLiteral(0)])])), \
                                                               Assign(Id('m'), ArrayCell(Id('a'), [IntLiteral(1),
                                                                                                   BinaryOp('+',
                                                                                                            IntLiteral(
                                                                                                                2),
                                                                                                            ArrayCell(
                                                                                                                Id('f'),
                                                                                                                [
                                                                                                                    IntLiteral(
                                                                                                                        2)]))]))]),
                     BinaryOp('==', Id('x'), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_case_17(self):
        input = """
        Var: m, n[10]; 
        Function: main 
        Parameter: n 
        Body: 
            x = {{{1,2}, {3,4}}, {5,6}};
            If n == 0 Then 
                Return 1; 
            Else
                Return n * face({1,2});
            EndIf.
        EndBody. 
        """
        expect = Program([VarDecl(Id('m'), [], None), VarDecl(Id('n'), [10], None),
                          FuncDecl(Id('main'), [VarDecl(Id('n'), [], None)], ([], [ \
                              Assign(Id('x'), ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                                                                          ArrayLiteral(
                                                                              [IntLiteral(3), IntLiteral(4)])]),
                                                            ArrayLiteral([IntLiteral(5), IntLiteral(6)])])), \
                              If([(BinaryOp('==', Id('n'), IntLiteral(0)), [], [Return(IntLiteral(1))])], ([], [Return(
                                  BinaryOp('*', Id('n'), CallExpr(Id('face'), [
                                      ArrayLiteral([IntLiteral(1), IntLiteral(2)])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_case_18(self):
        input = """
        Var: a, b, c = 10e12;
        Function: main
        Body:
            Var: i = 0, arr[10];
            c = arr[0];
            For (i = 1, i < 10, 1) Do
                If (c < arr[i]) Then
                    c = arr[i];
                EndIf.
            EndFor.  
            f(1, 2, 3);
            Return;
        EndBody.
        """
        expect = Program(
            [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None), VarDecl(Id('c'), [], FloatLiteral(10e12)),
             FuncDecl(Id('main'), [], ([VarDecl(Id('i'), [], IntLiteral(0)), VarDecl(Id('arr'), [10], None)], [ \
                 Assign(Id('c'), ArrayCell(Id('arr'), [IntLiteral(0)])), \
                 For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), IntLiteral(10)), IntLiteral(1), ([], [If([(BinaryOp(
                     '<', Id('c'), ArrayCell(Id('arr'), [Id('i')])), [], [Assign(Id('c'),
                                                                                 ArrayCell(Id('arr'), [Id('i')]))])], (
                                                                                                             [],
                                                                                                             []))])), \
                 CallStmt(Id('f'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_case_19(self):
        input = """
        Function: sortArr
        Parameter: arr[0o100], left, right
        Body:
            For(i = left + 1, i <= right, 1) Do
                Var: temp, j;
                temp = arr[i];
                j = i - 1;
                While (j >= left) && (arr[j] > temp) Do
                    arr[j + 1] = arr[j];
                    j = j - 1;
                EndWhile.
                arr[j + 1] = temple;
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('sortArr'), [VarDecl(Id('arr'), [0o100], None), VarDecl(Id('left'), [], None),
                                                   VarDecl(Id('right'), [], None)], ([], [ \
            For(Id('i'), BinaryOp('+', Id('left'), IntLiteral(1)), BinaryOp('<=', Id('i'), Id('right')), IntLiteral(1),
                ([VarDecl(Id('temp'), [], None), VarDecl(Id('j'), [], None)], \
                 [Assign(Id('temp'), ArrayCell(Id('arr'), [Id('i')])),
                  Assign(Id('j'), BinaryOp('-', Id('i'), IntLiteral(1))), \
                  While(BinaryOp('&&', BinaryOp('>=', Id('j'), Id('left')),
                                 BinaryOp('>', ArrayCell(Id('arr'), [Id('j')]), Id('temp'))), ([], [
                      Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]),
                             ArrayCell(Id('arr'), [Id('j')])),
                      Assign(Id('j'), BinaryOp('-', Id('j'), IntLiteral(1)))])), \
                  Assign(ArrayCell(Id('arr'), [BinaryOp('+', Id('j'), IntLiteral(1))]), Id('temple'))
                  ]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_case_20(self):
        input = r"""
    Function: main
        Body:
            Var: a;
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_case_21(self):
        input = r"""
    Function: main
        Body:
            foo();
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_case_22(self):
        input = r"""
    Function: main
        Body:
            Var: a, b;
            foo1();
            foo2d();
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([
                                          VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)
                                      ], [CallStmt(Id("foo1"), []), CallStmt(Id("foo2d"), [])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_case_23(self):
        input = r"""
    Function: main
        Parameter: a
        Body:
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_case_24(self):
        input = r"""
    Function: main
        Parameter: a, b, c
        Body:
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("b"), [], None),
                VarDecl(Id("c"), [], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_case_25(self):
        input = r"""
    Function: main
        Parameter: a[1], b[123], c[0xABCDEF][0X123], d[0o7654][0O3210]
        Body:
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [1], None),
                VarDecl(Id("b"), [123], None),
                VarDecl(Id("c"), [11259375, 291], None),
                VarDecl(Id("d"), [4012, 1672], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

        """ If statement """

    def test_case_26(self):
        input = r"""
    Function: main
        Body:
            If True Then
            EndIf.
        EndBody.
    """
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_case_27(self):
        input = r"""
    Function: main
        Body:
            If a Then
                Var: a;
            EndIf.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [VarDecl(Id("a"), [], None)], [])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_case_28(self):
        input = r"""
    Function: main
        Body:
            If a Then
                foo();
            EndIf.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [], [CallStmt(Id("foo"), [])])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_case_29(self):
        input = r"""
    Function: main
        Body:
            If a Then
                Var: a, b;
                foo1();
                foo2();
            EndIf.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(Id("a"), [VarDecl(Id("a"), [], None),
                               VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_case_30(self):
        input = """
        Function: main
        Body:
            inp = 123 * daf[g132[423][2] * 132 + {13}];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [Assign(Id('inp'), BinaryOp('*', IntLiteral(123),
                                                                                    ArrayCell(Id('daf'), [BinaryOp('+',
                                                                                                                   BinaryOp(
                                                                                                                       '*',
                                                                                                                       ArrayCell(
                                                                                                                           Id(
                                                                                                                               'g132'),
                                                                                                                           [
                                                                                                                               IntLiteral(
                                                                                                                                   423),
                                                                                                                               IntLiteral(
                                                                                                                                   2)]),
                                                                                                                       IntLiteral(
                                                                                                                           132)),
                                                                                                                   ArrayLiteral(
                                                                                                                       [
                                                                                                                           IntLiteral(
                                                                                                                               13)]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_case_31(self):
        input = """
        Function: main
        Body:
            If "" Then
            in = 1223 - 4234 +. 432 || !False;
            inp = {123, 435, 423} * in;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [If([(StringLiteral(''), [], [Assign(Id('in'), BinaryOp('||',
                                                                                                                BinaryOp(
                                                                                                                    '+.',
                                                                                                                    BinaryOp(
                                                                                                                        '-',
                                                                                                                        IntLiteral(
                                                                                                                            1223),
                                                                                                                        IntLiteral(
                                                                                                                            4234)),
                                                                                                                    IntLiteral(
                                                                                                                        432)),
                                                                                                                UnaryOp(
                                                                                                                    '!',
                                                                                                                    BooleanLiteral(
                                                                                                                        False)))),
                                                                                      Assign(Id('inp'), BinaryOp('*',
                                                                                                                 ArrayLiteral(
                                                                                                                     [
                                                                                                                         IntLiteral(
                                                                                                                             123),
                                                                                                                         IntLiteral(
                                                                                                                             435),
                                                                                                                         IntLiteral(
                                                                                                                             423)]),
                                                                                                                 Id(
                                                                                                                     'in')))])],
                                                            ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_case_32(self):
        input = """
        Var: x, y =1, y = "abc'" hello \\t ", m[13425], n[1053245] = {1,2,{"a534n",5.54324},5.e-145232};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+2120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4123542 + 7 > 4;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], IntLiteral(1)),
                          VarDecl(Id('y'), [], StringLiteral("""abc'" hello \\t """)), VarDecl(Id('m'), [13425], None),
                          VarDecl(Id('n'), [1053245], ArrayLiteral([IntLiteral(1), IntLiteral(2), ArrayLiteral(
                              [StringLiteral("""a534n"""), FloatLiteral(5.54324)]), FloatLiteral(0.0)])),
                          VarDecl(Id('a_jacj933'), [], FloatLiteral(12.21)), FuncDecl(Id('fact'),
                                                                                      [VarDecl(Id('n'), [], None),
                                                                                       VarDecl(Id('aca_312aAX'),
                                                                                               [3, 44, 12799], None),
                                                                                       VarDecl(Id('cxa'), [18, 1, 8, 0],
                                                                                               None)], (
                                                                                      [VarDecl(Id('t'), [], None),
                                                                                       VarDecl(Id('r'), [],
                                                                                               FloatLiteral(10.0)),
                                                                                       VarDecl(Id('thread'), [],
                                                                                               FloatLiteral('inf')),
                                                                                       VarDecl(Id('r'), [],
                                                                                               FloatLiteral(10.0))], [
                                                                                          Assign(Id('v'), BinaryOp('*',
                                                                                                                   BinaryOp(
                                                                                                                       '*',
                                                                                                                       BinaryOp(
                                                                                                                           '*.',
                                                                                                                           BinaryOp(
                                                                                                                               '*.',
                                                                                                                               BinaryOp(
                                                                                                                                   '\.',
                                                                                                                                   FloatLiteral(
                                                                                                                                       4.0),
                                                                                                                                   FloatLiteral(
                                                                                                                                       3.0)),
                                                                                                                               FloatLiteral(
                                                                                                                                   3.14)),
                                                                                                                           Id(
                                                                                                                               'r')),
                                                                                                                       Id(
                                                                                                                           'r')),
                                                                                                                   Id(
                                                                                                                       'a'))),
                                                                                          Assign(Id('object'),
                                                                                                 BinaryOp('>',
                                                                                                          BinaryOp('+',
                                                                                                                   IntLiteral(
                                                                                                                       4123542),
                                                                                                                   IntLiteral(
                                                                                                                       7)),
                                                                                                          IntLiteral(
                                                                                                              4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_case_33(self):
        input = """
        Function: main
        Body:
            If "" Then
                If 1 Then
                    inp = f23 + ads[2+10] --- 2 *f ** "87235jkfgshgsfg $&^# ** ;
                ElseIf 1 Then 
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [], ([], [If([(StringLiteral(""""""), [], [If([(IntLiteral(1), [], [
            Assign(Id('inp'), BinaryOp('-', BinaryOp('+', Id('f23'), ArrayCell(Id('ads'), [
                BinaryOp('+', IntLiteral(2), IntLiteral(10))])),
                                       BinaryOp('*', UnaryOp('-', UnaryOp('-', IntLiteral(2))), Id('f'))))]),
                                                                                              (IntLiteral(1), [], [])],
                                                                                             ([], []))])],
                                                            ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_case_34(self):
        input = """
		Var: x = 1,y= "abc",z[1];
		Var: temp = 0;
		Function: main
		Parameter: x,y,arr[10][12]
		Body:
			Var: x = 1;
			x = True && 1;
			Break;
			foo(1);
			Return x + 1;
		EndBody.
		"""
        expect = Program([VarDecl(Id('x'), [], IntLiteral(1)), VarDecl(Id('y'), [], StringLiteral("""abc""")),
                          VarDecl(Id('z'), [1], None), VarDecl(Id('temp'), [], IntLiteral(0)), FuncDecl(Id('main'), [
                VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None), VarDecl(Id('arr'), [10, 12], None)], ([VarDecl(
                Id('x'), [], IntLiteral(1))], [Assign(Id('x'), BinaryOp('&&', BooleanLiteral(True), IntLiteral(1))),
                                               Break(), CallStmt(Id('foo'), [IntLiteral(1)]),
                                               Return(BinaryOp('+', Id('x'), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_case_35(self):
        input = """
        Var: max_length = 100;
        Function: countintSort
        Parameter: arr[100]
        Body:
            Var: output[100];
            Var: count[100], i;
            memset(count, 0, sizeof(count));
            For(i = 0, arr[i] > 0, 1) Do
                count[arr[i]] = count[arr[i]] + 1;
            EndFor.
            For(i = 1, i <= range(arr), 1) Do
                count[i] = count[i] + count[i - 1];
            EndFor.
            For(i = 0, arr[i] > 0, 1) Do
                output[count[arr[i]] - 1] = arr[i];
                count[arr[i]] = count[arr[i]] - 1;
            EndFor.
            For( i = 0, arr[i] != 0, 1) Do
                If i % 2 == 0 Then
                    arr[i] = i \\ 2;
                ElseIf i % 3 == 0 Then
                    arr[i] = 3 *. i;
                ElseIf i % 5 == 1 Then
                    arr[i] = i;
                Else
                    arr[i] = output[i];
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('max_length'), [], IntLiteral(100)),
                          FuncDecl(Id('countintSort'), [VarDecl(Id('arr'), [100], None)], (
                          [VarDecl(Id('output'), [100], None), VarDecl(Id('count'), [100], None),
                           VarDecl(Id('i'), [], None)],
                          [CallStmt(Id('memset'), [Id('count'), IntLiteral(0), CallExpr(Id('sizeof'), [Id('count')])]),
                           For(Id('i'), IntLiteral(0), BinaryOp('>', ArrayCell(Id('arr'), [Id('i')]), IntLiteral(0)),
                               IntLiteral(1), ([], [Assign(ArrayCell(Id('count'), [ArrayCell(Id('arr'), [Id('i')])]),
                                                           BinaryOp('+', ArrayCell(Id('count'),
                                                                                   [ArrayCell(Id('arr'), [Id('i')])]),
                                                                    IntLiteral(1)))])),
                           For(Id('i'), IntLiteral(1), BinaryOp('<=', Id('i'), CallExpr(Id('range'), [Id('arr')])),
                               IntLiteral(1), ([], [Assign(ArrayCell(Id('count'), [Id('i')]),
                                                           BinaryOp('+', ArrayCell(Id('count'), [Id('i')]),
                                                                    ArrayCell(Id('count'), [
                                                                        BinaryOp('-', Id('i'), IntLiteral(1))])))])),
                           For(Id('i'), IntLiteral(0), BinaryOp('>', ArrayCell(Id('arr'), [Id('i')]), IntLiteral(0)),
                               IntLiteral(1), ([], [Assign(ArrayCell(Id('output'), [
                                   BinaryOp('-', ArrayCell(Id('count'), [ArrayCell(Id('arr'), [Id('i')])]),
                                            IntLiteral(1))]), ArrayCell(Id('arr'), [Id('i')])),
                                                    Assign(ArrayCell(Id('count'), [ArrayCell(Id('arr'), [Id('i')])]),
                                                           BinaryOp('-', ArrayCell(Id('count'),
                                                                                   [ArrayCell(Id('arr'), [Id('i')])]),
                                                                    IntLiteral(1)))])),
                           For(Id('i'), IntLiteral(0), BinaryOp('!=', ArrayCell(Id('arr'), [Id('i')]), IntLiteral(0)),
                               IntLiteral(1), ([], [If([(BinaryOp('==', BinaryOp('%', Id('i'), IntLiteral(2)),
                                                                  IntLiteral(0)), [], [
                                                             Assign(ArrayCell(Id('arr'), [Id('i')]),
                                                                    BinaryOp('\\', Id('i'), IntLiteral(2)))]), (
                                                        BinaryOp('==', BinaryOp('%', Id('i'), IntLiteral(3)),
                                                                 IntLiteral(0)), [], [
                                                            Assign(ArrayCell(Id('arr'), [Id('i')]),
                                                                   BinaryOp('*.', IntLiteral(3), Id('i')))]), (
                                                        BinaryOp('==', BinaryOp('%', Id('i'), IntLiteral(5)),
                                                                 IntLiteral(1)), [],
                                                        [Assign(ArrayCell(Id('arr'), [Id('i')]), Id('i'))])], ([], [
                                   Assign(ArrayCell(Id('arr'), [Id('i')]),
                                          ArrayCell(Id('output'), [Id('i')]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_case_36(self):
        input = """
        Var:x ;
        Var: f = 1232324.e23432;
        Function: main
        Parameter: a[2], b
        Body:
            While i < 10 Do
                While i < 10 Do
                    For (i = init(), con(), up()) Do
                    EndFor.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('f'), [], FloatLiteral('inf')),
                          FuncDecl(Id('main'), [VarDecl(Id('a'), [2], None), VarDecl(Id('b'), [], None)], ([], [
                              While(BinaryOp('<', Id('i'), IntLiteral(10)), ([], [
                                  While(BinaryOp('<', Id('i'), IntLiteral(10)), ([], [
                                      For(Id('i'), CallExpr(Id('init'), []), CallExpr(Id('con'), []),
                                          CallExpr(Id('up'), []), ([], []))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_case_37(self):
        input = """Var:x;
        Function: test
        Body:
            f = -1234.;
            Do 
                Do
                    If k Then If k Then EndIf. EndIf.
                While False
                EndDo.
            While f < 10
            EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None), FuncDecl(Id('test'), [], ([], [
            Assign(Id('f'), UnaryOp('-', FloatLiteral(1234.0))), Dowhile(([], [
                Dowhile(([], [If([(Id('k'), [], [If([(Id('k'), [], [])], ([], []))])], ([], []))]),
                        BooleanLiteral(False))]), BinaryOp('<', Id('f'), IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_case_38(self):
        input = """
        Var: s = "dad";
        Function: sum
        Body:
            Var: sum = 0.;
            For (i = init(i * init()), cond(c *. c() - c(c())), step(step - step(step \. step(step % step)))) Do
                sum = sum + random(randint(range(0, rand())));
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id('s'), [], StringLiteral("""dad""")), FuncDecl(Id('sum'), [], (
        [VarDecl(Id('sum'), [], FloatLiteral(0.0))], [
            For(Id('i'), CallExpr(Id('init'), [BinaryOp('*', Id('i'), CallExpr(Id('init'), []))]), CallExpr(Id('cond'),
                                                                                                            [BinaryOp(
                                                                                                                '-',
                                                                                                                BinaryOp(
                                                                                                                    '*.',
                                                                                                                    Id(
                                                                                                                        'c'),
                                                                                                                    CallExpr(
                                                                                                                        Id(
                                                                                                                            'c'),
                                                                                                                        [])),
                                                                                                                CallExpr(
                                                                                                                    Id(
                                                                                                                        'c'),
                                                                                                                    [
                                                                                                                        CallExpr(
                                                                                                                            Id(
                                                                                                                                'c'),
                                                                                                                            [])]))]),
                CallExpr(Id('step'), [BinaryOp('-', Id('step'), CallExpr(Id('step'), [
                    BinaryOp('\.', Id('step'), CallExpr(Id('step'), [BinaryOp('%', Id('step'), Id('step'))]))]))]), ([],
                                                                                                                     [
                                                                                                                         Assign(
                                                                                                                             Id(
                                                                                                                                 'sum'),
                                                                                                                             BinaryOp(
                                                                                                                                 '+',
                                                                                                                                 Id(
                                                                                                                                     'sum'),
                                                                                                                                 CallExpr(
                                                                                                                                     Id(
                                                                                                                                         'random'),
                                                                                                                                     [
                                                                                                                                         CallExpr(
                                                                                                                                             Id(
                                                                                                                                                 'randint'),
                                                                                                                                             [
                                                                                                                                                 CallExpr(
                                                                                                                                                     Id(
                                                                                                                                                         'range'),
                                                                                                                                                     [
                                                                                                                                                         IntLiteral(
                                                                                                                                                             0),
                                                                                                                                                         CallExpr(
                                                                                                                                                             Id(
                                                                                                                                                                 'rand'),
                                                                                                                                                             [])])])])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_case_39(self):
        input = """
        Var: s;
        Function: reverse
        Parameter: str
        Body:
            For(i = 0, i < len(str) \ 2, s) Do
                str[i] = str[len(str) - i - 1];
            EndFor.
        EndBody."""
        expect = Program([VarDecl(Id('s'), [], None), FuncDecl(Id('reverse'), [VarDecl(Id('str'), [], None)], ([], [
            For(Id('i'), IntLiteral(0),
                BinaryOp('<', Id('i'), BinaryOp('\\', CallExpr(Id('len'), [Id('str')]), IntLiteral(2))), Id('s'), ([], [
                    Assign(ArrayCell(Id('str'), [Id('i')]), ArrayCell(Id('str'), [
                        BinaryOp('-', BinaryOp('-', CallExpr(Id('len'), [Id('str')]), Id('i')),
                                 IntLiteral(1))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_case_40(self):
        input = """
        Var: ar[0x13][0o2][23];
        Function: ppl
        Parameter: threshold
        Body:
            If score >= threshold Then
                Return "Pass";
            Else
                Return "Again";
            EndIf.
            Return ppl;
        EndBody."""
        expect = Program([VarDecl(Id('ar'), [19, 2, 23], None),
                          FuncDecl(Id('ppl'), [VarDecl(Id('threshold'), [], None)], ([], [If(
                              [(BinaryOp('>=', Id('score'), Id('threshold')), [], [Return(StringLiteral("""Pass"""))])],
                              ([], [Return(StringLiteral("""Again"""))])), Return(Id('ppl'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_case_41(self):
        input = """
        Function: dfff
        Body:
            Var: s[100];
            While !empty(s) Do
                print(pop(s));
            EndWhile.
            While !full(s) Do
                s = push(s, vr());
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id('dfff'), [], ([VarDecl(Id('s'), [100], None)], [
            While(UnaryOp('!', CallExpr(Id('empty'), [Id('s')])),
                  ([], [CallStmt(Id('print'), [CallExpr(Id('pop'), [Id('s')])])])),
            While(UnaryOp('!', CallExpr(Id('full'), [Id('s')])),
                  ([], [Assign(Id('s'), CallExpr(Id('push'), [Id('s'), CallExpr(Id('vr'), [])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_case_42(self):
        input = """
        Function: main
        Parameter: arr
        Body:
            print(1 + 2, 0x22)[f()[2][3+arr[3]]] = arr[2 * f()[f()]];
        EndBody.
        """
        expect = Program([FuncDecl(Id('main'), [VarDecl(Id('arr'), [], None)], ([], [Assign(
            ArrayCell(CallExpr(Id('print'), [BinaryOp('+', IntLiteral(1), IntLiteral(2)), IntLiteral(34)]), [
                ArrayCell(CallExpr(Id('f'), []),
                          [IntLiteral(2), BinaryOp('+', IntLiteral(3), ArrayCell(Id('arr'), [IntLiteral(3)]))])]),
            ArrayCell(Id('arr'),
                      [BinaryOp('*', IntLiteral(2), ArrayCell(CallExpr(Id('f'), []), [CallExpr(Id('f'), [])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_case_43(self):
        input = """
        Function: fn
        Body:
            f(f(2 + 2));
            If i == 0 Then
                If True Then
                    If t Then ElseIf con Then ElseIf con Then Else EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id('fn'), [], ([], [
            CallStmt(Id('f'), [CallExpr(Id('f'), [BinaryOp('+', IntLiteral(2), IntLiteral(2))])]), If([(BinaryOp('==',
                                                                                                                 Id(
                                                                                                                     'i'),
                                                                                                                 IntLiteral(
                                                                                                                     0)),
                                                                                                        [], [If([(
                                                                                                                 BooleanLiteral(
                                                                                                                     True),
                                                                                                                 [], [
                                                                                                                     If(
                                                                                                                         [
                                                                                                                             (
                                                                                                                             Id(
                                                                                                                                 't'),
                                                                                                                             [],
                                                                                                                             []),
                                                                                                                             (
                                                                                                                             Id(
                                                                                                                                 'con'),
                                                                                                                             [],
                                                                                                                             []),
                                                                                                                             (
                                                                                                                             Id(
                                                                                                                                 'con'),
                                                                                                                             [],
                                                                                                                             [])],
                                                                                                                         (
                                                                                                                         [],
                                                                                                                         []))])],
                                                                                                                ([],
                                                                                                                 []))])],
                                                                                                      ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_case_44(self):
        input = """Var: x;
        Function: symmetry
        Body:
            Var: str = "";
            str = str(input());
            For(i = 0, i < len(str) \. 2, 1) Do
                If str[i] != str[len(str) - i - 1] Then
                    Return False;
                EndIf.
            EndFor.
            Return True;
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None), FuncDecl(Id('symmetry'), [], (
        [VarDecl(Id('str'), [], StringLiteral(""""""))],
        [Assign(Id('str'), CallExpr(Id('str'), [CallExpr(Id('input'), [])])), For(Id('i'), IntLiteral(0),
                                                                                  BinaryOp('<', Id('i'), BinaryOp('\.',
                                                                                                                  CallExpr(
                                                                                                                      Id(
                                                                                                                          'len'),
                                                                                                                      [
                                                                                                                          Id(
                                                                                                                              'str')]),
                                                                                                                  IntLiteral(
                                                                                                                      2))),
                                                                                  IntLiteral(1), ([], [If([(BinaryOp(
                '!=', ArrayCell(Id('str'), [Id('i')]), ArrayCell(Id('str'), [
                    BinaryOp('-', BinaryOp('-', CallExpr(Id('len'), [Id('str')]), Id('i')), IntLiteral(1))])), [], [
                                                                                                                Return(
                                                                                                                    BooleanLiteral(
                                                                                                                        False))])],
                                                                                                          ([], []))])),
         Return(BooleanLiteral(True)), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_case_45(self):
        input = """Var: x;
        Function: test
        Body:
            While True Do
                v = receive(socket, max_len);
                If v Then
                    handle();
                Else
                    raise(error("failed"));
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None), FuncDecl(Id('test'), [], ([], [While(BooleanLiteral(True), ([], [
            Assign(Id('v'), CallExpr(Id('receive'), [Id('socket'), Id('max_len')])),
            If([(Id('v'), [], [CallStmt(Id('handle'), [])])],
               ([], [CallStmt(Id('raise'), [CallExpr(Id('error'), [StringLiteral("""failed""")])])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_case_46(self):
        input = """
        Var: b = False, arr[0o10] = {120, 0x123};
        Function: test
        Body:
            Do
                While True Do
                    lock();
                    send(i + 1);
                    unlock();
                EndWhile.
            While True EndDo.
        EndBody."""
        expect = Program([VarDecl(Id('b'), [], BooleanLiteral(False)),
                          VarDecl(Id('arr'), [8], ArrayLiteral([IntLiteral(120), IntLiteral(291)])),
                          FuncDecl(Id('test'), [], ([], [Dowhile(([], [While(BooleanLiteral(True), ([], [
                              CallStmt(Id('lock'), []), CallStmt(Id('send'), [BinaryOp('+', Id('i'), IntLiteral(1))]),
                              CallStmt(Id('unlock'), [])]))]), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_case_47(self):
        input = """
        Var: kk = {123, 0x13, 0o13, "dasd", {}};
        Function: main
        Body:
            While exp == exp() && !error() Do
                print("kfkfkf" * 4);
                If cond() Then
                    process();
                    log();
                    Break;
                ElseIf k Then
                    handle();
                    error();
                    log();
                Else
                    log();
                    close();
                    finish();
                EndIf.
            EndWhile. 
        EndBody."""
        expect = Program([VarDecl(Id('kk'), [], ArrayLiteral(
            [IntLiteral(123), IntLiteral(19), IntLiteral(11), StringLiteral("""dasd"""), ArrayLiteral([])])),
                          FuncDecl(Id('main'), [], ([], [While(BinaryOp('==', Id('exp'),
                                                                        BinaryOp('&&', CallExpr(Id('exp'), []),
                                                                                 UnaryOp('!',
                                                                                         CallExpr(Id('error'), [])))), (
                                                               [], [CallStmt(Id('print'), [
                                                                   BinaryOp('*', StringLiteral("""kfkfkf"""),
                                                                            IntLiteral(4))]), If([(CallExpr(Id('cond'),
                                                                                                            []), [], [
                                                                                                       CallStmt(Id(
                                                                                                           'process'),
                                                                                                                []),
                                                                                                       CallStmt(
                                                                                                           Id('log'),
                                                                                                           []),
                                                                                                       Break()]), (
                                                                                                  Id('k'), [], [
                                                                                                      CallStmt(
                                                                                                          Id('handle'),
                                                                                                          []), CallStmt(
                                                                                                          Id('error'),
                                                                                                          []), CallStmt(
                                                                                                          Id('log'),
                                                                                                          [])])], ([], [
                                                                   CallStmt(Id('log'), []), CallStmt(Id('close'), []),
                                                                   CallStmt(Id('finish'), [])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_case_48(self):
        input = """
        Var: x;
        Function: test
        Body:
            Var: x = 10;
            Var: mm[10] = {1, 0x123, 0o123, "dasd"};
            If k == 10 Then
                While True Do
                    move_left();
                    Do 
                        For(i = 0, i < upper(), step) Do
                            While k > 10 Do
                                print("das", 123, exp(p + 2));
                            EndWhile.
                        EndFor.
                    While k == True EndDo.
                EndWhile.
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id('x'), [], None), FuncDecl(Id('test'), [], ([VarDecl(Id('x'), [], IntLiteral(10)),
                                                                                 VarDecl(Id('mm'), [10], ArrayLiteral(
                                                                                     [IntLiteral(1), IntLiteral(291),
                                                                                      IntLiteral(83),
                                                                                      StringLiteral("""dasd""")]))], [
                                                                                    If([(BinaryOp('==', Id('k'),
                                                                                                  IntLiteral(10)), [], [
                                                                                             While(BooleanLiteral(True),
                                                                                                   ([], [CallStmt(
                                                                                                       Id('move_left'),
                                                                                                       []), Dowhile(([],
                                                                                                                     [
                                                                                                                         For(
                                                                                                                             Id(
                                                                                                                                 'i'),
                                                                                                                             IntLiteral(
                                                                                                                                 0),
                                                                                                                             BinaryOp(
                                                                                                                                 '<',
                                                                                                                                 Id(
                                                                                                                                     'i'),
                                                                                                                                 CallExpr(
                                                                                                                                     Id(
                                                                                                                                         'upper'),
                                                                                                                                     [])),
                                                                                                                             Id(
                                                                                                                                 'step'),
                                                                                                                             (
                                                                                                                             [],
                                                                                                                             [
                                                                                                                                 While(
                                                                                                                                     BinaryOp(
                                                                                                                                         '>',
                                                                                                                                         Id(
                                                                                                                                             'k'),
                                                                                                                                         IntLiteral(
                                                                                                                                             10)),
                                                                                                                                     (
                                                                                                                                     [],
                                                                                                                                     [
                                                                                                                                         CallStmt(
                                                                                                                                             Id(
                                                                                                                                                 'print'),
                                                                                                                                             [
                                                                                                                                                 StringLiteral(
                                                                                                                                                     """das"""),
                                                                                                                                                 IntLiteral(
                                                                                                                                                     123),
                                                                                                                                                 CallExpr(
                                                                                                                                                     Id(
                                                                                                                                                         'exp'),
                                                                                                                                                     [
                                                                                                                                                         BinaryOp(
                                                                                                                                                             '+',
                                                                                                                                                             Id(
                                                                                                                                                                 'p'),
                                                                                                                                                             IntLiteral(
                                                                                                                                                                 2))])])]))]))]),
                                                                                                                    BinaryOp(
                                                                                                                        '==',
                                                                                                                        Id(
                                                                                                                            'k'),
                                                                                                                        BooleanLiteral(
                                                                                                                            True)))]))])],
                                                                                       ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_case_49(self):
        input = """
        Var: var = {0o123, 123., 123e-1, "das", 0x123};
        Function: test
        Body:
            Var: x = 12;
            For(i = "dasd" * 12, "dasd", "d") Do
                Var: m = 10;
                If m != 10 Then
                    Var: x;
                    x = int(input());
                ElseIf m && False Then
                    Var: x;
                    print(x);
                Else
                    Do
                        Var: k;
                        k = int(input());
                        If k == 10 Then
                            Var: i;
                            Break;
                        EndIf.
                    While True EndDo.
                EndIf.
            EndFor.
        EndBody."""
        expect = Program([VarDecl(Id('var'), [], ArrayLiteral(
            [IntLiteral(83), FloatLiteral(123.0), FloatLiteral(12.3), StringLiteral("""das"""), IntLiteral(291)])),
                          FuncDecl(Id('test'), [], ([VarDecl(Id('x'), [], IntLiteral(12))], [
                              For(Id('i'), BinaryOp('*', StringLiteral("""dasd"""), IntLiteral(12)),
                                  StringLiteral("""dasd"""), StringLiteral("""d"""), (
                                  [VarDecl(Id('m'), [], IntLiteral(10))], [If([(BinaryOp('!=', Id('m'), IntLiteral(10)),
                                                                                [VarDecl(Id('x'), [], None)], [
                                                                                    Assign(Id('x'), CallExpr(Id('int'),
                                                                                                             [CallExpr(
                                                                                                                 Id(
                                                                                                                     'input'),
                                                                                                                 [])]))]),
                                                                               (BinaryOp('&&', Id('m'),
                                                                                         BooleanLiteral(False)),
                                                                                [VarDecl(Id('x'), [], None)],
                                                                                [CallStmt(Id('print'), [Id('x')])])], (
                                                                              [], [Dowhile((
                                                                                           [VarDecl(Id('k'), [], None)],
                                                                                           [Assign(Id('k'),
                                                                                                   CallExpr(Id('int'), [
                                                                                                       CallExpr(
                                                                                                           Id('input'),
                                                                                                           [])])), If([(
                                                                                                                       BinaryOp(
                                                                                                                           '==',
                                                                                                                           Id(
                                                                                                                               'k'),
                                                                                                                           IntLiteral(
                                                                                                                               10)),
                                                                                                                       [
                                                                                                                           VarDecl(
                                                                                                                               Id(
                                                                                                                                   'i'),
                                                                                                                               [],
                                                                                                                               None)],
                                                                                                                       [
                                                                                                                           Break()])],
                                                                                                                      (
                                                                                                                      [],
                                                                                                                      []))]),
                                                                                           BooleanLiteral(
                                                                                               True))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_case_50(self):
        input = r"""
    Function: main
        Body:
            If True Then
            Else
                Var: a, b;
                foo1();
                foo2();
            EndIf.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], [])],
                   ([VarDecl(Id("a"), [], None),
                     VarDecl(Id("b"), [], None)],
                    [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_case_51(self):
        input = r"""
    Function: main
        Body:
            While True Do
            EndWhile.
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], [While(BooleanLiteral(True), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_case_52(self):
        input = r"""
    Function: main
        Body:
            While True Do
                Var: a;
            EndWhile.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([VarDecl(Id("a"), [], None)], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_case_53(self):
        input = r"""
    Function: main
        Body:
            While True Do
                foo();
            EndWhile.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([], [CallStmt(Id("foo"), [])]))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_case_54(self):
        input = r"""
    Function: main
        Body:
            While True Do
                Var: a, b;
                foo1();
                foo2();
            EndWhile.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                While(
                    BooleanLiteral(True),
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_case_55(self):
        input = r"""
    Function: main
        Body:
            Do
            While True
            EndDo.
        EndBody.
    """
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Dowhile(([], []), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_case_56(self):
        input = r"""
    Function: main
        Body:
            Do
                Var: a;
            While True
            EndDo.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([VarDecl(Id("a"), [], None)], []), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_case_57(self):
        input = r"""
    Function: main
        Body:
            Do
                foo();
            While True
            EndDo.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([], [CallStmt(Id("foo"), [])]), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_case_58(self):
        input = r"""
    Function: main
        Body:
            Do
                Var: a, b;
                foo1();
                foo2();
            While True
            EndDo.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Dowhile(
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]), BooleanLiteral(True))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_case_59(self):
        input = r"""
    Function: main
        Body:
            For (a = 1, a < 10, 1) Do
            EndFor.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1),
                    ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_case_60(self):
        input = """
        Function: mean
        Parameter: arr
        Body:
            If len(arr) == 0 Then Return; EndIf.
            m = mean(arr, axis, {1, 2, 3, 4, 5});
            Do
                mean(arr, 1, n, len(arr) - 1);
            While !((flag == False) || (flag != 23) * (flag <=. 123)) EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id('mean'), [VarDecl(Id('arr'), [], None)], ([], [
            If([(BinaryOp('==', CallExpr(Id('len'), [Id('arr')]), IntLiteral(0)), [], [Return(None)])], ([], [])),
            Assign(Id('m'), CallExpr(Id('mean'), [Id('arr'), Id('axis'), ArrayLiteral(
                [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)])])), Dowhile(([], [
                CallStmt(Id('mean'), [Id('arr'), IntLiteral(1), Id('n'),
                                      BinaryOp('-', CallExpr(Id('len'), [Id('arr')]), IntLiteral(1))])]), UnaryOp('!',
                                                                                                                  BinaryOp(
                                                                                                                      '||',
                                                                                                                      BinaryOp(
                                                                                                                          '==',
                                                                                                                          Id(
                                                                                                                              'flag'),
                                                                                                                          BooleanLiteral(
                                                                                                                              False)),
                                                                                                                      BinaryOp(
                                                                                                                          '*',
                                                                                                                          BinaryOp(
                                                                                                                              '!=',
                                                                                                                              Id(
                                                                                                                                  'flag'),
                                                                                                                              IntLiteral(
                                                                                                                                  23)),
                                                                                                                          BinaryOp(
                                                                                                                              '<=.',
                                                                                                                              Id(
                                                                                                                                  'flag'),
                                                                                                                              IntLiteral(
                                                                                                                                  123))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_case_61(self):
        input = """
        Function: test
        Parameter: arr[0x1000], low, high
        Body:
            Var: min, max;
            For(i = 1, i < high, 1) Do
                For(j = 0, j < i, 1) Do
                    If arr[j] < min Then
                        min = arr[j];
                    ElseIf arr[j] > max Then
                        max = arr[j];
                    Else
                        print("************");
                        print("NO OPERATION");
                        print("************");
                    EndIf.
                    While min =/= max Do
                        Var: temp;
                        For(i = low, i < high, 1) Do
                            println(arr[i]);
                        EndFor.
                    EndWhile.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [VarDecl(Id('arr'), [4096], None), VarDecl(Id('low'), [], None),
                                                VarDecl(Id('high'), [], None)], (
                                   [VarDecl(Id('min'), [], None), VarDecl(Id('max'), [], None)], [
                                       For(Id('i'), IntLiteral(1), BinaryOp('<', Id('i'), Id('high')), IntLiteral(1), (
                                       [], [For(Id('j'), IntLiteral(0), BinaryOp('<', Id('j'), Id('i')), IntLiteral(1),
                                                ([], [If([(
                                                          BinaryOp('<', ArrayCell(Id('arr'), [Id('j')]), Id('min')), [],
                                                          [Assign(Id('min'), ArrayCell(Id('arr'), [Id('j')]))]), (
                                                          BinaryOp('>', ArrayCell(Id('arr'), [Id('j')]), Id('max')), [],
                                                          [Assign(Id('max'), ArrayCell(Id('arr'), [Id('j')]))])], ([], [
                                                    CallStmt(Id('print'), [StringLiteral("""************""")]),
                                                    CallStmt(Id('print'), [StringLiteral("""NO OPERATION""")]),
                                                    CallStmt(Id('print'), [StringLiteral("""************""")])])),
                                                      While(BinaryOp('=/=', Id('min'), Id('max')), (
                                                      [VarDecl(Id('temp'), [], None)], [
                                                          For(Id('i'), Id('low'), BinaryOp('<', Id('i'), Id('high')),
                                                              IntLiteral(1), ([], [CallStmt(Id('println'), [
                                                                  ArrayCell(Id('arr'), [Id('i')])])]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_case_62(self):
        input = """
        Function: test
        Body:
            Var: flag;
            flag = (True != 123) + !3 * (False && kj % 123 <. f());
            praaa(--------.-.-(!123 == kk * 12 - 3)||False + !!!!!!9==4);
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [], ([VarDecl(Id('flag'), [], None)], [Assign(Id('flag'), BinaryOp('+',
                                                                                                                  BinaryOp(
                                                                                                                      '!=',
                                                                                                                      BooleanLiteral(
                                                                                                                          True),
                                                                                                                      IntLiteral(
                                                                                                                          123)),
                                                                                                                  BinaryOp(
                                                                                                                      '*',
                                                                                                                      UnaryOp(
                                                                                                                          '!',
                                                                                                                          IntLiteral(
                                                                                                                              3)),
                                                                                                                      BinaryOp(
                                                                                                                          '<.',
                                                                                                                          BinaryOp(
                                                                                                                              '&&',
                                                                                                                              BooleanLiteral(
                                                                                                                                  False),
                                                                                                                              BinaryOp(
                                                                                                                                  '%',
                                                                                                                                  Id(
                                                                                                                                      'kj'),
                                                                                                                                  IntLiteral(
                                                                                                                                      123))),
                                                                                                                          CallExpr(
                                                                                                                              Id(
                                                                                                                                  'f'),
                                                                                                                              []))))),
                                                                                      CallStmt(Id('praaa'), [
                                                                                          BinaryOp('==', BinaryOp('||',
                                                                                                                  UnaryOp(
                                                                                                                      '-',
                                                                                                                      UnaryOp(
                                                                                                                          '-',
                                                                                                                          UnaryOp(
                                                                                                                              '-',
                                                                                                                              UnaryOp(
                                                                                                                                  '-',
                                                                                                                                  UnaryOp(
                                                                                                                                      '-',
                                                                                                                                      UnaryOp(
                                                                                                                                          '-',
                                                                                                                                          UnaryOp(
                                                                                                                                              '-',
                                                                                                                                              UnaryOp(
                                                                                                                                                  '-.',
                                                                                                                                                  UnaryOp(
                                                                                                                                                      '-.',
                                                                                                                                                      UnaryOp(
                                                                                                                                                          '-',
                                                                                                                                                          BinaryOp(
                                                                                                                                                              '==',
                                                                                                                                                              UnaryOp(
                                                                                                                                                                  '!',
                                                                                                                                                                  IntLiteral(
                                                                                                                                                                      123)),
                                                                                                                                                              BinaryOp(
                                                                                                                                                                  '-',
                                                                                                                                                                  BinaryOp(
                                                                                                                                                                      '*',
                                                                                                                                                                      Id(
                                                                                                                                                                          'kk'),
                                                                                                                                                                      IntLiteral(
                                                                                                                                                                          12)),
                                                                                                                                                                  IntLiteral(
                                                                                                                                                                      3))))))))))))),
                                                                                                                  BinaryOp(
                                                                                                                      '+',
                                                                                                                      BooleanLiteral(
                                                                                                                          False),
                                                                                                                      UnaryOp(
                                                                                                                          '!',
                                                                                                                          UnaryOp(
                                                                                                                              '!',
                                                                                                                              UnaryOp(
                                                                                                                                  '!',
                                                                                                                                  UnaryOp(
                                                                                                                                      '!',
                                                                                                                                      UnaryOp(
                                                                                                                                          '!',
                                                                                                                                          UnaryOp(
                                                                                                                                              '!',
                                                                                                                                              IntLiteral(
                                                                                                                                                  9))))))))),
                                                                                                   IntLiteral(4))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_case_63(self):
        input = """
        Function: test
        Parameter: str
        Body:
            Var: dt;
            For(i = 0, i < len(str), 1) Do
                dt[dt[dt[arr[i]]]] = dt[arr[dt[arr[i]]]] + 1;
                f(dt, k * {1, 2, 3, 4});
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [VarDecl(Id('str'), [], None)], ([VarDecl(Id('dt'), [], None)], [
            For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), CallExpr(Id('len'), [Id('str')])), IntLiteral(1), ([], [
                Assign(ArrayCell(Id('dt'),
                                 [ArrayCell(Id('dt'), [ArrayCell(Id('dt'), [ArrayCell(Id('arr'), [Id('i')])])])]),
                       BinaryOp('+', ArrayCell(Id('dt'), [
                           ArrayCell(Id('arr'), [ArrayCell(Id('dt'), [ArrayCell(Id('arr'), [Id('i')])])])]),
                                IntLiteral(1))), CallStmt(Id('f'), [Id('dt'), BinaryOp('*', Id('k'), ArrayLiteral(
                    [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_case_64(self):
        input = """
        Var: x;
        Var: arr[123] = {1, 2, 3, 5, "dasd", {12, {12}}};
        Function: test
        Parameter: array
        Body:
            While array Do
                If arr Then
                    For(i = 0, i < length(arr), step()) Do
                        print(arr[i] * kk);
                    EndFor.
                    If True && (123 == 3123) Then
                        do();
                        Break;
                    EndIf.
                EndIf.
            EndWhile.
            Return;
        EndBody.
        """
        expect = Program([VarDecl(Id('x'), [], None), VarDecl(Id('arr'), [123], ArrayLiteral(
            [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(5), StringLiteral("""dasd"""),
             ArrayLiteral([IntLiteral(12), ArrayLiteral([IntLiteral(12)])])])),
                          FuncDecl(Id('test'), [VarDecl(Id('array'), [], None)], ([], [While(Id('array'), ([], [If([(Id(
                              'arr'), [], [For(Id('i'), IntLiteral(0),
                                               BinaryOp('<', Id('i'), CallExpr(Id('length'), [Id('arr')])),
                                               CallExpr(Id('step'), []), ([], [
                                  CallStmt(Id('print'), [BinaryOp('*', ArrayCell(Id('arr'), [Id('i')]), Id('kk'))])])),
                                           If([(BinaryOp('&&', BooleanLiteral(True),
                                                         BinaryOp('==', IntLiteral(123), IntLiteral(3123))), [],
                                                [CallStmt(Id('do'), []), Break()])], ([], []))])], ([], []))])),
                                                                                       Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_case_65(self):
        input = """
        Function: test
        Body:
            Var: kASKHD0123;
            Do
                Var: l123OKKD;
                While l123OKDS Do
                    print()[13] = {1,2,3,4,5,6,7,8,9};
                EndWhile.
            While False EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id('test'), [], ([VarDecl(Id('kASKHD0123'), [], None)], [Dowhile(([VarDecl(
            Id('l123OKKD'), [], None)], [While(Id('l123OKDS'), ([], [
            Assign(ArrayCell(CallExpr(Id('print'), []), [IntLiteral(13)]), ArrayLiteral(
                [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5), IntLiteral(6),
                 IntLiteral(7), IntLiteral(8), IntLiteral(9)]))]))]), BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_case_66(self):
        input = ""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_case_67(self):
        input = """
        Function: test
        Body:
            For(i = 0, i < 100, up()) Do
                If i % 2 == 0 Then
                    Break;
                    Continue;
                ElseIf i > 10 Then
                    w(i);
                EndIf.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [], ([], [
            For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), IntLiteral(100)), CallExpr(Id('up'), []), ([], [If(
                [(BinaryOp('==', BinaryOp('%', Id('i'), IntLiteral(2)), IntLiteral(0)), [], [Break(), Continue()]),
                 (BinaryOp('>', Id('i'), IntLiteral(10)), [], [CallStmt(Id('w'), [Id('i')])])], ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_case_68(self):
        input = """
        Function: swap
        Parameter: a, b
        Body:
            Var: temp;
            temp = a;
            a = b;
            b = temp;
        EndBody."""
        expect = Program([FuncDecl(Id('swap'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], (
        [VarDecl(Id('temp'), [], None)],
        [Assign(Id('temp'), Id('a')), Assign(Id('a'), Id('b')), Assign(Id('b'), Id('temp'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_case_69(self):
        input = """
        Function: max
        Parameter: x, y
        Body:
            If x > y Then
                Return x;
            Else
                Return y;
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: a = 10, b = 20;
            print("%d", max(a, b));
            Return;
        EndBody."""
        expect = Program([FuncDecl(Id('max'), [VarDecl(Id('x'), [], None), VarDecl(Id('y'), [], None)], (
        [], [If([(BinaryOp('>', Id('x'), Id('y')), [], [Return(Id('x'))])], ([], [Return(Id('y'))]))])),
                          FuncDecl(Id('main'), [], (
                          [VarDecl(Id('a'), [], IntLiteral(10)), VarDecl(Id('b'), [], IntLiteral(20))],
                          [CallStmt(Id('print'), [StringLiteral("""%d"""), CallExpr(Id('max'), [Id('a'), Id('b')])]),
                           Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_case_70(self):
        input = r"""
    Function: main
        Body:
            a = { {1, 2}, {3, 4} };
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                        ArrayLiteral([IntLiteral(3), IntLiteral(4)])
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_case_71(self):
        input = r"""
    Function: main
        Body:
            a = {{{{{{{{{{{1}}}}}}}}}}};
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([
                            ArrayLiteral([
                                ArrayLiteral([
                                    ArrayLiteral([
                                        ArrayLiteral([
                                            ArrayLiteral([
                                                ArrayLiteral([
                                                    ArrayLiteral([
                                                        ArrayLiteral(
                                                            [ArrayLiteral([IntLiteral(1)])])
                                                    ])
                                                ])
                                            ])
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_case_72(self):
        input = r"""
    Function: main
        Body:
            a = {{{{1}}}, {{1}}, {1}, 1};
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]),
                        ArrayLiteral([ArrayLiteral([IntLiteral(1)])]),
                        ArrayLiteral([IntLiteral(1)]),
                        IntLiteral(1)
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_case_73(self):
        input = r"""
    Function: main
        Body:
            a = (a);
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_case_74(self):
        input = r"""
    Function: main
        Body:
            a = (((a)));
        EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_case_75(self):
        input = r"""
    Function: main
        Body:
            a = foo();
            a = foo(1, True, "", 1.);
            a = foo(foo(foo()));
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), CallExpr(Id("foo"), [])),
                Assign(
                    Id("a"),
                    CallExpr(
                        Id("foo"),
                        [IntLiteral(1),
                         BooleanLiteral(True),
                         StringLiteral(""),
                         FloatLiteral(1.0)])),
                Assign(Id("a"), CallExpr(Id("foo"),
                                         [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_case_76(self):
        input = r"""
    Function: main
        Body:
            a = a[1];
            a = a[-1][a];
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), ArrayCell(Id("a"), [IntLiteral(1)])),
                Assign(Id("a"), ArrayCell(
                    Id("a"), [UnaryOp("-", IntLiteral(1)), Id("a")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_case_77(self):
        input = r"""
    Function: main
        Body:
            a = foo()[1];
            a = foo()[-1];
            a = foo(1, True, 1., "abcd")[a][b][c];
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(1)])),
                Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), []), [UnaryOp("-", IntLiteral(1))])),
                Assign(
                    Id("a"),
                    ArrayCell(
                        CallExpr(Id("foo"), [
                            IntLiteral(1),
                            BooleanLiteral(True),
                            FloatLiteral(1.0),
                            StringLiteral(r"""abcd""")
                        ]), [Id("a"), Id("b"), Id("c")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

        """ Binary and unary operator """

    def test_case_78(self):
        input = r"""
    Function: main
        Body:
            a = 1 * 2;
            a = 1 *. 2;
            a = 1 \ 2;
            a = 1 \. 2;
            a = 1 % 2;
            a = 1 + 2;
            a = 1 +. 2;
            a = 1 - 2;
            a = 1 -. 2;
            a = 1 && 2;
            a = 1 || 2;
            a = 1 == 2;
            a = 1 != 2;
            a = 1 =/= 2;
            a = 1 < 2;
            a = 1 <. 2;
            a = 1 > 2;
            a = 1 >. 2;
            a = 1 <= 2;
            a = 1 <=. 2;
            a = 1 >= 2;
            a = 1 >=. 2;
            a = !1;
            a = -1;
            a = -.1;
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), BinaryOp("*", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("*.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("\\", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("\\.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("%", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("+.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("-", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("-.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("&&", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("||", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("==", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("!=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("=/=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<=.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">=.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), UnaryOp("!", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-.", IntLiteral(1)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_case_79(self):
        input = r"""
    Function: main
        Body:
            a = 1 * 2 * 3;
            a = 1 *. 2 *. 3;
            a = 1 \ 2 \ 3;
            a = 1 \. 2 \. 3;
            a = 1 % 2 % 3;
            a = 1 + 2 + 3;
            a = 1 +. 2 +. 3;
            a = 1 - 2 - 3;
            a = 1 -. 2 -. 3;
            a = 1 && 2 && 3;
            a = 1 || 2 || 3;
            a = !!1;
            a = --1;
            a = -.-.1;
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"),
                       BinaryOp("*", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("*.", BinaryOp("*.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("\\", BinaryOp("\\", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(
                    Id("a"),
                    BinaryOp("\\.", BinaryOp("\\.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("%", BinaryOp("%", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("+", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("+.", BinaryOp("+.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("-", BinaryOp("-", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("-.", BinaryOp("-.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("!", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-.", UnaryOp("-.", IntLiteral(1))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_case_80(self):
        input = """
        Function: mse
        Parameter: a, b
        Body:
            Var: sum = 0.;
            If len(a) =/= len(b) Then raise(error()); EndIf.
            For(i = 0, i < len(a), 1) Do
                sum = sum + (a[i] - b[i]) * (a[i] - b[i]);
            EndFor.
            print(sum * sum \. 2);
        EndBody.
        """
        expect = Program([FuncDecl(Id('mse'), [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)], (
        [VarDecl(Id('sum'), [], FloatLiteral(0.0))], [If([(BinaryOp('=/=', CallExpr(Id('len'), [Id('a')]),
                                                                    CallExpr(Id('len'), [Id('b')])), [],
                                                           [CallStmt(Id('raise'), [CallExpr(Id('error'), [])])])],
                                                         ([], [])), For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'),
                                                                                                         CallExpr(
                                                                                                             Id('len'),
                                                                                                             [Id(
                                                                                                                 'a')])),
                                                                        IntLiteral(1), ([], [Assign(Id('sum'),
                                                                                                    BinaryOp('+',
                                                                                                             Id('sum'),
                                                                                                             BinaryOp(
                                                                                                                 '*',
                                                                                                                 BinaryOp(
                                                                                                                     '-',
                                                                                                                     ArrayCell(
                                                                                                                         Id(
                                                                                                                             'a'),
                                                                                                                         [
                                                                                                                             Id(
                                                                                                                                 'i')]),
                                                                                                                     ArrayCell(
                                                                                                                         Id(
                                                                                                                             'b'),
                                                                                                                         [
                                                                                                                             Id(
                                                                                                                                 'i')])),
                                                                                                                 BinaryOp(
                                                                                                                     '-',
                                                                                                                     ArrayCell(
                                                                                                                         Id(
                                                                                                                             'a'),
                                                                                                                         [
                                                                                                                             Id(
                                                                                                                                 'i')]),
                                                                                                                     ArrayCell(
                                                                                                                         Id(
                                                                                                                             'b'),
                                                                                                                         [
                                                                                                                             Id(
                                                                                                                                 'i')])))))])),
                                                      CallStmt(Id('print'), [
                                                          BinaryOp('\.', BinaryOp('*', Id('sum'), Id('sum')),
                                                                   IntLiteral(2))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_case_81(self):
        input = """
        Var: arr[10][0o10] = {{1,2,3,4}, {1,2,3}, {2,3,4}};
        Function: main
        Body:
            For(i = 0, i < getlength(arr, axis(0)), 1) Do
                Var: j = 0;
                While (isvalid(arr, axis(1), j)) Do
                    print(arr[i][j] * 10);
                    j = j + 1;
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program([VarDecl(Id('arr'), [10, 8], ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
             ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
             ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)])])), FuncDecl(Id('main'), [], ([], [
            For(Id('i'), IntLiteral(0),
                BinaryOp('<', Id('i'), CallExpr(Id('getlength'), [Id('arr'), CallExpr(Id('axis'), [IntLiteral(0)])])),
                IntLiteral(1), ([VarDecl(Id('j'), [], IntLiteral(0))], [
                    While(CallExpr(Id('isvalid'), [Id('arr'), CallExpr(Id('axis'), [IntLiteral(1)]), Id('j')]), ([], [
                        CallStmt(Id('print'),
                                 [BinaryOp('*', ArrayCell(Id('arr'), [Id('i'), Id('j')]), IntLiteral(10))]),
                        Assign(Id('j'), BinaryOp('+', Id('j'), IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_case_82(self):
        input = """
        Function: is_even
        Parameter: x
        Body:
            If x && 1 == 0 Then
                Return True;
            EndIf.
            Return False;
        EndBody."""
        expect = Program([FuncDecl(Id('is_even'), [VarDecl(Id('x'), [], None)], ([], [If([(BinaryOp('==', BinaryOp('&&',
                                                                                                                   Id(
                                                                                                                       'x'),
                                                                                                                   IntLiteral(
                                                                                                                       1)),
                                                                                                    IntLiteral(0)), [],
                                                                                           [Return(
                                                                                               BooleanLiteral(True))])],
                                                                                         ([], [])),
                                                                                      Return(BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_case_83(self):
        input = """
        Function: test
        Body:
            Return "dasd" * asd  - {1,2,3} || 82 == False;
        EndBody."""
        expect = Program([FuncDecl(Id('test'), [], ([], [Return(BinaryOp('==', BinaryOp('||', BinaryOp('-',
                                                                                                       BinaryOp('*',
                                                                                                                StringLiteral(
                                                                                                                    """dasd"""),
                                                                                                                Id(
                                                                                                                    'asd')),
                                                                                                       ArrayLiteral([
                                                                                                                        IntLiteral(
                                                                                                                            1),
                                                                                                                        IntLiteral(
                                                                                                                            2),
                                                                                                                        IntLiteral(
                                                                                                                            3)])),
                                                                                        IntLiteral(82)),
                                                                         BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_case_84(self):
        input = """
        Function: t____
        Parameter: n
        Body:
            create(size, {400, 400});
            For(i = enum(), isend(i), steps(iter())) Do
                sub(n, 1, i + 1);
                im = coverted(read("path", "w"), type);
                b = im[1];
                While b Do
                    im = draw(im, figure);
                    pop(p, rand());
                EndWhile.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id('t____'), [VarDecl(Id('n'), [], None)], ([], [
            CallStmt(Id('create'), [Id('size'), ArrayLiteral([IntLiteral(400), IntLiteral(400)])]),
            For(Id('i'), CallExpr(Id('enum'), []), CallExpr(Id('isend'), [Id('i')]),
                CallExpr(Id('steps'), [CallExpr(Id('iter'), [])]), ([], [
                    CallStmt(Id('sub'), [Id('n'), IntLiteral(1), BinaryOp('+', Id('i'), IntLiteral(1))]),
                    Assign(Id('im'), CallExpr(Id('coverted'), [
                        CallExpr(Id('read'), [StringLiteral("""path"""), StringLiteral("""w""")]), Id('type')])),
                    Assign(Id('b'), ArrayCell(Id('im'), [IntLiteral(1)])), While(Id('b'), ([], [
                        Assign(Id('im'), CallExpr(Id('draw'), [Id('im'), Id('figure')])),
                        CallStmt(Id('pop'), [Id('p'), CallExpr(Id('rand'), [])])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_case_85(self):
        input = """
        Var: k = False;
        Var: str = "no thing";
        Var: d = 123;
        Function: t___k
        Body:
        EndBody."""
        expect = Program(
            [VarDecl(Id('k'), [], BooleanLiteral(False)), VarDecl(Id('str'), [], StringLiteral("""no thing""")),
             VarDecl(Id('d'), [], IntLiteral(123)), FuncDecl(Id('t___k'), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_case_86(self):
        input = """
        Function: mmmmmmm
        Body:
            For(i = 0, i < len(row), 1) Do
                For(j = 0, i < len(col), 1) Do
                    result[i][j] = row[i] * col[j];
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('mmmmmmm'), [], ([], [
            For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), CallExpr(Id('len'), [Id('row')])), IntLiteral(1), ([], [
                For(Id('j'), IntLiteral(0), BinaryOp('<', Id('i'), CallExpr(Id('len'), [Id('col')])), IntLiteral(1), (
                [], [Assign(ArrayCell(Id('result'), [Id('i'), Id('j')]),
                            BinaryOp('*', ArrayCell(Id('row'), [Id('i')]), ArrayCell(Id('col'), [Id('j')])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_case_87(self):
        input = """
        Var: arr[100];
        Var: x;
        Function: binary_search
        Parameter: low, high
        Body:
            Var: mid;
            If low > high Then Return False; EndIf.
            mid = (low + high) \ 2;
            If (arr[mid] == x) Then Return False; EndIf.
            If (arr[mid] < x) Then
                Return binary_search(mid + 1, high);
            Else
                Return binary_search(low, mid - 1);
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id('arr'), [100], None), VarDecl(Id('x'), [], None),
                          FuncDecl(Id('binary_search'), [VarDecl(Id('low'), [], None), VarDecl(Id('high'), [], None)], (
                          [VarDecl(Id('mid'), [], None)],
                          [If([(BinaryOp('>', Id('low'), Id('high')), [], [Return(BooleanLiteral(False))])], ([], [])),
                           Assign(Id('mid'), BinaryOp('\\', BinaryOp('+', Id('low'), Id('high')), IntLiteral(2))), If([(
                                                                                                                       BinaryOp(
                                                                                                                           '==',
                                                                                                                           ArrayCell(
                                                                                                                               Id(
                                                                                                                                   'arr'),
                                                                                                                               [
                                                                                                                                   Id(
                                                                                                                                       'mid')]),
                                                                                                                           Id(
                                                                                                                               'x')),
                                                                                                                       [],
                                                                                                                       [
                                                                                                                           Return(
                                                                                                                               BooleanLiteral(
                                                                                                                                   False))])],
                                                                                                                      (
                                                                                                                      [],
                                                                                                                      [])),
                           If([(BinaryOp('<', ArrayCell(Id('arr'), [Id('mid')]), Id('x')), [], [Return(
                               CallExpr(Id('binary_search'), [BinaryOp('+', Id('mid'), IntLiteral(1)), Id('high')]))])],
                              ([], [Return(CallExpr(Id('binary_search'),
                                                    [Id('low'), BinaryOp('-', Id('mid'), IntLiteral(1))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_case_88(self):
        input = """
        Function: is_valid_index
        Parameter: arr[10], max_length, index
        Body:
            If index >= max_length Then raise(error());
            Else
                Return arr[index];
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('is_valid_index'),
                                   [VarDecl(Id('arr'), [10], None), VarDecl(Id('max_length'), [], None),
                                    VarDecl(Id('index'), [], None)], ([], [If([(BinaryOp('>=', Id('index'),
                                                                                         Id('max_length')), [], [
                                                                                    CallStmt(Id('raise'), [
                                                                                        CallExpr(Id('error'), [])])])],
                                                                              ([], [Return(ArrayCell(Id('arr'), [
                                                                                  Id('index')]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_case_89(self):
        input = """
        Function: no_ideas
        Body:
            If x % 2 == y % f() Then
                print(a[2]);
            ElseIf f() % g(f()) > f() * 12 - f[123] Then
            ElseIf x % 12 == 1 Then
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('no_ideas'), [], ([], [If([(BinaryOp('==', BinaryOp('%', Id('x'), IntLiteral(2)),
                                                                           BinaryOp('%', Id('y'),
                                                                                    CallExpr(Id('f'), []))), [], [
                                                                      CallStmt(Id('print'),
                                                                               [ArrayCell(Id('a'), [IntLiteral(2)])])]),
                                                                 (BinaryOp('>', BinaryOp('%', CallExpr(Id('f'), []),
                                                                                         CallExpr(Id('g'), [
                                                                                             CallExpr(Id('f'), [])])),
                                                                           BinaryOp('-',
                                                                                    BinaryOp('*', CallExpr(Id('f'), []),
                                                                                             IntLiteral(12)),
                                                                                    ArrayCell(Id('f'),
                                                                                              [IntLiteral(123)]))), [],
                                                                  []), (
                                                                 BinaryOp('==', BinaryOp('%', Id('x'), IntLiteral(12)),
                                                                          IntLiteral(1)), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_case_90(self):
        input = r"""
    Function: main
        Body:
            a = !(a + b);
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), UnaryOp("!", BinaryOp("+", Id("a"), Id("b"))))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_case_91(self):
        input = r"""
    Function: main
        Body:
            a = 1+-1;
        EndBody.
    """
        expect = Program([
            FuncDecl(
                Id("main"), [],
                ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_case_92(self):
        input = r"""
    Function: main
        Body:
            a = 1--2--3;
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("-", BinaryOp("-", IntLiteral(1), UnaryOp("-", IntLiteral(2))),
                             UnaryOp("-", IntLiteral(3))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_case_93(self):
        input = """
        Function: blink
        Body:
            sys_call(3 * 2, sys(delete("path")));
            print();
            function();
            If "" Then EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id('blink'), [], ([], [CallStmt(Id('sys_call'),
                                                                   [BinaryOp('*', IntLiteral(3), IntLiteral(2)),
                                                                    CallExpr(Id('sys'), [CallExpr(Id('delete'), [
                                                                        StringLiteral("""path""")])])]),
                                                          CallStmt(Id('print'), []), CallStmt(Id('function'), []),
                                                          If([(StringLiteral(""""""), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_case_94(self):
        input = """
        Function: test
        Body:
            print();
        EndBody.
        Function: fn1
        Body: runfn(); EndBody.
        Function: fn2
        Body: EndBody.
        Function: main
        Body: Return test() + fn1() + fn2(); EndBody."""
        expect = Program([FuncDecl(Id('test'), [], ([], [CallStmt(Id('print'), [])])),
                          FuncDecl(Id('fn1'), [], ([], [CallStmt(Id('runfn'), [])])), FuncDecl(Id('fn2'), [], ([], [])),
                          FuncDecl(Id('main'), [], ([], [Return(
                              BinaryOp('+', BinaryOp('+', CallExpr(Id('test'), []), CallExpr(Id('fn1'), [])),
                                       CallExpr(Id('fn2'), [])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_case_95(self):
        input = """
        Function: t__________________________
        Body:
            Var: y;
            k = 120;
            x[12] = 123;
            x = {1, 2, 3, 4, {4, 5}, {{{{{}}}}}};
        EndBody."""
        expect = Program([FuncDecl(Id('t__________________________'), [], ([VarDecl(Id('y'), [], None)],
                                                                           [Assign(Id('k'), IntLiteral(120)),
                                                                            Assign(ArrayCell(Id('x'), [IntLiteral(12)]),
                                                                                   IntLiteral(123)), Assign(Id('x'),
                                                                                                            ArrayLiteral(
                                                                                                                [
                                                                                                                    IntLiteral(
                                                                                                                        1),
                                                                                                                    IntLiteral(
                                                                                                                        2),
                                                                                                                    IntLiteral(
                                                                                                                        3),
                                                                                                                    IntLiteral(
                                                                                                                        4),
                                                                                                                    ArrayLiteral(
                                                                                                                        [
                                                                                                                            IntLiteral(
                                                                                                                                4),
                                                                                                                            IntLiteral(
                                                                                                                                5)]),
                                                                                                                    ArrayLiteral(
                                                                                                                        [
                                                                                                                            ArrayLiteral(
                                                                                                                                [
                                                                                                                                    ArrayLiteral(
                                                                                                                                        [
                                                                                                                                            ArrayLiteral(
                                                                                                                                                [
                                                                                                                                                    ArrayLiteral(
                                                                                                                                                        [])])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_case_96(self):
        input = r"""

    Function: main
        Body:
            a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    ArrayCell(Id("a"),
                              [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                    BinaryOp(
                        "+", ArrayCell(
                            Id("a"),
                            [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]), IntLiteral(4)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_case_97(self):
        input = """
        Function: testttt
        Body:
            For(iter = 0, iter < max_iter, 1) Do
                If do_some_thing() == end Then
                    Return;
                EndIf.
                Continue; 
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('testttt'), [], ([], [
            For(Id('iter'), IntLiteral(0), BinaryOp('<', Id('iter'), Id('max_iter')), IntLiteral(1), ([], [
                If([(BinaryOp('==', CallExpr(Id('do_some_thing'), []), Id('end')), [], [Return(None)])], ([], [])),
                Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_case_98(self):
        input = """Var: t;
        Function: t__Ddas
        Body:
            x = 2 -. 3 -. 4 + 123 + ((f() == 23) || 123) * 24 % (2 == 22);
        EndBody."""
        expect = Program([VarDecl(Id('t'), [], None), FuncDecl(Id('t__Ddas'), [], ([], [Assign(Id('x'), BinaryOp('+',
                                                                                                                 BinaryOp(
                                                                                                                     '+',
                                                                                                                     BinaryOp(
                                                                                                                         '-.',
                                                                                                                         BinaryOp(
                                                                                                                             '-.',
                                                                                                                             IntLiteral(
                                                                                                                                 2),
                                                                                                                             IntLiteral(
                                                                                                                                 3)),
                                                                                                                         IntLiteral(
                                                                                                                             4)),
                                                                                                                     IntLiteral(
                                                                                                                         123)),
                                                                                                                 BinaryOp(
                                                                                                                     '%',
                                                                                                                     BinaryOp(
                                                                                                                         '*',
                                                                                                                         BinaryOp(
                                                                                                                             '||',
                                                                                                                             BinaryOp(
                                                                                                                                 '==',
                                                                                                                                 CallExpr(
                                                                                                                                     Id(
                                                                                                                                         'f'),
                                                                                                                                     []),
                                                                                                                                 IntLiteral(
                                                                                                                                     23)),
                                                                                                                             IntLiteral(
                                                                                                                                 123)),
                                                                                                                         IntLiteral(
                                                                                                                             24)),
                                                                                                                     BinaryOp(
                                                                                                                         '==',
                                                                                                                         IntLiteral(
                                                                                                                             2),
                                                                                                                         IntLiteral(
                                                                                                                             22)))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_case_99(self):
        input = """
        Function: t_2937124
        Parameter: arr[100]
        Body:
            Var: sum = 0;
            create_multi_threads(num_threads);
            For (i = 0, i < len, 1) Do
                lock();
                sum = sum + arr[i];
                unlock();
            EndFor.
            destroy_all_resources();
        EndBody."""
        expect = Program([FuncDecl(Id('t_2937124'), [VarDecl(Id('arr'), [100], None)], (
        [VarDecl(Id('sum'), [], IntLiteral(0))], [CallStmt(Id('create_multi_threads'), [Id('num_threads')]),
                                                  For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), Id('len')),
                                                      IntLiteral(1), ([], [CallStmt(Id('lock'), []), Assign(Id('sum'),
                                                                                                            BinaryOp(
                                                                                                                '+', Id(
                                                                                                                    'sum'),
                                                                                                                ArrayCell(
                                                                                                                    Id(
                                                                                                                        'arr'),
                                                                                                                    [Id(
                                                                                                                        'i')]))),
                                                                           CallStmt(Id('unlock'), [])])),
                                                  CallStmt(Id('destroy_all_resources'), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_case_100(self):
        input = """
        Var: a, b = 120, c = "123", d[10] = {1,2,5};
        Var: f = {12, 3,4, {{}}};
        Function: test_
        Parameter: flag
        Body:
            If flag[0] && 1 Then
                For(i = 0, i < upp(upp(i)), s()) Do
                    update(f, i, d[i]);
                EndFor.
            ElseIf flag[2] && 2 Then
                Return;
            ElseIf all(flag, {0,1,2,3,4,5,6}) Then
                test_(flag[i]);
            ElseIf !flag Then
                Break;
            ElseIf is___(flag) Then
                flag = flag * ad - 123 + {1,2} % "124";
            Else
                println("da");
                delete(flag);
            EndIf.
        EndBody.
        Function: main
        Parameter: flags[100], len
        Body:
            For(i = 0, i < len, 1) Do
                test_(flags[i]);
            EndFor.
            Return 0;
        EndBody."""
        expect = Program([VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], IntLiteral(120)),
                          VarDecl(Id('c'), [], StringLiteral("""123""")),
                          VarDecl(Id('d'), [10], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(5)])),
                          VarDecl(Id('f'), [], ArrayLiteral(
                              [IntLiteral(12), IntLiteral(3), IntLiteral(4), ArrayLiteral([ArrayLiteral([])])])),
                          FuncDecl(Id('test_'), [VarDecl(Id('flag'), [], None)], ([], [If([(BinaryOp('&&', ArrayCell(
                              Id('flag'), [IntLiteral(0)]), IntLiteral(1)), [], [For(Id('i'), IntLiteral(0),
                                                                                     BinaryOp('<', Id('i'),
                                                                                              CallExpr(Id('upp'), [
                                                                                                  CallExpr(Id('upp'), [
                                                                                                      Id('i')])])),
                                                                                     CallExpr(Id('s'), []), ([], [
                                  CallStmt(Id('update'), [Id('f'), Id('i'), ArrayCell(Id('d'), [Id('i')])])]))]), (
                                                                                           BinaryOp('&&', ArrayCell(
                                                                                               Id('flag'),
                                                                                               [IntLiteral(2)]),
                                                                                                    IntLiteral(2)), [],
                                                                                           [Return(None)]), (
                                                                                           CallExpr(Id('all'),
                                                                                                    [Id('flag'),
                                                                                                     ArrayLiteral(
                                                                                                         [IntLiteral(0),
                                                                                                          IntLiteral(1),
                                                                                                          IntLiteral(2),
                                                                                                          IntLiteral(3),
                                                                                                          IntLiteral(4),
                                                                                                          IntLiteral(5),
                                                                                                          IntLiteral(
                                                                                                              6)])]),
                                                                                           [], [CallStmt(Id('test_'), [
                                                                                               ArrayCell(Id('flag'),
                                                                                                         [Id('i')])])]),
                                                                                           (
                                                                                           UnaryOp('!', Id('flag')), [],
                                                                                           [Break()]), (
                                                                                           CallExpr(Id('is___'),
                                                                                                    [Id('flag')]), [], [
                                                                                               Assign(Id('flag'),
                                                                                                      BinaryOp('+',
                                                                                                               BinaryOp(
                                                                                                                   '-',
                                                                                                                   BinaryOp(
                                                                                                                       '*',
                                                                                                                       Id(
                                                                                                                           'flag'),
                                                                                                                       Id(
                                                                                                                           'ad')),
                                                                                                                   IntLiteral(
                                                                                                                       123)),
                                                                                                               BinaryOp(
                                                                                                                   '%',
                                                                                                                   ArrayLiteral(
                                                                                                                       [
                                                                                                                           IntLiteral(
                                                                                                                               1),
                                                                                                                           IntLiteral(
                                                                                                                               2)]),
                                                                                                                   StringLiteral(
                                                                                                                       """124"""))))])],
                                                                                          ([], [CallStmt(Id('println'),
                                                                                                         [StringLiteral(
                                                                                                             """da""")]),
                                                                                                CallStmt(Id('delete'), [
                                                                                                    Id('flag')])]))])),
                          FuncDecl(Id('main'), [VarDecl(Id('flags'), [100], None), VarDecl(Id('len'), [], None)], ([], [
                              For(Id('i'), IntLiteral(0), BinaryOp('<', Id('i'), Id('len')), IntLiteral(1),
                                  ([], [CallStmt(Id('test_'), [ArrayCell(Id('flags'), [Id('i')])])])),
                              Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

    def test_case_101(self):
        input = r"""
    Function: main
        Body:
            Var: sum = 0, a = 1;
            While a < 10 Do
                Var: b = 1, prod = 1;
                While b < 10 Do
                    prod = prod * b;
                    b = b + 1;
                EndWhile.
                sum = sum + prod;
                a = a + 1;
            EndWhile.
        EndBody.
    """
        expect = Program([
            FuncDecl(Id("main"), [], ([
                                          VarDecl(Id("sum"), [], IntLiteral(0)),
                                          VarDecl(Id("a"), [], IntLiteral(1))
                                      ], [
                                          While(
                                              BinaryOp("<", Id("a"), IntLiteral(10)),
                                              ([VarDecl(Id("b"), [], IntLiteral(1)),
                                                VarDecl(Id("prod"), [], IntLiteral(1))], [
                                                   While(BinaryOp("<", Id("b"), IntLiteral(10)), ([], [
                                                       Assign(Id("prod"), BinaryOp("*", Id("prod"), Id("b"))),
                                                       Assign(Id("b"), BinaryOp("+", Id("b"), IntLiteral(1)))
                                                   ])),
                                                   Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("prod"))),
                                                   Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))
                                               ]))
                                      ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 401))


