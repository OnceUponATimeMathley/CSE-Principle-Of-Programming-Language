import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test1(self):
        """Miss variable"""
        input = """Var: y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test2(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    # Test expression
    def test3(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            m = [b+3];
        EndBody.
        """
        expect = "Error on line 5 col 16: ["
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test4(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = -.t;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test5(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = !cas; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test6(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =rmit * 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test7(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =wow + 5; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test8(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c =a && b; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test9(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = a >= 12; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test10(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            char = a < 4;
            c = !fx; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    # Test statement
    def test11(self):
        """ Test assign statement """
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            a = 3 + 5 ; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test12(self):
        """ Test if statement """
        input = """ Function: foo 
        Parameter: n , t[1]
        Body: 
            If !a Then b = 0; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test13(self):
        """ Test if elseif else statement """
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            If a==5 Then b = 5;
            ElseIf a==6 Then c=6; 
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test14(self):
        """ Test if else statement """
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; 
            Else c="abx"; 
            EndIf. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test15(self):
        """ For Statement """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test16(self):
        """ For Statement """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            froo(2 + x, 4. \. rt); 
            goo ();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test17(self):
        """ test simple function """
        input = """Function: foo 
        Parameter: n 
        Body: 
        x = 110; 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test18(self):
        """ test empty body function """
        input = """Function: foo 
        Parameter: n 
        Body: 

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test19(self):
        """ test empty body, list parameter function """
        input = """Function: foo 
        Parameter: n, a[10], check
        Body: 

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test20(self):
        """ test return_stmt in function """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return break;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test21(self):
        """ test return_stmt in function """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 2);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test22(self):
        """ test call function """
        input = """Function: foo 
        Parameter: n
        Body: 
            x = 10;
            fact (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test23(self):
        """ test while function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 9.0e-2;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test24(self):
        """ test index operator function """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test25(self):
        """ test  """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. t;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test26(self):
        """ test do while stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                x= x+1;
            While x>2.0 
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test27(self):
        """ test break stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test28(self):
        """ test conitnue stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test29(self):
        """ test Global variable declaration """
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,2},{4,5,6}};
        Var: c, d = 4, e, f;
        Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test30(self):
        """ test comment in function """
        input = """Function: foo 
        Parameter: n
        Body: ** Xin chao hello \n**
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test31(self):
        """ test return type of value function """
        input = """
        Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            Else
                Return True;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test32(self):
        """ test var declare function """
        input = """
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[5] = {1,2,3,4.0};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test33(self):
        """ test many else """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (t - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = "Error on line 8 col 12: Else"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test34(self):
        """ test no else """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test35(self):
        """ test assign_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3, 2)];
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test36(self):
        """ test var declare with function"""
        input = """
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test37(self):
        """ test var not at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
            Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody."""
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test38(self):
        """ test var not at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                a[i] = b +. 1.0;
                Var: k = 10;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test39(self):
        """ test var at top list_stmt function """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test40(self):
        """ test nested if """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    Return 1;
                Else 
                    Return 2;
                EndIf.
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test41(self):
        """ test for_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test42(self):
        """ test multi function """
        input = """Function: foo 
        Parameter: n
        Body: 
        EndBody.
        Function: goo 
        Parameter: n
        Body: 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test42(self):
        """ test null stmt while_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do

            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test43(self):
        """ test miss Do in While_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 
                Var: k = 10;
                a[i] = b +. 1.0E+3;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test44(self):
        """ test error break """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x=="ax" Then Return;
                Else Break abc;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 6 col 27: abc"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test45(self):
        """ test error continue """
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue absd;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "Error on line 6 col 30: absd"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test46(self):
        """ test error call_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            fact (x) + 3;
        EndBody."""
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test47(self):
        """ test error return_stmt"""
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 
                If n > 10 Then Return x=3;
                EndIf.
                ;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 16: If"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test48(self):
        """ test var_decl function """
        input = """Function: foo 
        Parameter: n
        Body:
            Var: r = 10., v, f,d;
            r = 10., v;
        EndBody."""
        expect = "Error on line 5 col 19: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test49(self):
        """ test error for_stmt """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 19: =="
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test50(self):
        """ test error scala-type in for_stmt """
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (a[i] = 0, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test51(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (, i != 5, i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test52(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, , i*1) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test53(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (i=0, i != 5,) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 29: )"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test54(self):
        """ test missing for stmt"""
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (,,) Do x=6; EndFor.
        EndBody."""
        expect = "Error on line 5 col 17: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test55(self):
        """ test empty parameter function """
        input = """Var: x;
                   Var: a,b,c;
                   Var: a[100];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test56(self):
        input = """Var: a[100];
                   Var: b[10][200], c[9999], e[];
                """
        expect = "Error on line 2 col 47: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test57(self):
        input = """Var: e[5];
                   Var: decArray[987654321], hexArray[0x123456789][0XABCDEF], octArray[0o1234567][0O5731321];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test58(self):
        input = """ Function: main
                        Body:
                        Var: a, b, c;
                        a = False;
                        b = True;
                        r = False;
                        c = a || b;
                        a = (!(b && c)||!(a && c)||!(a&&b)); 
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test59(self):
        input = """ Function: main
                    Body:
                        Var: a[5][5][9], b = 1.55, c = -10;
                    EndBody.
                    """
        expect = "Error on line 3 col 55: -"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test60(self):
        input = """ Function: testIfStatement
                        Parameter: x, a, b, c
                        Body:
                            If(x == ((False||True) && (a > b + c))) Then
                                a = b - c;
                            Else
                                a = b + c * r;
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test61(self):
        """ test for_stmt """
        input = """Function: foo
                        Parameter: x
                        Body:
                            For (i = 1, i <= x*x*x,i + x ) Do
                                writeln(i);
                            EndFor.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test62(self):
        """ Test while stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While(1) Do
                While(!x) Do
                    x = True;
                EndWhile.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test63(self):
        """ Test miss endwhile stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            While((x > a) && (x < b)) Do
                While((x >= b) || (x >= a)) Do
                    While((x > c * b) && (x < b*b)) Do
                        x = x - 1;
                        c = 2 * c;
                        While( !False ) Do
                            a = a * 32;
                        EndWhile.
                    EndWhile.
                EndWhile.
        EndBody."""
        expect = "Error on line 14 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test64(self):
        """ Test miss EndDo."""
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                x = a + b;
                writeln(x);
            While(True || False || True || (a > b))
        EndBody."""
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test65(self):
        """  """
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
            While();
            EndDo.
        EndBody."""
        expect = "Error on line 5 col 18: )"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test66(self):
        """  """
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                Do
                    While(b!=4);
                While(a!=3);
                EndDo.
            EndDo.
        EndBody."""
        expect = "Error on line 6 col 31: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test67(self):
        """ Test break stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Break;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test68(self):
        """ Test continue stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Continue;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test69(self):
        """ Test complex func_call """
        input = """Function: foo 
        Parameter: n
        Body: 
            test(a,3*7+2+.2,y[1],z[2] + 5,"string",True);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test70(self):
        """ Test return stmt  """
        input = """Function: foo 
        Parameter: n
        Body: 
            Do  
                Return foo(x,y);
            While (True)
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test71(self):
        """ test relational arithmetic """
        input = """Function: foo 
        Parameter: n
        Body: 
            a= (a==b)!= c ;
            x= (x =/= y) <. z >.t;
        EndBody."""
        expect = "Error on line 5 col 30: >."
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test72(self):
        """ test adding operator  """
        input = """Function: foo 
        Parameter: n
        Body: 
            x= (y+3)+. 0.e3 - (z -. -9)*z*z;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test73(self):
        """ test multiplying operator  """
        input = """Function: foo 
        Parameter: n
        Body: 
            ra= (x*3\.2)*. 0x3E \ (y \. 0.123) % 5;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test74(self):
        """ test sign operator """
        input = """Function: foo 
        Parameter: n
        Body:
            a= -3;
            b= -0x123;
            c= -0o77;
            d= -a;
            c= -foo(x); 
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test75(self):
        """ test boolean operator """
        input = """Function: foo 
        Parameter: n
        Body: 
            x = !(True);
            y = (False || True) && True;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test76(self):
        """ Test boolean and expression """
        input = """Function: foo 
        Parameter: n
        Body: 
            compli = !(!(!(y) && z) || (x > 3) !(y < 2));
        EndBody."""
        expect = "Error on line 4 col 47: !"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test77(self):
        """ test index operator """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||False]][b[b[1+0X369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test78(self):
        """ Test func_call expression """
        input = """Function: foo 
        Parameter: n
        Body: 
            a= foo(a,b) + goo (x);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test79(self):
        """ Test funcall_expr  """
        input = """Function: foo 
        Parameter: n
        Body: 
            foo(2.34,"string",-9.2e11);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test80(self):
        """ test simple program """
        input = """Function: foo 
            Parameter: n
            Body: 
            Var : a;
            EndBody.

            Function: program22
            Parameter: e
            Body:
            EndBody.

            Function: main
            Body:
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test81(self):
        """ test missing parameter """
        input = """
            Function: main
            Body:
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test82(self):
        """ Miss parameter  """
        input = """
        Function: foo 
        Parameter: 
        Body: 
        EndBody."""
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test83(self):
        """ Test var_declare   """
        input = """
            Function: main
            Body:
            EndBody.
            Var:x=10;"""
        expect = "Error on line 5 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test84(self):
        """ test array literal """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[123]= {1,2,3};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test85(self):
        """ Test arrayliteral """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[12] = { 1 ,2 , 3};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test86(self):
        """ Test arrayLiteral """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[12] = {"abc",123};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test87(self):
        """ Test array """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[123]={};
            b[1]={{{}}};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test88(self):
        """ Test array """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[12]={{1,2,3},{"abc"},{0.12e3,0X12F,0o456}};
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test89(self):
        """  """
        input = """Function: foo 
        Parameter: n
        Body: 
            array[12]={a,b,c};
        EndBody."""
        expect = "Error on line 4 col 23: a"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test90(self):
        """ Test empty program """
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test91(self):
        """ Test relational operator """
        input = """Function: foo 
        Parameter: n
        Body: 
            If (x == y) || (x != y) Then
                x = ((a >=. 2.3e-13) || (x =/= 2e-35));
            EndIf.
            z = (x < 3) && (y > 4);
            a = (x != z);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test92(self):
        """ Test func_call + expression"""
        input = """Function: foo 
        Parameter: n
        Body: 
            a =(foo(3) != foo(4))* 0.e2;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test93(self):
        """ Test array with comment"""
        input = """Var: x = {{1,2,3}, **Comment here** "abc"};"""
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test94(self):
        """ Check wrong composite type """
        input = """
        Var: x[]=1;
        """
        expect = "Error on line 2 col 15: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test95(self):
        """Check wrong composite type  """
        input = """
        Var: x[12.e3]=1;
        """
        expect = "Error on line 2 col 15: 12.e3"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test96(self):
        """ Check wrong inital-values """
        input = """Var:x[1]=1+2;"""
        expect = "Error on line 1 col 9: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test97(self):
        """ Check var_decl with comment """
        input = """Var **some COMMENT**: ****someid = 3
        **more more**;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test98(self):
        """ Failed funcall """
        input = """ Function: testfuncallexpression
                    Parameter: a,b,c
                    Body:
                        foo;
                    EndBody."""
        expect = "Error on line 4 col 27: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test99(self):
        """ Test no name func """
        input = """Function:
        Parameter: n
        Body: 
        EndBody."""
        expect = "Error on line 2 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test100(self):
        """ Test no body func """
        input = """Function: foo 
        Parameter: n"""
        expect = "Error on line 2 col 20: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test101(self):
        """ Test no body func """
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
        Parameter: n"""
        expect = "Error on line 2 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test102(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: Aa_jacj933 = 00012.21; 
        Function: fact
        Body:
        EndBody."""
        expect = "A"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test103(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x312d], cxa[0x12][0o1][8][0]
        Body:
        EndBody."""
        expect = "Error on line 4 col 45: d"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test104(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        v = (4. \\. 3.);
        Var: t, r= 10.;
        EndBody."""
        expect = "Error on line 8 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test105(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+312.0, r= 10.;
        v = (4. \\. 3.);
        
        EndBody."""
        expect = "Error on line 7 col 39: ."
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test106(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[i], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        

        EndBody."""
        expect = "Error on line 1 col 39: i"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test107(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        
        object = 4 > 7 > 4;

        EndBody."""
        expect = "Error on line 10 col 23: >"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

    def test108(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4>7 && 4 + 4.3 && 4 % !4.e+21e[1] ;

        EndBody."""
        expect = "Error on line 10 col 46: e"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def test109(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4>7 && 4 + 4.3 && 4 % !4.e+21 > e[1]  ;

        EndBody."""
        expect = "Error on line 10 col 47: >"
        self.assertTrue(TestParser.checkParser(input, expect, 309))

    def test110(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4>7 && 4 + 4.3 && 4 % !4.e+21 != e[1];

        EndBody."""
        expect = "Error on line 10 col 47: !="
        self.assertTrue(TestParser.checkParser(input, expect, 310))

    def test111(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4>7 && 4 + 4.3 && 4 % (!4.e+21 != e[1]);

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test112(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = (4>7 && 4 + 4.3 && 4 % (!4.e+21 != e[1]))[4];

        EndBody."""
        expect = "Error on line 10 col 58: ["
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test112(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = (4>7 && 4 + 4.3 && 4 % (!4.e+21 != e[1]))[4];

        EndBody."""
        expect = "Error on line 10 col 58: ["
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test113(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = foo(4>7 && 4 + 4.3 && 4 % (!4.e+21 != e[1]))[4][4];

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 313))

    def test114(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.; 
        
        v = (4. \\. 3.) *.   3.14 *. r * r * a;
        r[5] = {1,2,3};

        object = foo(4>7 && 4 + 4.3 && 4 % (!4.e+21 != e[1]))[4][4] + foo(3,2+3.2<3);

        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 314))

    def test115(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[1], n[10] = {1,2,{"an",5.4},5.e-12};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        While True print("hello");
        EndWhile.

        EndBody."""
        expect = "Error on line 6 col 19: print"
        self.assertTrue(TestParser.checkParser(input, expect, 315))

    def test116(self):
        input = """Function: main
        Body:
            f = f * ffffffff([]); 
        EndBody."""
        expect = "Error on line 6 col 19: print"
        self.assertTrue(TestParser.checkParser(input, expect, 316))