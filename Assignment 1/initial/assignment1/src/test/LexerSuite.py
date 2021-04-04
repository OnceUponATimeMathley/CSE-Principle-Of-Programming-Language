import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("** hcac b* ca","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_8(self):
        self.assertTrue(TestLexer.checkLexeme("""a__MB902bc""","""a__MB902bc,<EOF>""",108))

    def test_9(self):
        self.assertTrue(TestLexer.checkLexeme("""0__MB902bc""","""0,Error Token _""",109))

    def test_10(self):
        self.assertTrue(TestLexer.checkLexeme("""1aMb9__02bc""","""1,aMb9__02bc,<EOF>""",110))

    def test_11(self):
        self.assertTrue(TestLexer.checkLexeme("""1AMb9__02bc""", """1,Error Token A""", 111))

    def test_12(self):
        self.assertTrue(TestLexer.checkLexeme("""BodyBreakTrueFunction""", """Body,Break,True,Function,<EOF>""", 112))

    def test_13(self):
        self.assertTrue(TestLexer.checkLexeme("""odyBreak+ -.1. TrueFunction""", """odyBreak,+,-.,1.,True,Function,<EOF>""", 113))

    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme("""+...--\\ |""", """+.,.,.,-,-,\,Error Token |""", 114))

    def test_15(self):
        self.assertTrue(TestLexer.checkLexeme("""+...--\\ || \\. >=.7 ((()[""", """+.,.,.,-,-,\,||,\.,>=.,7,(,(,(,),[,<EOF>""", 115))

    def test_16(self):
        self.assertTrue(TestLexer.checkLexeme("""0 00 199 0xFF 0XABC
                                                 0o567 0O77""", """0,0,0,199,0xFF,0XABC,0o567,0O77,<EOF>""", 116))
    def test_17(self):
        self.assertTrue(TestLexer.checkLexeme("""12.000e-313.3 12e3 12.e5  312. 32E+1""", """12.000e-313,.,3,12e3,12.e5,312.,32E+1,<EOF>""", 117))

    def test_18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "cas? \\n \\f \\\\" """, """cas? \\n \\f \\\\,<EOF>""", 118))

    def test_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" "cas? have tab:   , '"where? '"" """, """cas? have tab:   , '"where? '",<EOF>""", 119))

    def test_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" {1, 2} {1,2.4, 7.e-3} """, """{,1,,,2,},{,1,,,2.4,,,7.e-3,},<EOF>""", 120))

    def test_21(self):
        self.assertTrue(TestLexer.checkLexeme(""" { 2 , {"ac", {3.3, 9}}, true, {a}, {{{False}}}} """, """{,2,,,{,ac,,,{,3.3,,,9,},},,,true,,,{,a,},,,{,{,{,False,},},},},<EOF>""", 121))

    def test_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" {1,2,3**cmt**,6} """, """{,1,,,2,,,3,,,6,},<EOF>""", 122))

    def test_23(self):
        self.assertTrue(TestLexer.checkLexeme("""{3,5,6**12**,432}""", """{,3,,,5,,,6,,,432,},<EOF>""", 123))

    def test_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" {} """, """{,},<EOF>""", 124))

    def test_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var x = {1,2} , y = "abc" ;""", """Var,x,=,{,1,,,2,},,,y,=,abc,;,<EOF>""", 125))

    def test_26(self):
        self.assertTrue(TestLexer.checkLexeme("""1.24e-7 \\ 32 + bca*.%chh > -1""", """1.24e-7,\,32,+,bca,*.,%,chh,>,-,1,<EOF>""", 126))

    def test_27(self):
        self.assertTrue(TestLexer.checkLexeme("""wfe fac xx[2+3]= 5.666.6""", """wfe,fac,xx,[,2,+,3,],=,5.666,.,6,<EOF>""", 127))

    def test_28(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** wwoc ???## ** """, """<EOF>""", 128))

    def test_29(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** dauc ****ca cs || =\=  """, """Unterminated Comment""", 129))

    def test_30(self):
        self.assertTrue(TestLexer.checkLexeme(""" * * * *** * ** * """, """*,*,*,*,<EOF>""", 130))

    def test_31(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** Multi line
                                                     * ca
                                                    * chcha
                                                    \ ** zz """, """zz,<EOF>""", 131))

    def test_32(self):
        self.assertTrue(TestLexer.checkLexeme(""" "faic tir """, """Unclosed String: faic tir """, 132))

    def test_33(self):
        self.assertTrue(TestLexer.checkLexeme(""" " hac \\x gogo " """, """Illegal Escape In String:  hac \\x""", 133))


    def test_34(self):
        self.assertTrue(TestLexer.checkLexeme(""" " che6.7ck \\\\\\ d\t \\n wow \\ m rek" """, """Illegal Escape In String:  che6.7ck \\\\\\ """, 134))


    def test_35(self):
        self.assertTrue(TestLexer.checkLexeme(""" 01232.3""", """01232.3,<EOF>""", 135))

    def test_36(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc
         def wow" """, """Unclosed String: abc
""", 136))

    def test_37(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** hdac x* """, """Unterminated Comment""", 137))

    def test_38(self):
        self.assertTrue(TestLexer.checkLexeme(""" "chao cac ban \\n \\h '" h" : nice -9,7 """, """Illegal Escape In String: chao cac ban \\n \\h""", 138))

    def test_39(self):
        self.assertTrue(TestLexer.checkLexeme(""" "chao cac ban \\n \\t '" h" : nice -9,7 """, """chao cac ban \\n \\t '" h,:,nice,-,9,,,7,<EOF>""", 139))

    def test_40(self):
        self.assertTrue(TestLexer.checkLexeme(""" True aTrue hello12BreakFunction Do""", """True,aTrue,hello12BreakFunction,Do,<EOF>""", 140))

    def test_41(self):
        self.assertTrue(TestLexer.checkLexeme("""\\\\.\\\\ <.>=.<=  """, """\,\.,\,\,<.,>=.,<=,<EOF>""", 141))

    def test_42(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = 5;""", """Var,:,a,=,5,;,<EOF>""", 142))

    def test_43(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var b[2][3] = {{2,3,4},{4,5,6}}; """, """Var,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},;,<EOF>""", 143))

    def test_44(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: c, d = 6,e,f; """, """Var,:,c,,,d,=,6,,,e,,,f,;,<EOF>""", 144))

    def test_45(self):
        self.assertTrue(TestLexer.checkLexeme("""Var m,n[10]; """, """Var,m,,,n,[,10,],;,<EOF>""", 145))

    def test_46(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: fact """, """Function,:,fact,<EOF>""", 146))

    def test_47(self):
        self.assertTrue(TestLexer.checkLexeme("""Parameter: n""", """Parameter,:,n,<EOF>""", 147))

    def test_48(self):
        self.assertTrue(TestLexer.checkLexeme(""" If n = 0 Then
                                                  Return 1;""", """If,n,=,0,Then,Return,1,;,<EOF>""", 148))
    def test_49(self):
        self.assertTrue(TestLexer.checkLexeme("""Else
                                                    Return n*fact(n-1);
                                                    EndIf.""", """Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,<EOF>""", 149))

    def test_50(self):
        self.assertTrue(TestLexer.checkLexeme(""" [ba[b]a[ba][a]b[ab][a {12312}{123{}{}{ (abv12)(())(Aasd)""", """[,ba,[,b,],a,[,ba,],[,a,],b,[,ab,],[,a,{,12312,},{,123,{,},{,},{,(,abv12,),(,(,),),(,Error Token A""", 150))

    def test_51(self):
        self.assertTrue(TestLexer.checkLexeme("""..asdasd....asdasd......""", """.,.,asdasd,.,.,.,.,asdasd,.,.,.,.,.,.,<EOF>""", 151))

    def test_52(self):
        self.assertTrue(TestLexer.checkLexeme("""asd:AD:ASD:ASD:ASD:ASD:ASD: """, """asd,:,Error Token A""", 152))

    def test_53(self):
        self.assertTrue(TestLexer.checkLexeme("""as;das;das;dasd; """, """as,;,das,;,das,;,dasd,;,<EOF>""", 153))

    def test_54(self):
        self.assertTrue(TestLexer.checkLexeme(""",123,2,31,3,1 """, """,,123,,,2,,,31,,,3,,,1,<EOF>""", 154))

    def test_55(self):
        self.assertTrue(TestLexer.checkLexeme("""a:=a+b """, """a,:,=,a,+,b,<EOF>""", 155))

    def test_56(self):
        self.assertTrue(TestLexer.checkLexeme("""125/*58 """, """125,Error Token /""", 156))

    def test_57(self):
        self.assertTrue(TestLexer.checkLexeme("""div DiV moddiv """, """div,Error Token D""", 157))

    def test_58(self):
        self.assertTrue(TestLexer.checkLexeme("""not OR and notorand""", """not,Error Token O""", 158))

    def test_59(self):
        self.assertTrue(TestLexer.checkLexeme(""" (a+c-f+e*g/e div f mod t)""", """(,a,+,c,-,f,+,e,*,g,Error Token /""", 159))

    def test_60(self):
        self.assertTrue(TestLexer.checkLexeme("""(*//dasdasdasdadsasadads1231312313*) """, """(,*,Error Token /""", 160))

    def test_61(self):
        self.assertTrue(TestLexer.checkLexeme("""//////////////(**){} """, """Error Token /""", 161))

    def test_62(self):
        self.assertTrue(TestLexer.checkLexeme("""procedure foo(); begin print(); end""", """procedure,foo,(,),;,begin,print,(,),;,end,<EOF>""", 162))

    def test_63(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a test '" asdsadasd ' \\f asdasd " """, """Illegal Escape In String: This is a test '" asdsadasd ' """, 163))

    def test_64(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bac""xyc """, """bac,Unclosed String: xyc """, 164))

    def test_65(self):
        self.assertTrue(TestLexer.checkLexeme(""" a+11.2+"mam.123" 12 "%^& """, """a,+,11.2,+,mam.123,12,Unclosed String: %^& """, 165))

    def test_66(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Nk8U;"rA"@Y3*"oV"bh1 """, """Nk8U;,rA,@Y3*,oV,Unclosed String: bh1 """, 166))

    def test_67(self):
        self.assertTrue(TestLexer.checkLexeme(""" a~bc """, """a,Error Token ~""", 167))

    def test_68(self):
        self.assertTrue(TestLexer.checkLexeme(""" BODY int 1.12INTEGER 12and """, """Error Token B""", 168))

    def test_69(self):
        self.assertTrue(TestLexer.checkLexeme(""" oR diVModNTcascEGER Mod nxxottrEu """, """oR,diVModNTcascEGER,Error Token M""", 169))

    def test_70(self):
        self.assertTrue(TestLexer.checkLexeme(""" EndDoccEndForWhWxhileileWhileWhile """, """EndDo,ccEndForWhWxhileileWhileWhile,<EOF>""", 170))

    def test_71(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"\"\"\" """, """,,<EOF>""", 171))

    def test_72(self):
        self.assertTrue(TestLexer.checkLexeme(""" asdf*dsf*.123/ca123/.321 """, """asdf,*,dsf,*.,123,Error Token /""", 172))

    def test_73(self):
        self.assertTrue(TestLexer.checkLexeme(""" =/=6==5<.abd>.0<<<++ """, """=/=,6,==,5,<.,abd,>.,0,<,<,<,+,+,<EOF>""", 173))

    def test_74(self):
        self.assertTrue(TestLexer.checkLexeme("""  3>.12343e """, """3,>.,12343,e,<EOF>""", 174))

    def test_75(self):
        self.assertTrue(TestLexer.checkLexeme(""" **12.e0\\nacabc -101 """, """Unterminated Comment""", 175))

    def test_76(self):
        self.assertTrue(TestLexer.checkLexeme(""" ***** *sAMPLE* """, """*,*,sAMPLE,*,<EOF>""", 176))

    def test_77(self):
        self.assertTrue(TestLexer.checkLexeme(""".e5 .5 01e2.32 +10 """, """.,e5,.,5,01e2,.,32,+,10,<EOF>""", 177))

    def test_78(self):
        self.assertTrue(TestLexer.checkLexeme(""" True + False""", """True,+,False,<EOF>""", 178))

    def test_79(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0.e3 01e3 01.e3 01.0e3 """, """0.e3,01e3,01.e3,01.0e3,<EOF>""", 179))

    def test_80(self):
        self.assertTrue(TestLexer.checkLexeme(""" +abc<>xyzdcb>cv **12mds<>dsd=(*dsd*)*)** """, """+,abc,<,>,xyzdcb,>,cv,<EOF>""", 180))

    def test_81(self):
        self.assertTrue(TestLexer.checkLexeme(""" 13ek3<9**e=9dsae**end*das***d1.nerE """, """13,ek3,<,9,end,*,das,Unterminated Comment""", 181))

    def test_82(self):
        self.assertTrue(TestLexer.checkLexeme(""" "John isn'"t me" """, """John isn'"t me,<EOF>""", 182))

    def test_83(self):
        self.assertTrue(TestLexer.checkLexeme(""" acnv EOF """, """acnv,Error Token E""", 183))

    def test_84(self):
        self.assertTrue(TestLexer.checkLexeme(""" a+11.322+"mam.123" 12 "%^& """, """a,+,11.322,+,mam.123,12,Unclosed String: %^& """, 184))

    def test_85(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var x0.12e51.2 s""", """Var,x0,.,12e51,.,2,s,<EOF>""", 185))

    def test_86(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1 cOn viT xOE rA HAi caI canh ..""", """1,cOn,viT,xOE,rA,Error Token H""", 186))

    def test_87(self):
        self.assertTrue(TestLexer.checkLexeme(""" imposter lol<<<""", """imposter,lol,<,<,<,<EOF>""", 187))

    def test_88(self):
        self.assertTrue(TestLexer.checkLexeme(""" aksdfhak akdfvlahngoiuqwe omvlkasngvoiuwae  """, """aksdfhak,akdfvlahngoiuqwe,omvlkasngvoiuwae,<EOF>""", 188))

    def test_89(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is \\W illegal """, """Unclosed String: This is \W illegal """, 189))

    def test_90(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aa\\f" """, """aa\\f,<EOF>""", 190))

    def test_91(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ULxhskjdhfkja2 """, """Unclosed String: ULxhskjdhfkja2 """, 191))

    def test_92(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1++3 """, """1,+,+,3,<EOF>""", 192))

    def test_93(self):
        self.assertTrue(TestLexer.checkLexeme(""" BODY int 1.12INTEGER 12and """, """Error Token B""", 193))

    def test_94(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**This is not a comment **" 12yz """, """**This is not a comment **,12,yz,<EOF>""", 194))

    def test_95(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """, """,<EOF>""", 195))

    def test_96(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: x = {{1,2,3}, **Comment here** "abc"}; """, """Var,:,x,=,{,{,1,,,2,,,3,},,,abc,},;,<EOF>""", 196))

    def test_97(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" """, """This is a string containing tab 	,<EOF>""", 197))

    def test_98(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" """, """This is a string containing tab \\t,<EOF>""", 198))

    def test_99(self):
        self.assertTrue(TestLexer.checkLexeme(""" <C{ha><b.iet>><<g]hi>><<gi""", """<,Error Token C""", 199))

    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme(""" Xong 100 testcase""", """Error Token X""", 200))
